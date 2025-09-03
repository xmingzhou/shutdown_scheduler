import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import subprocess
import platform
import sys
import os

class ShutdownScheduler:
    def __init__(self, root):
        self.root = root
        self.root.title("定时关机/重启程序")
        self.root.geometry("400x500")  # 增加窗口高度以容纳重启功能
        self.root.resizable(False, False)
        
        # 设置中文字体支持
        self.font_family = self._get_font_family()
        
        # 存储关机/重启任务的时间戳和类型
        self.task_time = None
        self.task_type = None  # 'shutdown' 或 'restart'
        
        # 创建界面
        self.create_widgets()
        
        # 检查系统平台
        self.system = platform.system()
        if self.system not in ["Windows", "Linux", "Darwin"]:
            messagebox.showerror("错误", f"不支持的操作系统: {self.system}")
            root.after(1000, root.destroy)
    
    def _get_font_family(self):
        """获取适用于当前系统的字体族"""
        system = platform.system()
        if system == "Windows":
            return ("SimHei", 10)
        elif system == "Darwin":  # macOS
            return ("Heiti TC", 10)
        elif system == "Linux":
            # Linux系统默认字体
            return ("DejaVu Sans", 10)
        else:
            # 默认字体
            return ("Arial", 10)
    
    def create_widgets(self):
        # 主框架
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 操作类型选择
        ttk.Label(main_frame, text="操作类型:", font=self.font_family).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.operation_var = tk.StringVar(value="shutdown")
        ttk.Radiobutton(main_frame, text="关机", variable=self.operation_var, value="shutdown").grid(row=0, column=1, sticky=tk.W, pady=5)
        ttk.Radiobutton(main_frame, text="重启", variable=self.operation_var, value="restart").grid(row=0, column=2, sticky=tk.W, pady=5)
        
        # 日期选择
        ttk.Label(main_frame, text="日期:", font=self.font_family).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.date_var = tk.StringVar(value=datetime.date.today().strftime("%Y-%m-%d"))
        ttk.Entry(main_frame, textvariable=self.date_var, width=12).grid(row=1, column=1, sticky=tk.W, pady=5)
        ttk.Label(main_frame, text="(YYYY-MM-DD)", font=self.font_family).grid(row=1, column=2, sticky=tk.W, pady=5)
        
        # 时间选择
        ttk.Label(main_frame, text="时间:", font=self.font_family).grid(row=2, column=0, sticky=tk.W, pady=5)
        self.time_var = tk.StringVar(value=datetime.datetime.now().strftime("%H:%M"))
        ttk.Entry(main_frame, textvariable=self.time_var, width=12).grid(row=2, column=1, sticky=tk.W, pady=5)
        ttk.Label(main_frame, text="(HH:MM)", font=self.font_family).grid(row=2, column=2, sticky=tk.W, pady=5)
        
        # 当前状态
        self.status_var = tk.StringVar(value="未设置任务")
        ttk.Label(main_frame, text="状态:", font=self.font_family).grid(row=3, column=0, sticky=tk.W, pady=10)
        ttk.Label(main_frame, textvariable=self.status_var, font=self.font_family, foreground="red").grid(
            row=3, column=1, columnspan=2, sticky=tk.W, pady=10)
        
        # 设置按钮
        ttk.Button(main_frame, text="设置任务", command=self.set_task, width=15).grid(
            row=4, column=0, pady=20)
        
        # 取消任务按钮
        ttk.Button(main_frame, text="取消任务", command=self.cancel_task, width=15).grid(
            row=4, column=1, pady=20)
        
        # 快捷功能标题
        ttk.Label(main_frame, text="快捷关机选项", font=self.font_family, foreground="blue").grid(
            row=5, column=0, columnspan=3, sticky=tk.W, pady=10)
        
        # 快捷按钮 - 第一行
        ttk.Button(main_frame, text="10分钟后", command=lambda: self.set_quick_task(10), width=10).grid(
            row=6, column=0, pady=5)
        ttk.Button(main_frame, text="30分钟后", command=lambda: self.set_quick_task(30), width=10).grid(
            row=6, column=1, pady=5)
        ttk.Button(main_frame, text="1小时后", command=lambda: self.set_quick_task(60), width=10).grid(
            row=6, column=2, pady=5)
        
        # 快捷按钮 - 第二行
        ttk.Button(main_frame, text="2小时后", command=lambda: self.set_quick_task(120), width=10).grid(
            row=7, column=0, pady=5)
        ttk.Button(main_frame, text="4小时后", command=lambda: self.set_quick_task(240), width=10).grid(
            row=7, column=1, pady=5)
        ttk.Button(main_frame, text="8小时后", command=lambda: self.set_quick_task(480), width=10).grid(
            row=7, column=2, pady=5)
        
        # 快捷按钮 - 第三行
        ttk.Button(main_frame, text="明日7:30", command=self.set_task_tomorrow_morning, width=15).grid(
            row=8, column=0, columnspan=3, pady=10)
        
        # 开发者信息
        ttk.Label(main_frame, text="© 2025 ZXM", font=("Arial", 8)).grid(
            row=9, column=0, columnspan=3, pady=10)
    
    def set_task(self):
        """设置关机/重启任务"""
        try:
            # 获取用户输入的日期和时间
            date_str = self.date_var.get()
            time_str = self.time_var.get()
            
            # 解析日期和时间
            task_datetime = datetime.datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
            
            # 检查日期是否在过去
            current_time = datetime.datetime.now()
            if task_datetime < current_time:
                messagebox.showerror("错误", "设置的时间不能早于当前时间!")
                return
            
            # 获取操作类型
            self.task_type = self.operation_var.get()
            operation_text = "关机" if self.task_type == "shutdown" else "重启"
            
            # 计算还有多少秒执行任务
            seconds_until_task = (task_datetime - current_time).total_seconds()
            
            # 根据不同系统执行命令
            if self.system == "Windows":
                if self.task_type == "shutdown":
                    subprocess.run(["shutdown", "/s", "/t", str(int(seconds_until_task))], check=True)
                else:  # restart
                    subprocess.run(["shutdown", "/r", "/t", str(int(seconds_until_task))], check=True)
            elif self.system in ["Linux", "Darwin"]:
                if self.task_type == "shutdown":
                    subprocess.run(["shutdown", "-h", f"+{int(seconds_until_task // 60)}"], check=True)
                else:  # restart
                    subprocess.run(["shutdown", "-r", f"+{int(seconds_until_task // 60)}"], check=True)
            
            # 更新状态
            self.task_time = task_datetime
            time_display = task_datetime.strftime("%Y-%m-%d %H:%M:%S")
            self.status_var.set(f"系统将于 {time_display} {operation_text}")
            
            messagebox.showinfo("成功", f"已设置系统在 {time_display} {operation_text}")
            
        except ValueError as e:
            messagebox.showerror("格式错误", f"日期或时间格式不正确: {e}")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("命令执行失败", f"设置{operation_text}失败: {e}")
        except Exception as e:
            messagebox.showerror("错误", f"发生未知错误: {e}")
    
    def cancel_task(self):
        """取消已设置的任务"""
        try:
            if self.task_time is None:
                messagebox.showinfo("提示", "没有任务需要取消")
                return
            
            # 根据不同系统执行取消命令
            if self.system == "Windows":
                subprocess.run(["shutdown", "/a"], check=True)
            elif self.system in ["Linux", "Darwin"]:
                subprocess.run(["shutdown", "-c"], check=True)
            
            # 更新状态
            self.task_time = None
            self.task_type = None
            self.status_var.set("未设置任务")
            
            messagebox.showinfo("成功", "已取消任务")
            
        except subprocess.CalledProcessError as e:
            messagebox.showerror("命令执行失败", f"取消任务失败: {e}")
        except Exception as e:
            messagebox.showerror("错误", f"发生未知错误: {e}")
    
    def set_quick_task(self, minutes):
        """设置快速任务，参数为分钟数"""
        # 计算任务时间
        current_time = datetime.datetime.now()
        task_datetime = current_time + datetime.timedelta(minutes=minutes)
        
        # 更新日期和时间输入框
        self.date_var.set(task_datetime.strftime("%Y-%m-%d"))
        self.time_var.set(task_datetime.strftime("%H:%M"))
        
        # 直接调用设置任务
        self.set_task()
    
    def set_task_tomorrow_morning(self):
        """设置明日早上7:30的任务"""
        # 获取当前日期
        today = datetime.date.today()
        # 计算明天的日期
        tomorrow = today + datetime.timedelta(days=1)
        # 设置时间为7:30
        tomorrow_morning = datetime.datetime.combine(tomorrow, datetime.time(7, 30))
        
        # 如果当前时间已经超过今天的7:30，计算明天的7:30
        current_time = datetime.datetime.now()
        if current_time > tomorrow_morning:
            tomorrow_morning += datetime.timedelta(days=1)
        
        # 更新日期和时间输入框
        self.date_var.set(tomorrow_morning.strftime("%Y-%m-%d"))
        self.time_var.set(tomorrow_morning.strftime("%H:%M"))
        
        # 直接调用设置任务
        self.set_task()

if __name__ == "__main__":
    root = tk.Tk()
    app = ShutdownScheduler(root)
    root.mainloop()    