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
import os

class ShutdownScheduler:
    def __init__(self, root):
        self.root = root
        self.root.title("Shutdown/Restart Scheduler")
        self.root.geometry("400x620") # Adjusted geometry again for new buttons
        self.root.resizable(False, False)
        
        # Language support
        self.languages = {
            "English": {
                "title": "Shutdown/Restart Scheduler",
                "operation_type": "Operation Type:",
                "shutdown": "Shutdown",
                "restart": "Restart",
                "date": "Date:",
                "year": "Year:",
                "month": "Month:",
                "day": "Day:",
                "time": "Time:",
                "hour": "Hour:", # New
                "minute": "Minute:", # New
                "second": "Second:", # New
                "time_format": "(HH:MM:SS)", # Updated
                "status": "Status:",
                "no_task": "No task scheduled",
                "set_task": "Set Task",
                "cancel_task": "Cancel Task",
                "quick_options": "Quick Shutdown Options",
                "minutes_later": " minutes later",
                "tomorrow_morning": "Tomorrow 7:30",
                "tomorrow_eight": "Tomorrow 8:00", # New
                "saturday_morning": "Saturday 7:30", # New
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
                "task_set": "Task has been set to ",
                "cancelling_existing": "Cancelling existing task..." # New
            },
            "中文": {
                "title": "定时关机/重启程序",
                "operation_type": "操作类型:",
                "shutdown": "关机",
                "restart": "重启",
                "date": "日期:",
                "year": "年份:",
                "month": "月份:",
                "day": "日期:",
                "time": "时间:",
                "hour": "小时:", # New
                "minute": "分钟:", # New
                "second": "秒:", # New
                "time_format": "(时:分:秒)", # Updated
                "status": "状态:",
                "no_task": "未设置任务",
                "set_task": "设置任务",
                "cancel_task": "取消任务",
                "quick_options": "快捷关机选项",
                "minutes_later": "分钟后",
                "tomorrow_morning": "明日7:30",
                "tomorrow_eight": "明日8:00", # New
                "saturday_morning": "周六7:30", # New
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
                "task_set": "已设置系统在",
                "cancelling_existing": "正在取消现有任务..." # New
            },
            "Français": {
                "title": "Planificateur d'arrêt/redémarrage",
                "operation_type": "Type d'opération:",
                "shutdown": "Arrêt",
                "restart": "Redémarrage",
                "date": "Date:",
                "year": "Année:",
                "month": "Mois:",
                "day": "Jour:",
                "time": "Heure:",
                "hour": "Heure:", # New
                "minute": "Minute:", # New
                "second": "Seconde:", # New
                "time_format": "(HH:MM:SS)", # Updated
                "status": "État:",
                "no_task": "Aucune tâche planifiée",
                "set_task": "Planifier la tâche",
                "cancel_task": "Annuler la tâche",
                "quick_options": "Options rapides",
                "minutes_later": " minutes plus tard",
                "tomorrow_morning": "Demain 7:30",
                "tomorrow_eight": "Demain 8:00", # New
                "saturday_morning": "Samedi 7:30", # New
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
                "task_set": "La tâche a été planifiée pour ",
                "cancelling_existing": "Annulation de la tâche existante..." # New
            },
            "日本語": {
                "title": "シャットダウン/再起動スケジューラ",
                "operation_type": "操作タイプ:",
                "shutdown": "シャットダウン",
                "restart": "再起動",
                "date": "日付:",
                "year": "年:",
                "month": "月:",
                "day": "日:",
                "time": "時間:",
                "hour": "時:", # New
                "minute": "分:", # New
                "second": "秒:", # New
                "time_format": "(HH:MM:SS)", # Updated
                "status": "状態:",
                "no_task": "タスク未設定",
                "set_task": "タスク設定",
                "cancel_task": "タスク取消",
                "quick_options": "ショートカット",
                "minutes_later": "分後",
                "tomorrow_morning": "明日の7:30",
                "tomorrow_eight": "明日の8:00", # New
                "saturday_morning": "土曜日の7:30", # New
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
                "task_set": "タスクは",
                "cancelling_existing": "既存のタスクをキャンセル中..." # New
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
    
    def generate_years(self):
        """Generate a list of years for the dropdown (e.g., current year - 2 years to current year + 10 years)"""
        current_year = datetime.date.today().year
        # 修改了年份范围：从当前年份往前推2年到往后推10年
        return [str(year) for year in range(current_year - 2, current_year + 11)] 
    
    def generate_months(self):
        """Generate a list of months for the dropdown (1-12)"""
        return [f"{m:02d}" for m in range(1, 13)]

    def generate_days(self, year, month):
        """Generate a list of days for the dropdown based on selected year and month"""
        try:
            year = int(year)
            month = int(month)
            # Get the number of days in the selected month
            if month == 2: # February
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): # Leap year
                    num_days = 29
                else:
                    num_days = 28
            elif month in [4, 6, 9, 11]: # April, June, September, November
                num_days = 30
            else: # Other months
                num_days = 31
            return [f"{d:02d}" for d in range(1, num_days + 1)]
        except ValueError:
            return [f"{d:02d}" for d in range(1, 32)] # Fallback to 1-31 if invalid year/month for manual input

    def generate_hours(self):
        """Generate a list of hours for the dropdown (00-23)"""
        return [f"{h:02d}" for h in range(24)]

    def generate_minutes(self):
        """Generate a list of minutes for the dropdown (00-59)"""
        return [f"{m:02d}" for m in range(60)]

    def generate_seconds(self):
        """Generate a list of seconds for the dropdown (00-59)"""
        return [f"{s:02d}" for s in range(60)]

    def update_days_dropdown(self, event=None):
        """Update the list of days when year or month changes"""
        selected_year = self.year_var.get()
        selected_month = self.month_var.get()
        new_days = self.generate_days(selected_year, selected_month)
        self.day_combobox.config(values=new_days)
        # Ensure the selected day is still valid, otherwise reset
        if self.day_var.get() not in new_days and new_days:
            self.day_var.set(new_days[0]) # Default to the first day if current day is invalid

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
        
        # Date selection (Dropdowns: Year, Month, Day)
        current_date = datetime.date.today()

        ttk.Label(main_frame, text=self.get_text("year"), font=("Arial", 10)).grid(row=2, column=0, sticky=tk.W, pady=5)
        self.year_var = tk.StringVar(value=str(current_date.year))
        # Changed state to "normal"
        self.year_combobox = ttk.Combobox(main_frame, textvariable=self.year_var, values=self.generate_years(), state="normal", width=7)
        self.year_combobox.grid(row=2, column=1, sticky=tk.W, pady=5)
        self.year_combobox.bind("<<ComboboxSelected>>", self.update_days_dropdown)
        # Add event binding for manual input change
        self.year_combobox.bind("<FocusOut>", self.update_days_dropdown)
        self.year_combobox.bind("<Return>", self.update_days_dropdown) # Press Enter to update

        ttk.Label(main_frame, text=self.get_text("month"), font=("Arial", 10)).grid(row=3, column=0, sticky=tk.W, pady=5)
        self.month_var = tk.StringVar(value=f"{current_date.month:02d}")
        # Changed state to "normal"
        self.month_combobox = ttk.Combobox(main_frame, textvariable=self.month_var, values=self.generate_months(), state="normal", width=7)
        self.month_combobox.grid(row=3, column=1, sticky=tk.W, pady=5)
        self.month_combobox.bind("<<ComboboxSelected>>", self.update_days_dropdown)
        # Add event binding for manual input change
        self.month_combobox.bind("<FocusOut>", self.update_days_dropdown)
        self.month_combobox.bind("<Return>", self.update_days_dropdown)

        ttk.Label(main_frame, text=self.get_text("day"), font=("Arial", 10)).grid(row=4, column=0, sticky=tk.W, pady=5)
        self.day_var = tk.StringVar(value=f"{current_date.day:02d}")
        # Changed state to "normal"
        self.day_combobox = ttk.Combobox(main_frame, textvariable=self.day_var, values=self.generate_days(current_date.year, current_date.month), state="normal", width=7)
        self.day_combobox.grid(row=4, column=1, sticky=tk.W, pady=5)
        # No specific update_days_dropdown for day_combobox needed as it's the target

        # Time selection (Dropdowns: Hour, Minute, Second)
        current_time_dt = datetime.datetime.now()

        ttk.Label(main_frame, text=self.get_text("hour"), font=("Arial", 10)).grid(row=5, column=0, sticky=tk.W, pady=5)
        self.hour_var = tk.StringVar(value=f"{current_time_dt.hour:02d}")
        # Changed state to "normal"
        self.hour_combobox = ttk.Combobox(main_frame, textvariable=self.hour_var, values=self.generate_hours(), state="normal", width=7)
        self.hour_combobox.grid(row=5, column=1, sticky=tk.W, pady=5)

        ttk.Label(main_frame, text=self.get_text("minute"), font=("Arial", 10)).grid(row=6, column=0, sticky=tk.W, pady=5)
        self.minute_var = tk.StringVar(value=f"{current_time_dt.minute:02d}")
        # Changed state to "normal"
        self.minute_combobox = ttk.Combobox(main_frame, textvariable=self.minute_var, values=self.generate_minutes(), state="normal", width=7)
        self.minute_combobox.grid(row=6, column=1, sticky=tk.W, pady=5)

        ttk.Label(main_frame, text=self.get_text("second"), font=("Arial", 10)).grid(row=7, column=0, sticky=tk.W, pady=5)
        self.second_var = tk.StringVar(value=f"{current_time_dt.second:02d}")
        # Changed state to "normal"
        self.second_combobox = ttk.Combobox(main_frame, textvariable=self.second_var, values=self.generate_seconds(), state="normal", width=7)
        self.second_combobox.grid(row=7, column=1, sticky=tk.W, pady=5)

        ttk.Label(main_frame, text=self.get_text("time_format"), font=("Arial", 8)).grid(row=7, column=2, sticky=tk.W, pady=5)
        
        # Current status
        self.status_var = tk.StringVar(value=self.get_text("no_task"))
        ttk.Label(main_frame, text=self.get_text("status"), font=("Arial", 10)).grid(row=8, column=0, sticky=tk.W, pady=10)
        ttk.Label(main_frame, textvariable=self.status_var, font=("Arial", 10), foreground="red").grid(
            row=8, column=1, columnspan=2, sticky=tk.W, pady=10)
        
        # Set task button
        ttk.Button(main_frame, text=self.get_text("set_task"), command=self.set_task, width=15).grid(
            row=9, column=0, pady=20)
        
        # Cancel task button
        ttk.Button(main_frame, text=self.get_text("cancel_task"), command=self.cancel_task, width=15).grid(
            row=9, column=1, pady=20)
        
        # Quick function title
        ttk.Label(main_frame, text=self.get_text("quick_options"), font=("Arial", 10, "underline"), foreground="blue").grid(
            row=10, column=0, columnspan=3, sticky=tk.W, pady=10)
        
        # Quick buttons - First row
        ttk.Button(main_frame, text="10" + self.get_text("minutes_later"), command=lambda: self.set_quick_task(10), width=10).grid(
            row=11, column=0, pady=5)
        ttk.Button(main_frame, text="30" + self.get_text("minutes_later"), command=lambda: self.set_quick_task(30), width=10).grid(
            row=11, column=1, pady=5)
        ttk.Button(main_frame, text="1" + self.get_text("minutes_later").replace("s", ""), command=lambda: self.set_quick_task(60), width=10).grid(
            row=11, column=2, pady=5)
        
        # Quick buttons - Second row
        ttk.Button(main_frame, text="2" + self.get_text("minutes_later").replace("s", ""), command=lambda: self.set_quick_task(120), width=10).grid(
            row=12, column=0, pady=5)
        ttk.Button(main_frame, text="4" + self.get_text("minutes_later").replace("s", ""), command=lambda: self.set_quick_task(240), width=10).grid(
            row=12, column=1, pady=5)
        ttk.Button(main_frame, text="8" + self.get_text("minutes_later").replace("s", ""), command=lambda: self.set_quick_task(480), width=10).grid(
            row=12, column=2, pady=5)
        
        # Quick buttons - Third row
        ttk.Button(main_frame, text=self.get_text("tomorrow_morning"), command=self.set_task_tomorrow_morning, width=15).grid(
            row=13, column=0, pady=5)
        ttk.Button(main_frame, text=self.get_text("tomorrow_eight"), command=self.set_task_tomorrow_eight, width=15).grid(
            row=13, column=1, pady=5)
        ttk.Button(main_frame, text=self.get_text("saturday_morning"), command=self.set_task_saturday_morning, width=15).grid(
            row=13, column=2, pady=5)
        
        # Developer information
        ttk.Label(main_frame, text=self.get_text("developer_info"), font=("Arial", 8)).grid(
            row=14, column=0, columnspan=3, pady=10)
    
    def change_language(self, event=None):
        """Change the language of the interface"""
        new_language = self.language_var.get()
        if new_language != self.current_language:
            self.current_language = new_language
            self.root.title(self.get_text("title"))
            self.update_ui_text()
    
    def update_ui_text(self):
        """Update all UI elements with the current language"""
        # Update dropdown values for date and time (essential for correct values)
        # Note: When state is "normal", setting values here only affects the dropdown list,
        # not the user's manual input if it's not in the list.
        self.year_combobox.config(values=self.generate_years())
        self.month_combobox.config(values=self.generate_months())
        self.update_days_dropdown() # Update days based on potentially new month/year labels
        self.hour_combobox.config(values=self.generate_hours())
        self.minute_combobox.config(values=self.generate_minutes())
        self.second_combobox.config(values=self.generate_seconds())


        # Get all widgets in the main frame
        main_frame = self.root.winfo_children()[0]
        for widget in main_frame.winfo_children():
            widget_type = widget.winfo_class()
            
            if widget_type == "TLabel":
                current_text = widget.cget("text")
                found_key = None
                for lang_dict in self.languages.values(): # Iterate through all language dictionaries
                    for k, v in lang_dict.items():
                        if current_text == v:
                            found_key = k
                            break
                    if found_key:
                        break

                if found_key:
                    widget.config(text=self.get_text(found_key))
                elif current_text == "Language:":
                    pass # Keep as is or add to language dictionary
                
            elif widget_type == "TRadiobutton":
                if widget.cget("value") == "shutdown":
                    widget.config(text=self.get_text("shutdown"))
                elif widget.cget("value") == "restart":
                    widget.config(text=self.get_text("restart"))
            
            elif widget_type == "TButton":
                current_text = widget.cget("text")
                if current_text.endswith(tuple([lang["set_task"] for lang in self.languages.values()])):
                    widget.config(text=self.get_text("set_task"))
                elif current_text.endswith(tuple([lang["cancel_task"] for lang in self.languages.values()])):
                    widget.config(text=self.get_text("cancel_task"))
                elif current_text.endswith(tuple([lang["quick_options"] for lang in self.languages.values()])):
                    widget.config(text=self.get_text("quick_options"))
                elif current_text.endswith(tuple([lang["tomorrow_morning"] for lang in self.languages.values()])):
                    widget.config(text=self.get_text("tomorrow_morning"))
                elif current_text.endswith(tuple([lang["tomorrow_eight"] for lang in self.languages.values()])): # New
                    widget.config(text=self.get_text("tomorrow_eight"))
                elif current_text.endswith(tuple([lang["saturday_morning"] for lang in self.languages.values()])): # New
                    widget.config(text=self.get_text("saturday_morning"))
                # Handle quick buttons with numbers dynamically
                elif any(text in current_text for text in ["10", "30", "1", "2", "4", "8"]):
                    digits = "".join(filter(str.isdigit, current_text))
                    if digits:
                        if digits == "1" or digits == "2" or digits == "4" or digits == "8":
                            widget.config(text=digits + self.get_text("minutes_later").replace("s", ""))
                        else:
                            widget.config(text=digits + self.get_text("minutes_later"))

        # Update status bar text
        self.status_var.set(self.get_text("no_task")) # Resetting to "no task" for simplicity on language change
            
    def set_task(self):
        """Set a shutdown/restart task"""
        try:
            # --- Start: Added pre-execution cancellation ---
            self.status_var.set(self.get_text("cancelling_existing")) # Show cancelling message
            self.root.update_idletasks() # Update UI immediately
            
            # Attempt to cancel any existing shutdown tasks
            if self.system == "Windows":
                # Use /a to abort pending shutdown/restart.
                # Use `check=False` to prevent error if no pending shutdown exists.
                subprocess.run(["shutdown", "/a"], check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif self.system in ["Linux", "Darwin"]:
                # Use `sudo shutdown -c` to cancel.
                # `check=False` for robust error handling if no task is scheduled.
                # `stdout` and `stderr` to suppress console output.
                subprocess.run(["sudo", "shutdown", "-c"], check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Reset task_time and task_type after cancellation attempt
            self.task_time = None
            self.task_type = None
            # --- End: Added pre-execution cancellation ---

            # Get user input for year, month, day, hour, minute, and second from comboboxes
            year_str = self.year_var.get()
            month_str = self.month_var.get()
            day_str = self.day_var.get()
            hour_str = self.hour_var.get()
            minute_str = self.minute_var.get()
            second_str = self.second_var.get()
            
            # Combine to form a full date-time string
            full_datetime_str = f"{year_str}-{month_str}-{day_str} {hour_str}:{minute_str}:{second_str}"

            # Parse date and time - this is where the validation happens
            task_datetime = datetime.datetime.strptime(full_datetime_str, "%Y-%m-%d %H:%M:%S")
            
            # Check if the date is in the past
            current_time = datetime.datetime.now()
            if task_datetime < current_time:
                messagebox.showerror(self.get_text("error"), self.get_text("time_in_past"))
                self.status_var.set(self.get_text("no_task")) # Reset status if error
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
                    minutes = int(seconds_until_task // 60)
                    if minutes == 0 and seconds_until_task > 0: # Ensure at least 1 minute if task is soon
                         minutes = 1
                    subprocess.run(["sudo", "shutdown", "-h", f"+{minutes}"], check=True)
                else:  # restart
                    minutes = int(seconds_until_task // 60)
                    if minutes == 0 and seconds_until_task > 0:
                         minutes = 1
                    subprocess.run(["sudo", "shutdown", "-r", f"+{minutes}"], check=True)
            
            # Update status
            self.task_time = task_datetime
            time_display = task_datetime.strftime("%Y-%m-%d %H:%M:%S")
            self.status_var.set(f"{self.get_text('system_will')}{time_display}{self.get_text('at')}{operation_text}")
            
            messagebox.showinfo(self.get_text("success"), f"{self.get_text('task_set')}{time_display}{self.get_text('at')}{operation_text}")
            
        except ValueError as e:
            # This will catch errors from datetime.strptime if the input is invalid
            messagebox.showerror(self.get_text("format_error"), f"{self.get_text('format_error')}: {e}\n{full_datetime_str}")
            self.status_var.set(self.get_text("no_task")) # Reset status if error
        except subprocess.CalledProcessError as e:
            messagebox.showerror(self.get_text("command_failed"), f"{self.get_text('command_failed')}: {e}\n检查权限或命令是否存在。")
            self.status_var.set(self.get_text("no_task")) # Reset status if error
        except Exception as e:
            messagebox.showerror(self.get_text("unknown_error"), f"{self.get_text('unknown_error')}: {e}")
            self.status_var.set(self.get_text("no_task")) # Reset status if error
    
    def cancel_task(self):
        """Cancel the scheduled task"""
        try:
            if self.task_time is None and self.system == "Windows":
                # For Windows, we can't easily check if a task is "active" without parsing `shutdown /query`
                # So, we'll just attempt to cancel. If it fails, it means no task was there.
                # For other OS, we rely on the task_time being set by our app.
                pass
            elif self.task_time is None: # For Linux/macOS, if task_time is None, we assume no task was set by us.
                messagebox.showinfo(self.get_text("info"), self.get_text("no_task_to_cancel"))
                return
            
            # Execute cancel command based on system
            if self.system == "Windows":
                # Use `check=False` to prevent error if no pending shutdown exists.
                result = subprocess.run(["shutdown", "/a"], check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                # Check if cancellation was truly effective (e.g., "There are no pending system shutdowns")
                if "no pending system shutdowns" in result.stderr.lower() or "no pending system shutdowns" in result.stdout.lower():
                    if self.task_time is None: # Only show "no task to cancel" if we didn't think there was one
                        messagebox.showinfo(self.get_text("info"), self.get_text("no_task_to_cancel"))
                        return
            elif self.system in ["Linux", "Darwin"]:
                subprocess.run(["sudo", "shutdown", "-c"], check=True) # Needs sudo on Linux/macOS
            
            # Update status
            self.task_time = None
            self.task_type = None
            self.status_var.set(self.get_text("no_task"))
            
            messagebox.showinfo(self.get_text("success"), self.get_text("task_canceled"))
            
        except subprocess.CalledProcessError as e:
            messagebox.showerror(self.get_text("command_failed"), f"{self.get_text('command_failed')}: {e}\n检查权限或命令是否存在。")
        except Exception as e:
            messagebox.showerror(self.get_text("unknown_error"), f"{self.get_text('unknown_error')}: {e}")
    
    def set_quick_task(self, minutes):
        """Set a quick task with specified minutes"""
        # Calculate task time
        current_time = datetime.datetime.now()
        task_datetime = current_time + datetime.timedelta(minutes=minutes)
        
        # Update date and time inputs (comboboxes)
        self.year_var.set(task_datetime.strftime("%Y"))
        self.month_var.set(task_datetime.strftime("%m"))
        self.day_var.set(task_datetime.strftime("%d"))
        self.hour_var.set(task_datetime.strftime("%H"))
        self.minute_var.set(task_datetime.strftime("%M"))
        self.second_var.set(task_datetime.strftime("%S")) # Set seconds as well
        
        # Set the task (this will now include the pre-cancellation logic)
        self.set_task()
    
    def set_task_tomorrow_morning(self):
        """Set a task for 7:30 tomorrow morning"""
        # Get current date
        today = datetime.date.today()
        # Calculate tomorrow's date
        tomorrow = today + datetime.timedelta(days=1)
        # Set time to 7:30:00
        task_datetime = datetime.datetime.combine(tomorrow, datetime.time(7, 30, 0))
        
        # If current time is already past 7:30 today, calculate 7:30 the day after tomorrow
        current_time = datetime.datetime.now()
        if current_time > task_datetime:
            task_datetime += datetime.timedelta(days=1)
        
        # Update date and time inputs (comboboxes)
        self.year_var.set(task_datetime.strftime("%Y"))
        self.month_var.set(task_datetime.strftime("%m"))
        self.day_var.set(task_datetime.strftime("%d"))
        self.hour_var.set(task_datetime.strftime("%H"))
        self.minute_var.set(task_datetime.strftime("%M"))
        self.second_var.set(task_datetime.strftime("%S")) # Set seconds as well
        
        # Set the task (this will now include the pre-cancellation logic)
        self.set_task()

    def set_task_tomorrow_eight(self):
        """Set a task for 8:00 tomorrow morning"""
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        task_datetime = datetime.datetime.combine(tomorrow, datetime.time(8, 0, 0))

        current_time = datetime.datetime.now()
        if current_time > task_datetime:
            task_datetime += datetime.timedelta(days=1)

        self.year_var.set(task_datetime.strftime("%Y"))
        self.month_var.set(task_datetime.strftime("%m"))
        self.day_var.set(task_datetime.strftime("%d"))
        self.hour_var.set(task_datetime.strftime("%H"))
        self.minute_var.set(task_datetime.strftime("%M"))
        self.second_var.set(task_datetime.strftime("%S"))
        
        # Set the task (this will now include the pre-cancellation logic)
        self.set_task()

    def set_task_saturday_morning(self):
        """Set a task for 7:30 on the next Saturday"""
        today = datetime.date.today()
        # weekday() returns 0 for Monday, 6 for Sunday
        # Saturday is 5
        days_until_saturday = (5 - today.weekday() + 7) % 7
        if days_until_saturday == 0: # If today is Saturday, set for next Saturday
            days_until_saturday = 7
            
        next_saturday = today + datetime.timedelta(days=days_until_saturday)
        task_datetime = datetime.datetime.combine(next_saturday, datetime.time(7, 30, 0))

        current_time = datetime.datetime.now()
        # If the calculated Saturday 7:30 is in the past (e.g., if it's Saturday afternoon), set for the Saturday after
        if current_time > task_datetime:
            task_datetime += datetime.timedelta(weeks=1)

        self.year_var.set(task_datetime.strftime("%Y"))
        self.month_var.set(task_datetime.strftime("%m"))
        self.day_var.set(task_datetime.strftime("%d"))
        self.hour_var.set(task_datetime.strftime("%H"))
        self.minute_var.set(task_datetime.strftime("%M"))
        self.second_var.set(task_datetime.strftime("%S"))
        
        # Set the task (this will now include the pre-cancellation logic)
        self.set_task()

if __name__ == "__main__":
    root = tk.Tk()
    app = ShutdownScheduler(root)

    root.mainloop()
