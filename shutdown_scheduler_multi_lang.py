# The Shutdown Scheduler program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

# Copyright (c) 2025 Xiangming Zhou

# SUPPLEMENTARY DISCLAIMER
# The copyright holder assumes no responsibility for any illegal use of this software,
# or for any data loss, damages, or other liabilities arising directly or indirectly
# from its use. The user of this software assumes all risks and full responsibility
# for compliance with all applicable local, national, and international laws.
# If you find this software useful, a voluntary economic contribution to the author
# is appreciated but not required.


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
        self.root.title("Shutdown/Restart Scheduler")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Language support
        self.languages = {
            "English": {
                "title": "Shutdown/Restart Scheduler",
                "operation_type": "Operation Type:",
                "shutdown": "Shutdown",
                "restart": "Restart",
                "date": "Date:",
                "date_format": "(YYYY-MM-DD)",
                "time": "Time:",
                "time_format": "(HH:MM)",
                "status": "Status:",
                "no_task": "No task scheduled",
                "set_task": "Set Task",
                "cancel_task": "Cancel Task",
                "quick_options": "Quick Shutdown Options",
                "minutes_later": " minutes later",
                "tomorrow_morning": "Tomorrow 7:30",
                "developer_info": "© 2025 ZXM",
                "success": "Success",
                "error": "Error",
                "format_error": "Format Error",
                "command_failed": "Command Execution Failed",
                "unknown_error": "Unknown Error",
                "time_in_past": "The selected time cannot be earlier than the current time!",
                "no_task_to_cancel": "There is no task to cancel",
                "task_canceled": "Task has been canceled",
                "system_will": "System will ",
                "at": " at ",
                "shutdown_text": "shutdown",
                "restart_text": "restart",
                "task_set": "Task has been set to "
            },
            "中文": {
                "title": "定时关机/重启程序",
                "operation_type": "操作类型:",
                "shutdown": "关机",
                "restart": "重启",
                "date": "日期:",
                "date_format": "(YYYY-MM-DD)",
                "time": "时间:",
                "time_format": "(HH:MM)",
                "status": "状态:",
                "no_task": "未设置任务",
                "set_task": "设置任务",
                "cancel_task": "取消任务",
                "quick_options": "快捷关机选项",
                "minutes_later": "分钟后",
                "tomorrow_morning": "明日7:30",
                "developer_info": "© 2025 ZXM",
                "success": "成功",
                "error": "错误",
                "format_error": "格式错误",
                "command_failed": "命令执行失败",
                "unknown_error": "发生未知错误",
                "time_in_past": "设置的时间不能早于当前时间!",
                "no_task_to_cancel": "没有任务需要取消",
                "task_canceled": "已取消任务",
                "system_will": "系统将于",
                "at": "",
                "shutdown_text": "关机",
                "restart_text": "重启",
                "task_set": "已设置系统在"
            },
            "Français": {
                "title": "Planificateur d'arrêt/redémarrage",
                "operation_type": "Type d'opération:",
                "shutdown": "Arrêt",
                "restart": "Redémarrage",
                "date": "Date:",
                "date_format": "(AAAA-MM-JJ)",
                "time": "Heure:",
                "time_format": "(HH:MM)",
                "status": "État:",
                "no_task": "Aucune tâche planifiée",
                "set_task": "Planifier la tâche",
                "cancel_task": "Annuler la tâche",
                "quick_options": "Options rapides",
                "minutes_later": " minutes plus tard",
                "tomorrow_morning": "Demain 7:30",
                "developer_info": "© 2025 ZXM",
                "success": "Succès",
                "error": "Erreur",
                "format_error": "Erreur de format",
                "command_failed": "Échec de l'exécution de la commande",
                "unknown_error": "Erreur inconnue",
                "time_in_past": "L'heure sélectionnée ne peut pas être antérieure à l'heure actuelle!",
                "no_task_to_cancel": "Il n'y a pas de tâche à annuler",
                "task_canceled": "Tâche annulée",
                "system_will": "Le système va ",
                "at": " à ",
                "shutdown_text": "s'arrêter",
                "restart_text": "redémarrer",
                "task_set": "La tâche a été planifiée pour "
            },
            "日本語": {
                "title": "シャットダウン/再起動スケジューラ",
                "operation_type": "操作タイプ:",
                "shutdown": "シャットダウン",
                "restart": "再起動",
                "date": "日付:",
                "date_format": "(YYYY-MM-DD)",
                "time": "時間:",
                "time_format": "(HH:MM)",
                "status": "状態:",
                "no_task": "タスク未設定",
                "set_task": "タスク設定",
                "cancel_task": "タスク取消",
                "quick_options": "ショートカット",
                "minutes_later": "分後",
                "tomorrow_morning": "明日の7:30",
                "developer_info": "© 2025 ZXM",
                "success": "成功",
                "error": "エラー",
                "format_error": "形式エラー",
                "command_failed": "コマンド実行失敗",
                "unknown_error": "不明なエラー",
                "time_in_past": "選択した時間は現在より前に設定できません！",
                "no_task_to_cancel": "キャンセルするタスクはありません",
                "task_canceled": "タスクをキャンセルしました",
                "system_will": "システムは",
                "at": "に",
                "shutdown_text": "シャットダウンします",
                "restart_text": "再起動します",
                "task_set": "タスクは"
            }
        }
        
        # Current language
        self.current_language = "中文"
        
        # Store the timestamp and type of shutdown/restart task
        self.task_time = None
        self.task_type = None  # 'shutdown' or 'restart'
        
        # Create UI
        self.create_widgets()
        
        # Check system platform
        self.system = platform.system()
        if self.system not in ["Windows", "Linux", "Darwin"]:
            messagebox.showerror(self.get_text("error"), f"Unsupported operating system: {self.system}")
            root.after(1000, root.destroy)
    
    def get_text(self, key):
        """Get translated text based on current language"""
        return self.languages[self.current_language][key]
    
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Language selection
        ttk.Label(main_frame, text="Language:", font=("Arial", 9)).grid(row=0, column=0, columnspan=3, sticky=tk.W, pady=5)
        self.language_var = tk.StringVar(value=self.current_language)
        language_combo = ttk.Combobox(main_frame, textvariable=self.language_var, values=list(self.languages.keys()), state="readonly", width=10)
        language_combo.grid(row=0, column=2, sticky=tk.E, pady=5)
        language_combo.bind("<<ComboboxSelected>>", self.change_language)
        
        # Operation type selection
        ttk.Label(main_frame, text=self.get_text("operation_type"), font=("Arial", 10)).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.operation_var = tk.StringVar(value="shutdown")
        ttk.Radiobutton(main_frame, text=self.get_text("shutdown"), variable=self.operation_var, value="shutdown").grid(row=1, column=1, sticky=tk.W, pady=5)
        ttk.Radiobutton(main_frame, text=self.get_text("restart"), variable=self.operation_var, value="restart").grid(row=1, column=2, sticky=tk.W, pady=5)
        
        # Date selection
        ttk.Label(main_frame, text=self.get_text("date"), font=("Arial", 10)).grid(row=2, column=0, sticky=tk.W, pady=5)
        self.date_var = tk.StringVar(value=datetime.date.today().strftime("%Y-%m-%d"))
        ttk.Entry(main_frame, textvariable=self.date_var, width=12).grid(row=2, column=1, sticky=tk.W, pady=5)
        ttk.Label(main_frame, text=self.get_text("date_format"), font=("Arial", 8)).grid(row=2, column=2, sticky=tk.W, pady=5)
        
        # Time selection
        ttk.Label(main_frame, text=self.get_text("time"), font=("Arial", 10)).grid(row=3, column=0, sticky=tk.W, pady=5)
        self.time_var = tk.StringVar(value=datetime.datetime.now().strftime("%H:%M"))
        ttk.Entry(main_frame, textvariable=self.time_var, width=12).grid(row=3, column=1, sticky=tk.W, pady=5)
        ttk.Label(main_frame, text=self.get_text("time_format"), font=("Arial", 8)).grid(row=3, column=2, sticky=tk.W, pady=5)
        
        # Current status
        self.status_var = tk.StringVar(value=self.get_text("no_task"))
        ttk.Label(main_frame, text=self.get_text("status"), font=("Arial", 10)).grid(row=4, column=0, sticky=tk.W, pady=10)
        ttk.Label(main_frame, textvariable=self.status_var, font=("Arial", 10), foreground="red").grid(
            row=4, column=1, columnspan=2, sticky=tk.W, pady=10)
        
        # Set task button
        ttk.Button(main_frame, text=self.get_text("set_task"), command=self.set_task, width=15).grid(
            row=5, column=0, pady=20)
        
        # Cancel task button
        ttk.Button(main_frame, text=self.get_text("cancel_task"), command=self.cancel_task, width=15).grid(
            row=5, column=1, pady=20)
        
        # Quick function title
        ttk.Label(main_frame, text=self.get_text("quick_options"), font=("Arial", 10, "underline"), foreground="blue").grid(
            row=6, column=0, columnspan=3, sticky=tk.W, pady=10)
        
        # Quick buttons - First row
        ttk.Button(main_frame, text="10" + self.get_text("minutes_later"), command=lambda: self.set_quick_task(10), width=10).grid(
            row=7, column=0, pady=5)
        ttk.Button(main_frame, text="30" + self.get_text("minutes_later"), command=lambda: self.set_quick_task(30), width=10).grid(
            row=7, column=1, pady=5)
        ttk.Button(main_frame, text="1" + self.get_text("minutes_later").replace("s", ""), command=lambda: self.set_quick_task(60), width=10).grid(
            row=7, column=2, pady=5)
        
        # Quick buttons - Second row
        ttk.Button(main_frame, text="2" + self.get_text("minutes_later").replace("s", ""), command=lambda: self.set_quick_task(120), width=10).grid(
            row=8, column=0, pady=5)
        ttk.Button(main_frame, text="4" + self.get_text("minutes_later").replace("s", ""), command=lambda: self.set_quick_task(240), width=10).grid(
            row=8, column=1, pady=5)
        ttk.Button(main_frame, text="8" + self.get_text("minutes_later").replace("s", ""), command=lambda: self.set_quick_task(480), width=10).grid(
            row=8, column=2, pady=5)
        
        # Quick buttons - Third row
        ttk.Button(main_frame, text=self.get_text("tomorrow_morning"), command=self.set_task_tomorrow_morning, width=15).grid(
            row=9, column=0, columnspan=3, pady=10)
        
        # Developer information
        ttk.Label(main_frame, text=self.get_text("developer_info"), font=("Arial", 8)).grid(
            row=10, column=0, columnspan=3, pady=10)
    
    def change_language(self, event=None):
        """Change the language of the interface"""
        new_language = self.language_var.get()
        if new_language != self.current_language:
            self.current_language = new_language
            self.root.title(self.get_text("title"))
            self.update_ui_text()
    
    def update_ui_text(self):
        """Update all UI elements with the current language"""
        # Get all widgets in the main frame
        main_frame = self.root.winfo_children()[0]
        for widget in main_frame.winfo_children():
            widget_type = widget.winfo_class()
            
            if widget_type == "TLabel":
                # Update label text
                if widget.cget("textvariable") == "":
                    # Find the corresponding text key
                    for key, value in self.languages[self.current_language].items():
                        if widget.cget("text") == self.languages[list(self.languages.keys())[0]][key]:
                            widget.config(text=value)
                            break
            
            elif widget_type == "TRadiobutton":
                # Update radiobutton text
                if widget.cget("value") == "shutdown":
                    widget.config(text=self.get_text("shutdown"))
                elif widget.cget("value") == "restart":
                    widget.config(text=self.get_text("restart"))
            
            elif widget_type == "TButton":
                # Update button text
                current_text = widget.cget("text")
                if current_text.startswith(tuple([lang["set_task"] for lang in self.languages.values()])):
                    widget.config(text=self.get_text("set_task"))
                elif current_text.startswith(tuple([lang["cancel_task"] for lang in self.languages.values()])):
                    widget.config(text=self.get_text("cancel_task"))
                elif current_text == list(self.languages.values())[0]["quick_options"]:
                    widget.config(text=self.get_text("quick_options"))
                elif current_text == list(self.languages.values())[0]["tomorrow_morning"]:
                    widget.config(text=self.get_text("tomorrow_morning"))
                elif current_text.endswith(tuple([lang["minutes_later"] for lang in self.languages.values()])):
                    # Handle quick buttons
                    minutes = current_text.split()[0]
                    widget.config(text=minutes + self.get_text("minutes_later"))
                elif current_text.endswith(tuple([lang["minutes_later"].replace("s", "") for lang in self.languages.values()])):
                    # Handle quick buttons with "hour"
                    hours = current_text.split()[0]
                    widget.config(text=hours + self.get_text("minutes_later").replace("s", ""))
    
    def set_task(self):
        """Set a shutdown/restart task"""
        try:
            # Get user input for date and time
            date_str = self.date_var.get()
            time_str = self.time_var.get()
            
            # Parse date and time
            task_datetime = datetime.datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
            
            # Check if the date is in the past
            current_time = datetime.datetime.now()
            if task_datetime < current_time:
                messagebox.showerror(self.get_text("error"), self.get_text("time_in_past"))
                return
            
            # Get operation type
            self.task_type = self.operation_var.get()
            operation_text = self.get_text("shutdown_text") if self.task_type == "shutdown" else self.get_text("restart_text")
            
            # Calculate seconds until task execution
            seconds_until_task = (task_datetime - current_time).total_seconds()
            
            # Execute command based on system
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
            
            # Update status
            self.task_time = task_datetime
            time_display = task_datetime.strftime("%Y-%m-%d %H:%M:%S")
            self.status_var.set(f"{self.get_text('system_will')}{time_display}{self.get_text('at')}{operation_text}")
            
            messagebox.showinfo(self.get_text("success"), f"{self.get_text('task_set')}{time_display}{self.get_text('at')}{operation_text}")
            
        except ValueError as e:
            messagebox.showerror(self.get_text("format_error"), f"Invalid date or time format: {e}")
        except subprocess.CalledProcessError as e:
            messagebox.showerror(self.get_text("command_failed"), f"Failed to set {operation_text}: {e}")
        except Exception as e:
            messagebox.showerror(self.get_text("unknown_error"), f"An unknown error occurred: {e}")
    
    def cancel_task(self):
        """Cancel the scheduled task"""
        try:
            if self.task_time is None:
                messagebox.showinfo(self.get_text("info"), self.get_text("no_task_to_cancel"))
                return
            
            # Execute cancel command based on system
            if self.system == "Windows":
                subprocess.run(["shutdown", "-a"], check=True)
            elif self.system in ["Linux", "Darwin"]:
                subprocess.run(["shutdown", "-c"], check=True)
            
            # Update status
            self.task_time = None
            self.task_type = None
            self.status_var.set(self.get_text("no_task"))
            
            messagebox.showinfo(self.get_text("success"), self.get_text("task_canceled"))
            
        except subprocess.CalledProcessError as e:
            messagebox.showerror(self.get_text("command_failed"), f"Failed to cancel task: {e}")
        except Exception as e:
            messagebox.showerror(self.get_text("unknown_error"), f"An unknown error occurred: {e}")
    
    def set_quick_task(self, minutes):
        """Set a quick task with specified minutes"""
        # Calculate task time
        current_time = datetime.datetime.now()
        task_datetime = current_time + datetime.timedelta(minutes=minutes)
        
        # Update date and time inputs
        self.date_var.set(task_datetime.strftime("%Y-%m-%d"))
        self.time_var.set(task_datetime.strftime("%H:%M"))
        
        # Set the task
        self.set_task()
    
    def set_task_tomorrow_morning(self):
        """Set a task for 7:30 tomorrow morning"""
        # Get current date
        today = datetime.date.today()
        # Calculate tomorrow's date
        tomorrow = today + datetime.timedelta(days=1)
        # Set time to 7:30
        tomorrow_morning = datetime.datetime.combine(tomorrow, datetime.time(7, 30))
        
        # If current time is already past 7:30 today, calculate 7:30 the day after tomorrow
        current_time = datetime.datetime.now()
        if current_time > tomorrow_morning:
            tomorrow_morning += datetime.timedelta(days=1)
        
        # Update date and time inputs
        self.date_var.set(tomorrow_morning.strftime("%Y-%m-%d"))
        self.time_var.set(tomorrow_morning.strftime("%H:%M"))
        
        # Set the task
        self.set_task()

if __name__ == "__main__":
    root = tk.Tk()
    app = ShutdownScheduler(root)

    root.mainloop()    
