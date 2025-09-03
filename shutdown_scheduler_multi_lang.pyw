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




import ttkbootstrap as ttk
from tkinter import messagebox
import datetime
import threading
import subprocess
import platform
import os
import functools
import json

# QR code string for donation (unchanged)
qr_code_string = """

    ███████   █ ██ █ █ ██  ██ ███████    
    █     █ █ █  ███  █ █ █ █ █     █    
    █ ███ █     ██ █  ██████  █ ███ █    
    █ ███ █ ███ █ █ ███ █ ███ █ ███ █
    █ ███ █  █         █ ███  █ ███ █
    █     █ ██ ██  █ █        █     █
    ███████ █ █ █ █ █ █ █ █ █ ███████
             ███  █      ████
    █████ ████ █   █ █ ██ █ ██ █ █ █
     ██ █  ██ █ ███ ██ █   █ ██   ███
    █ █  ███  █  ██████ █   ██ ███ █
    █ ████  █   ██ █  █ ██ █ ██ █ █
    ██   ██ ███ █ █ ██ █  ████ ███
    █  ██  █ █      █ ███████ ██   ██
      █  ██ █  ██  ███  ███  █ █   █
    █ ████ █ █ █  █      █  ██ █  █
    █ █████   ██     ████  █ █  █  █
     ████  ███  █████   █  █  █  █ ██
    █   ███   █  ███      █    █ █ █
    █ ███    ██ ██ █  █████ ████  █
     ██  ███    █ ████  █ █ ██  █  █
    ██ █ █         ██ ██ ███  █  █ ██
    █ ██  █ █ ███  ██    █  █ █  █ █
    █ ███  █ █ █  █ █ █  ██ █  █ ██
    █ ██  █  █ █   ██  █  █ ██████  █
            █ █ ███  █  █████   █ █ █
    ███████ ██   █████  █  ██ █ █ ██
    █     █  █  ██ █     █ ██   █████
    █ ███ █ █   █ █ ██  █   █████   █
    █ ███ █ ███    ██   █   ██ ██ ███
    █ ███ █ █  ██  █    █ ███ █  ██
    █     █ ████  ███    ███     ██
    ███████ ████     █   █████ ███ █
"""

class ConfigManager:
    """管理配置文件的加载和保存。"""
    def __init__(self, filename="config.json"):
        self.filename = filename
        self.default_config = {
            "default_language": "中文",
            "default_operation": "restart",
            "default_timer_minutes": 30
        }

    def load_config(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                config = json.load(f)
                # 确保所有键都存在
                for key, default_value in self.default_config.items():
                    if key not in config or not isinstance(config[key], type(default_value)):
                        print(f"Warning: '{key}' not found or has invalid type. Using default.")
                        config[key] = default_value
                return config
        except (FileNotFoundError, json.JSONDecodeError):
            print("Warning: config.json not found or is invalid. Using default configuration.")
            return self.default_config

    def save_config(self, config):
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(config, f, indent=4)
        except Exception as e:
            print(f"Error saving config file: {e}")


class LocalizationManager:
    """管理多语言文本数据。"""
    def __init__(self):
        self.languages = self._load_languages()

    def _load_languages(self):
        return {
            "English": {
                "title": "Shutdown/Restart Scheduler",
                "operation_type": "Operation Type",
                "specific_time": "Set Specific Time",
                "shutdown": "Shutdown",
                "restart": "Restart",
                "year": "Year:",
                "month": "Month:",
                "day": "Day:",
                "hour": "Hour:",
                "minute": "Minute:",
                "second": "Second:",
                "status": "Current Status:",
                "info": "Information:",
                "custom_timer": "Custom Timer",
                "custom_days": "Days:",
                "custom_hours": "Hours:",
                "custom_minutes": "Minutes:",
                "set_timer": "Set Timer",
                "no_task": "No task scheduled",
                "set_task": "Set Task",
                "cancel_task": "Cancel Task",
                "quick_options": "Quick Options",
                "minutes_later": " Mins Later",
                "tomorrow_750": "Tomorrow 7:50",
                "tomorrow_800": "Tomorrow 8:00",
                "today_750": "Today 7:50",
                "developer_info": "© Copyright Xiangming Zhou; E-mail:zhouxmmail@163.com",
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
                "cancelling_existing": "Cancelling existing task...",
                "invalid_timer_value": "Please enter a valid positive number for days, hours, and minutes.",
                "donate_button": "Donate",
                "donate_title": "Thank you for your donation!",
                "donate_note": qr_code_string,
                "donate_text_addition": "If you are satisfied with my work, you are welcome to donate via WeChat Pay.",
                "run_as_admin_note": "Please run the program with administrator privileges.",
                "monday_800": "Monday 8:00",
                "tuesday_800": "Tuesday 8:00",
                "wednesday_800": "Wednesday 8:00",
                "thursday_800": "Thursday 8:00",
                "friday_800": "Friday 8:00",
                "saturday_750": "Saturday 7:50",
                "saturday_800": "Saturday 8:00",
                "sunday_800": "Sunday 8:00",
            },
            "中文": {
                "title": "定时关机/重启程序",
                "operation_type": "操作类型",
                "specific_time": "设定具体时间",
                "shutdown": "关机",
                "restart": "重启",
                "year": "年:",
                "month": "月:",
                "day": "日:",
                "hour": "时:",
                "minute": "分:",
                "second": "秒:",
                "status": "当前状态:",
                "info": "信息:",
                "custom_timer": "自定义倒计时",
                "custom_days": "天:",
                "custom_hours": "小时:",
                "custom_minutes": "分钟:",
                "set_timer": "设置定时任务",
                "no_task": "未设置任务",
                "set_task": "设置任务",
                "cancel_task": "取消任务",
                "quick_options": "快捷选项",
                "minutes_later": "分钟后",
                "tomorrow_750": "明日 7:50",
                "tomorrow_800": "明日 8:00",
                "today_750": "今日 7:50",
                "developer_info": "© Copyright Xiangming Zhou; E-mail:zhouxmmail@163.com",
                "success": "成功",
                "error": "错误",
                "format_error": "格式错误",
                "command_failed": "命令执行失败",
                "unknown_error": "发生未知错误",
                "time_in_past": "设置的时间不能早于当前时间!",
                "no_task_to_cancel": "没有任务需要取消",
                "task_canceled": "已取消任务",
                "system_will": "系统将于 ",
                "at": " ",
                "shutdown_text": "关机",
                "restart_text": "重启",
                "task_set": "已设置系统在 ",
                "cancelling_existing": "正在取消现有任务...",
                "invalid_timer_value": "请输入有效的天、小时和分钟值，且不能为负数。",
                "donate_button": "捐助作者",
                "donate_title": "感谢您的捐助",
                "donate_note": qr_code_string,
                "donate_text_addition": "如果您对我的作品感到满意，欢迎通过微信支付进行捐赠。",
                "run_as_admin_note": "请确保以管理员权限运行程序。",
                "monday_800": "周一 8:00",
                "tuesday_800": "周二 8:00",
                "wednesday_800": "周三 8:00",
                "thursday_800": "周四 8:00",
                "friday_800": "周五 8:00",
                "saturday_750": "周六 7:50",
                "saturday_800": "周六 8:00",
                "sunday_800": "周日 8:00",
            },
            "Français": {
                "title": "Planificateur d'arrêt/redémarrage",
                "operation_type": "Type d'opération",
                "specific_time": "Définir l'heure spécifique",
                "shutdown": "Arrêt",
                "restart": "Redémarrage",
                "year": "Année:",
                "month": "Mois:",
                "day": "Jour:",
                "hour": "Heure:",
                "minute": "Minute:",
                "second": "Seconde:",
                "status": "État actuel:",
                "info": "Information:",
                "custom_timer": "Minuterie personnalisée",
                "custom_days": "Jours:",
                "custom_hours": "Heures:",
                "custom_minutes": "Minutes:",
                "set_timer": "Démarrer la minuterie",
                "no_task": "Aucune tâche planifiée",
                "set_task": "Planifier la tâche",
                "cancel_task": "Annuler la tâche",
                "quick_options": "Options rapides",
                "minutes_later": " minutes plus tard",
                "tomorrow_750": "Demain 7:50",
                "tomorrow_800": "Demain 8:00",
                "saturday_750": "Samedi 7:50",
                "saturday_800": "Samedi 8:00",
                "today_750": "Aujourd'hui 7:50",
                "developer_info": "© Copyright Xiangming Zhou; E-mail:zhouxmmail@163.com",
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
                "cancelling_existing": "Annulation de la tâche existante...",
                "invalid_timer_value": "Veuillez entrer une valeur positive valide pour les jours, les heures et les minutes。",
                "donate_button": "Faire un don",
                "donate_title": "Merci pour votre don !",
                "donate_note": qr_code_string,
                "donate_text_addition": "Si vous êtes satisfait de mon travail, vous pouvez faire un don via WeChat Pay。",
                "run_as_admin_note": "Veuillez exécuter le programme avec des privilèges d'administrateur.",
                "monday_800": "Lundi 8:00",
                "tuesday_800": "Mardi 8:00",
                "wednesday_800": "Mercredi 8:00",
                "thursday_800": "Jeudi 8:00",
                "friday_800": "Vendredi 8:00",
                "saturday_800": "Samedi 8:00",
                "saturday_750": "Samedi 7:50",
                "sunday_800": "Dimanche 8:00",
            },
            "日本語": {
                "title": "シャットダウン/再起動スケジューラ",
                "operation_type": "操作タイプ",
                "specific_time": "特定の時間を設定",
                "shutdown": "シャットダウン",
                "restart": "再起動",
                "year": "年:",
                "month": "月:",
                "day": "日:",
                "hour": "時:",
                "minute": "分:",
                "second": "秒:",
                "status": "現在の状態:",
                "info": "情報:",
                "custom_timer": "カスタムタイマー",
                "custom_days": "日:",
                "custom_hours": "時間:",
                "custom_minutes": "分:",
                "set_timer": "タイマー設定",
                "no_task": "タスク未設定",
                "set_task": "タスク設定",
                "cancel_task": "タスク取消",
                "quick_options": "クイックオプション",
                "minutes_later": "分後",
                "tomorrow_750": "明日の7:50",
                "tomorrow_800": "明日の8:00",
                "saturday_750": "土曜日の7:50",
                "saturday_800": "土曜日の8:00",
                "today_750": "今日の7:50",
                "developer_info": "© Copyright Xiangming Zhou; E-mail:zhouxmmail@163.com",
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
                "cancelling_existing": "既存のタスクをキャンセル中...",
                "invalid_timer_value": "日数、時間、分の有効な正の値を入力してください。",
                "donate_button": "寄付",
                "donate_title": "ご寄付ありがとうございます！",
                "donate_note": qr_code_string,
                "donate_text_addition": "私の作品にご満足いただけましたら、WeChat Payでご寄付いただけます。",
                "run_as_admin_note": "管理者権限でプログラムを実行してください。",
                "monday_800": "月曜日の8:00",
                "tuesday_800": "火曜日の8:00",
                "wednesday_800": "水曜日の8:00",
                "thursday_800": "木曜日の8:00",
                "friday_800": "金曜日の8:00",
                "saturday_800": "土曜日の8:00",
                "saturday_750": "土曜日の7:50",
                "sunday_800": "日曜日の8:00",
            },
        }

    def get_text(self, language, key):
        return self.languages.get(language, {}).get(key, key)


class SystemExecutor:
    """
    负责执行与操作系统相关的关机/重启命令。
    符合职责单一原则，将系统命令逻辑与GUI逻辑分离。
    """
    def __init__(self, system):
        self.system = system

    def _run_command_in_thread(self, command_args, on_success, on_error):
        """异步执行命令以避免GUI卡顿。"""
        def run_cmd():
            try:
                startupinfo = None
                if self.system == "Windows":
                    startupinfo = subprocess.STARTUPINFO()
                    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                    startupinfo.wShowWindow = subprocess.SW_HIDE
                
                process = subprocess.Popen(
                    command_args,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    startupinfo=startupinfo,
                )
                stdout, stderr = process.communicate()
                
                if process.returncode == 0:
                    on_success(stdout.strip())
                else:
                    error_msg = stderr.strip() if stderr else f"Exit code: {process.returncode}"
                    on_error(error_msg)
            except Exception as e:
                on_error(str(e))

        thread = threading.Thread(target=run_cmd)
        thread.daemon = True
        thread.start()

    def set_task(self, seconds, op_type, on_success, on_error):
        """设置关机或重启任务。"""
        command = []
        if self.system == "Windows":
            op_flag = "/s" if op_type == "shutdown" else "/r"
            command = ["shutdown", op_flag, "/t", str(int(seconds))]
        elif self.system in ["Linux", "Darwin"]:
            minutes = max(1, round(seconds / 60))
            op_flag = "-h" if op_type == "shutdown" else "-r"
            command = ["sudo", "shutdown", op_flag, f"+{minutes}"]
        self._run_command_in_thread(command, on_success, on_error)

    def cancel_task(self, on_success, on_error):
        """取消现有任务。"""
        command = ["shutdown", "/a"] if self.system == "Windows" else ["sudo", "shutdown", "-c"]
        self._run_command_in_thread(command, on_success, on_error)


class SchedulerModel:
    """模型层：管理应用程序状态。"""
    def __init__(self, config):
        self.config = config
        self.current_language = config["default_language"]
        self.task_time = None
        self.task_type = None

    def set_task(self, task_time, task_type):
        self.task_time = task_time
        self.task_type = task_type

    def clear_task(self):
        self.task_time = None
        self.task_type = None


class DateTimeUtils:
    """处理日期和时间相关的工具类。"""
    @staticmethod
    def generate_years():
        current_year = datetime.date.today().year
        return [str(year) for year in range(current_year, current_year + 11)]

    @staticmethod
    def generate_months():
        return [f"{m:02d}" for m in range(1, 13)]

    @staticmethod
    def generate_days(year, month):
        try:
            year, month = int(year), int(month)
            if month == 2:
                num_days = 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
            elif month in [4, 6, 9, 11]:
                num_days = 30
            else:
                num_days = 31
            return [f"{d:02d}" for d in range(1, num_days + 1)]
        except (ValueError, TypeError):
            return [f"{d:02d}" for d in range(1, 32)]

    @staticmethod
    def generate_hours(): return [f"{h:02d}" for h in range(24)]

    @staticmethod
    def generate_minutes(): return [f"{m:02d}" for m in range(60)]

    @staticmethod
    def generate_seconds(): return [f"{s:02d}" for s in range(60)]

    @staticmethod
    def get_weekday_task_time(weekday, hour, minute):
        today = datetime.date.today()
        # weekday() returns 0 for Monday, 6 for Sunday
        days_ahead = (weekday - today.weekday() + 7) % 7
        
        target_time = datetime.time(hour, minute)
        if days_ahead == 0 and datetime.datetime.now().time() > target_time:
            days_ahead = 7
        
        target_date = today + datetime.timedelta(days=days_ahead)
        return datetime.datetime.combine(target_date, target_time)


class DonateView:
    """视图层：专门处理捐赠弹窗。"""
    def __init__(self, parent, localization_manager, current_language):
        self.parent = parent
        self.localization = localization_manager
        self.current_language = current_language

    def show(self):
        donate_window = ttk.Toplevel(self.parent)
        donate_window.title(self.localization.get_text(self.current_language, "donate_title"))
        donate_window.geometry("400x450")
        donate_window.resizable(False, False)
        frame = ttk.Frame(donate_window, padding="10")
        frame.pack(fill=ttk.BOTH, expand=True)
        
        ttk.Label(frame, text=self.localization.get_text(self.current_language, "donate_text_addition"), wraplength=380, justify=ttk.CENTER).pack(pady=(0, 10))
        ttk.Label(frame, text=qr_code_string, font=("Courier New", 6), justify=ttk.LEFT).pack(pady=10)


class SchedulerView:
    """视图层：构建和管理主GUI界面。"""
    def __init__(self, root, localization_manager, model):
        self.root = root
        self.localization = localization_manager
        self.model = model
        self.language_var = ttk.StringVar(value=self.model.current_language)
        self.operation_var = ttk.StringVar(value=self.model.config["default_operation"])
        self.year_var = ttk.StringVar()
        self.month_var = ttk.StringVar()
        self.day_var = ttk.StringVar()
        self.hour_var = ttk.StringVar()
        self.minute_var = ttk.StringVar()
        self.second_var = ttk.StringVar()
        self.custom_timer_days_var = ttk.StringVar(value="0")
        self.custom_timer_hours_var = ttk.StringVar(value="0")
        self.custom_timer_minutes_var = ttk.StringVar(value=str(self.model.config["default_timer_minutes"]))
        self.status_var = ttk.StringVar()
        self.info_var = ttk.StringVar()
        self.quick_buttons = {}
        self.callbacks = {}

        self._create_widgets()
        self.update_ui_text()
        self.update_status_display()

    def set_callbacks(self, callbacks):
        self.callbacks = callbacks
        self.language_combo.bind("<<ComboboxSelected>>", self.callbacks.get("on_language_change"))
        self.set_task_btn.config(command=self.callbacks.get("on_set_task"))
        self.cancel_task_btn.config(command=self.callbacks.get("on_cancel_task"))
        self.set_timer_btn.config(command=self.callbacks.get("on_set_custom_timer"))
        self.donate_btn.config(command=self.callbacks.get("on_show_donate"))

        for key, btn in self.quick_buttons.items():
            if key.isdigit():
                cmd = lambda minutes=int(key): self.callbacks.get("on_set_quick_task")(minutes)
            else:
                cmd = self.callbacks.get(f"on_set_{key}")
            if cmd:
                btn.config(command=cmd)
        
    def _create_widgets(self):
        self.root.geometry("680x560")
        self.root.resizable(False, False)

        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=ttk.BOTH, expand=True)
        main_frame.columnconfigure(0, weight=1, uniform="group1")
        main_frame.columnconfigure(1, weight=1, uniform="group1")

        self._create_language_selection(main_frame)
        self.left_frame = ttk.Frame(main_frame)
        self.left_frame.grid(row=1, column=0, sticky="nsew", padx=(0, 5))
        self.right_frame = ttk.Frame(main_frame)
        self.right_frame.grid(row=1, column=1, sticky="nsew", padx=(5, 0))

        self.options_frame = self._create_operation_type_selection(self.left_frame)
        self.options_frame.pack(fill=ttk.X, expand=True, pady=(0, 10))
        self.custom_timer_frame = self._create_custom_timer_options(self.left_frame)
        self.custom_timer_frame.pack(fill=ttk.X, expand=True)
        self.quick_options_frame = self._create_quick_options(self.right_frame)
        self.quick_options_frame.pack(fill=ttk.BOTH, expand=True)

        self._create_status_display(main_frame)
        self._create_action_buttons(main_frame)
        self._create_info_bar(main_frame)
        self._create_developer_info(main_frame)

    # UI创建方法（简化）...
    def _create_language_selection(self, parent):
        lang_frame = ttk.Frame(parent)
        lang_frame.grid(row=0, column=0, columnspan=2, sticky="e", pady=(0, 10))
        ttk.Label(lang_frame, text="Language:").pack(side=ttk.LEFT, padx=(0, 5))
        self.language_combo = ttk.Combobox(
            lang_frame, textvariable=self.language_var,
            values=list(self.localization.languages.keys()), state="readonly", width=10
        )
        self.language_combo.pack(side=ttk.LEFT)

    def _create_operation_type_selection(self, parent):
        options_frame = ttk.LabelFrame(parent, padding="10")
        radio_frame = ttk.Frame(options_frame)
        radio_frame.pack(fill=ttk.X, pady=(0, 10))
        self.shutdown_radio = ttk.Radiobutton(
            radio_frame, variable=self.operation_var, value="shutdown", bootstyle="info-round-toggle"
        )
        self.shutdown_radio.pack(side=ttk.LEFT, padx=5, expand=True)
        self.restart_radio = ttk.Radiobutton(
            radio_frame, variable=self.operation_var, value="restart", bootstyle="info-round-toggle"
        )
        self.restart_radio.pack(side=ttk.LEFT, padx=5, expand=True)
        self.specific_time_frame = ttk.LabelFrame(options_frame, padding="10")
        self.specific_time_frame.pack(fill=ttk.X)
        self._create_date_time_selection(self.specific_time_frame)
        return options_frame

    def _create_date_time_selection(self, parent):
        now = datetime.datetime.now()
        self.year_var.set(str(now.year))
        self.month_var.set(f"{now.month:02d}")
        self.day_var.set(f"{now.day:02d}")
        self.hour_var.set(f"{now.hour:02d}")
        self.minute_var.set(f"{now.minute:02d}")
        self.second_var.set(f"{now.second:02d}")
        parent.columnconfigure((0, 1, 2), weight=1)
        self.year_combobox, self.year_label = self._create_labeled_combobox(parent, "year", self.year_var, DateTimeUtils.generate_years())
        self.year_combobox.master.grid(row=0, column=0, sticky='ew', padx=2, pady=2)
        self.month_combobox, self.month_label = self._create_labeled_combobox(parent, "month", self.month_var, DateTimeUtils.generate_months())
        self.month_combobox.master.grid(row=0, column=1, sticky='ew', padx=2, pady=2)
        self.day_combobox, self.day_label = self._create_labeled_combobox(parent, "day", self.day_var, DateTimeUtils.generate_days(now.year, now.month))
        self.day_combobox.master.grid(row=0, column=2, sticky='ew', padx=2, pady=2)
        self.hour_combobox, self.hour_label = self._create_labeled_combobox(parent, "hour", self.hour_var, DateTimeUtils.generate_hours())
        self.hour_combobox.master.grid(row=1, column=0, sticky='ew', padx=2, pady=2)
        self.minute_combobox, self.minute_label = self._create_labeled_combobox(parent, "minute", self.minute_var, DateTimeUtils.generate_minutes())
        self.minute_combobox.master.grid(row=1, column=1, sticky='ew', padx=2, pady=2)
        self.second_combobox, self.second_label = self._create_labeled_combobox(parent, "second", self.second_var, DateTimeUtils.generate_seconds())
        self.second_combobox.master.grid(row=1, column=2, sticky='ew', padx=2, pady=2)
    
    def _create_labeled_combobox(self, parent, label_key, var, values):
        frame = ttk.Frame(parent)
        label = ttk.Label(frame, text=self.localization.get_text(self.model.current_language, label_key))
        label.pack(side=ttk.LEFT, padx=(0, 5))
        combobox = ttk.Combobox(frame, textvariable=var, values=values, state="readonly", width=5)
        combobox.pack(side=ttk.LEFT, fill=ttk.X, expand=True)
        return combobox, label

    def _create_custom_timer_options(self, parent):
        custom_timer_frame = ttk.LabelFrame(parent, padding="10")
        timer_input_frame = ttk.Frame(custom_timer_frame)
        timer_input_frame.pack(fill=ttk.X, pady=5)
        timer_input_frame.columnconfigure((0, 1, 2), weight=1)
        days_frame = ttk.Frame(timer_input_frame)
        days_frame.grid(row=0, column=0, sticky='ew', padx=2)
        self.days_label = ttk.Label(days_frame)
        self.days_label.pack(side=ttk.LEFT)
        self.days_spinbox = ttk.Spinbox(days_frame, from_=0, to=999, textvariable=self.custom_timer_days_var, width=4)
        self.days_spinbox.pack(side=ttk.LEFT, fill=ttk.X, expand=True)
        hours_frame = ttk.Frame(timer_input_frame)
        hours_frame.grid(row=0, column=1, sticky='ew', padx=2)
        self.hours_label = ttk.Label(hours_frame)
        self.hours_label.pack(side=ttk.LEFT)
        self.hours_spinbox = ttk.Spinbox(hours_frame, from_=0, to=23, textvariable=self.custom_timer_hours_var, width=4)
        self.hours_spinbox.pack(side=ttk.LEFT, fill=ttk.X, expand=True)
        minutes_frame = ttk.Frame(timer_input_frame)
        minutes_frame.grid(row=0, column=2, sticky='ew', padx=2)
        self.minutes_label = ttk.Label(minutes_frame)
        self.minutes_label.pack(side=ttk.LEFT)
        self.minutes_spinbox = ttk.Spinbox(minutes_frame, from_=0, to=59, textvariable=self.custom_timer_minutes_var, width=4)
        self.minutes_spinbox.pack(side=ttk.LEFT, fill=ttk.X, expand=True)
        self.set_timer_btn = ttk.Button(custom_timer_frame, bootstyle="info")
        self.set_timer_btn.pack(fill=ttk.X, pady=5)
        return custom_timer_frame

    def _create_quick_options(self, parent):
        quick_options_frame = ttk.LabelFrame(parent, padding="10")
        button_configs = [
            ("30", "secondary"), ("60", "secondary"),
            ("today_750", "secondary"), ("tomorrow_750", "secondary"), ("tomorrow_800", "secondary"),
            ("saturday_750", "secondary"), ("saturday_800", "secondary"),
            ("monday_800", "secondary"), ("tuesday_800", "secondary"), ("wednesday_800", "secondary"),
            ("thursday_800", "secondary"), ("friday_800", "secondary"), ("sunday_800", "secondary"),
        ]
        for i, (key, style) in enumerate(button_configs):
            row, col = divmod(i, 2)
            btn = ttk.Button(quick_options_frame, bootstyle=style)
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            self.quick_buttons[key] = btn
        quick_options_frame.grid_columnconfigure((0, 1), weight=1)
        return quick_options_frame
    
    def _create_status_display(self, parent):
        status_frame = ttk.Frame(parent)
        status_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=10)
        self.status_title_label = ttk.Label(status_frame, font="-weight bold")
        self.status_title_label.pack(side=ttk.LEFT)
        self.status_label = ttk.Label(status_frame, textvariable=self.status_var, bootstyle="info")
        self.status_label.pack(side=ttk.LEFT, padx=10)
    
    def _create_action_buttons(self, parent):
        button_frame = ttk.Frame(parent)
        button_frame.grid(row=3, column=0, columnspan=2, sticky="ew", pady=5)
        button_frame.columnconfigure((0, 1), weight=1)
        self.set_task_btn = ttk.Button(button_frame, bootstyle="success")
        self.set_task_btn.grid(row=0, column=0, sticky="ew", padx=5)
        self.cancel_task_btn = ttk.Button(button_frame, bootstyle="danger")
        self.cancel_task_btn.grid(row=0, column=1, sticky="ew", padx=5)

    def _create_info_bar(self, parent):
        info_frame = ttk.Frame(parent)
        info_frame.grid(row=4, column=0, columnspan=2, sticky="ew", pady=5)
        self.info_title_label = ttk.Label(info_frame, font="-weight bold")
        self.info_title_label.pack(side=ttk.LEFT)
        self.info_label = ttk.Label(info_frame, textvariable=self.info_var, wraplength=550)
        self.info_label.pack(side=ttk.LEFT, padx=10)

    def _create_developer_info(self, parent):
        info_frame = ttk.Frame(parent)
        info_frame.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(10, 0))
        self.donate_btn = ttk.Button(info_frame)
        self.donate_btn.pack(side=ttk.LEFT, padx=(0, 10))
        self.developer_info_label = ttk.Label(info_frame, font="-size 9")
        self.developer_info_label.pack(side=ttk.LEFT)

    def update_ui_text(self):
        """更新所有UI文本。"""
        lang = self.model.current_language
        self.root.title(self.localization.get_text(lang, "title"))
        self.options_frame.config(text=self.localization.get_text(lang, "operation_type"))
        self.specific_time_frame.config(text=self.localization.get_text(lang, "specific_time"))
        self.custom_timer_frame.config(text=self.localization.get_text(lang, "custom_timer"))
        self.quick_options_frame.config(text=self.localization.get_text(lang, "quick_options"))
        self.shutdown_radio.config(text=self.localization.get_text(lang, "shutdown"))
        self.restart_radio.config(text=self.localization.get_text(lang, "restart"))
        self.year_label.config(text=self.localization.get_text(lang, "year"))
        self.month_label.config(text=self.localization.get_text(lang, "month"))
        self.day_label.config(text=self.localization.get_text(lang, "day"))
        self.hour_label.config(text=self.localization.get_text(lang, "hour"))
        self.minute_label.config(text=self.localization.get_text(lang, "minute"))
        self.second_label.config(text=self.localization.get_text(lang, "second"))
        self.days_label.config(text=self.localization.get_text(lang, "custom_days"))
        self.hours_label.config(text=self.localization.get_text(lang, "custom_hours"))
        self.minutes_label.config(text=self.localization.get_text(lang, "custom_minutes"))
        self.set_timer_btn.config(text=self.localization.get_text(lang, "set_timer"))
        self.quick_buttons["30"].config(text="30" + self.localization.get_text(lang, "minutes_later"))
        self.quick_buttons["60"].config(text="60" + self.localization.get_text(lang, "minutes_later"))
        for key in ["today_750", "tomorrow_750", "tomorrow_800", "monday_800", "tuesday_800", "wednesday_800", "thursday_800", "friday_800", "saturday_750", "saturday_800", "sunday_800"]:
            self.quick_buttons[key].config(text=self.localization.get_text(lang, key))
        self.status_title_label.config(text=self.localization.get_text(lang, "status"))
        self.info_title_label.config(text=self.localization.get_text(lang, "info"))
        self.set_task_btn.config(text=self.localization.get_text(lang, "set_task"))
        self.cancel_task_btn.config(text=self.localization.get_text(lang, "cancel_task"))
        self.developer_info_label.config(text=self.localization.get_text(lang, "developer_info"))
        self.donate_btn.config(text=self.localization.get_text(lang, "donate_button"))
        self.info_var.set("")
        self.update_status_display()

    def update_status_display(self):
        lang = self.model.current_language
        if self.model.task_time and self.model.task_type:
            time_display = self.model.task_time.strftime("%Y-%m-%d %H:%M:%S")
            op_text = self.localization.get_text(lang, "shutdown_text") if self.model.task_type == "shutdown" else self.localization.get_text(lang, "restart_text")
            status_text = f"{self.localization.get_text(lang, 'system_will')}{time_display}{self.localization.get_text(lang, 'at')}{op_text}"
            self.status_var.set(status_text)
        else:
            self.status_var.set(self.localization.get_text(lang, "no_task"))

    def update_info_bar(self, message, is_success=True):
        self.info_var.set(message)
        bootstyle = "success" if is_success else "danger"
        self.info_label.config(bootstyle=bootstyle)


class TaskScheduler:
    """业务逻辑层：处理任务调度核心逻辑。"""
    def __init__(self, model, system_executor, localization_manager, view):
        self.model = model
        self.system_executor = system_executor
        self.localization = localization_manager
        self.view = view

    def set_task(self, task_datetime_provider):
        self.view.update_info_bar(self.localization.get_text(self.model.current_language, "cancelling_existing"), is_success=True)
        self.view.root.update_idletasks()

        def on_cancel_success(output):
            try:
                task_datetime = task_datetime_provider()
                self._execute_task_setting(task_datetime)
            except ValueError as e:
                message = f"{self.localization.get_text(self.model.current_language, 'format_error')}: {e}"
                self.view.update_info_bar(message, is_success=False)
                self.view.update_status_display()
        
        def on_cancel_error(err_msg):
            message = f"{self.localization.get_text(self.model.current_language, 'command_failed')}: {err_msg}. {self.localization.get_text(self.model.current_language, 'run_as_admin_note')}"
            self.view.update_info_bar(message, is_success=False)
            on_cancel_success(None)

        self.system_executor.cancel_task(
            functools.partial(self.view.root.after, 0, on_cancel_success),
            functools.partial(self.view.root.after, 0, on_cancel_error)
        )

    def _execute_task_setting(self, task_datetime):
        current_time = datetime.datetime.now()
        if task_datetime < current_time:
            self.model.clear_task()
            self.view.update_info_bar(self.localization.get_text(self.model.current_language, "time_in_past"), is_success=False)
            self.view.update_status_display()
            return
        
        op_type = self.view.operation_var.get()
        seconds_until_task = (task_datetime - current_time).total_seconds()

        def on_success(output):
            self.model.set_task(task_datetime, op_type)
            self.view.update_status_display()
            op_text = self.localization.get_text(self.model.current_language, "shutdown_text") if op_type == "shutdown" else self.localization.get_text(self.model.current_language, "restart_text")
            message = f"{self.localization.get_text(self.model.current_language, 'task_set')}{task_datetime.strftime('%Y-%m-%d %H:%M:%S')}{self.localization.get_text(self.model.current_language, 'at')}{op_text}"
            self.view.update_info_bar(message, is_success=True)

        def on_error(err_msg):
            self.model.clear_task()
            self.view.update_status_display()
            message = f"{self.localization.get_text(self.model.current_language, 'command_failed')}: {err_msg}\n{self.localization.get_text(self.model.current_language, 'run_as_admin_note')}"
            self.view.update_info_bar(message, is_success=False)

        self.system_executor.set_task(
            seconds_until_task, op_type,
            functools.partial(self.view.root.after, 0, on_success),
            functools.partial(self.view.root.after, 0, on_error)
        )

    def cancel_task(self):
        self.view.update_info_bar(self.localization.get_text(self.model.current_language, "cancelling_existing"), is_success=True)
        self.view.root.update_idletasks()
        
        def on_success(output):
            self.model.clear_task()
            self.view.update_status_display()
            self.view.update_info_bar(self.localization.get_text(self.model.current_language, "task_canceled"), is_success=True)

        def on_error(err_msg):
            if "no pending system shutdowns" in err_msg.lower() or "没有待执行的关机" in err_msg:
                on_success(err_msg)
            else:
                message = f"{self.localization.get_text(self.model.current_language, 'command_failed')}: {err_msg}\n{self.localization.get_text(self.model.current_language, 'run_as_admin_note')}"
                self.view.update_info_bar(message, is_success=False)
            self.view.update_status_display()

        self.system_executor.cancel_task(
            functools.partial(self.view.root.after, 0, on_success),
            functools.partial(self.view.root.after, 0, on_error)
        )


class MainController:
    """主控制器：连接所有组件，处理用户输入。"""
    def __init__(self, root, config_manager, localization_manager, system_executor):
        self.root = root
        self.config_manager = config_manager
        self.localization = localization_manager
        self.system_executor = system_executor
        
        self.model = SchedulerModel(self.config_manager.load_config())
        self.view = SchedulerView(self.root, self.localization, self.model)
        self.task_scheduler = TaskScheduler(self.model, self.system_executor, self.localization, self.view)
        
        self.view.set_callbacks(self._get_callbacks())

        self.view.year_combobox.bind("<<ComboboxSelected>>", self.update_days_dropdown)
        self.view.month_combobox.bind("<<ComboboxSelected>>", self.update_days_dropdown)
        self.check_system_compatibility()

    def _get_callbacks(self):
        return {
            "on_language_change": self.change_language,
            "on_set_task": self.set_task,
            "on_cancel_task": self.task_scheduler.cancel_task,
            "on_set_custom_timer": self.set_custom_timer_task,
            "on_show_donate": self.show_donate_qr,
            "on_set_30": lambda e=None: self.task_scheduler.set_task(lambda: datetime.datetime.now() + datetime.timedelta(minutes=30)),
            "on_set_60": lambda e=None: self.task_scheduler.set_task(lambda: datetime.datetime.now() + datetime.timedelta(minutes=60)),
            "on_set_today_750": lambda e=None: self.set_task_today_750(),
            "on_set_tomorrow_750": lambda e=None: self.set_task_tomorrow_750(),
            "on_set_tomorrow_800": lambda e=None: self.set_task_tomorrow_800(),
            "on_set_monday_800": lambda e=None: self.set_task_for_weekday(0, 8, 0),
            "on_set_tuesday_800": lambda e=None: self.set_task_for_weekday(1, 8, 0),
            "on_set_wednesday_800": lambda e=None: self.set_task_for_weekday(2, 8, 0),
            "on_set_thursday_800": lambda e=None: self.set_task_for_weekday(3, 8, 0),
            "on_set_friday_800": lambda e=None: self.set_task_for_weekday(4, 8, 0),
            "on_set_saturday_750": lambda e=None: self.set_task_for_weekday(5, 7, 50),
            "on_set_saturday_800": lambda e=None: self.set_task_for_weekday(5, 8, 0),
            "on_set_sunday_800": lambda e=None: self.set_task_for_weekday(6, 8, 0),
        }

    def change_language(self, event=None):
        new_language = self.view.language_var.get()
        if new_language != self.model.current_language:
            self.model.current_language = new_language
            self.view.update_ui_text()
    
    def update_days_dropdown(self, event=None):
        days = DateTimeUtils.generate_days(self.view.year_var.get(), self.view.month_var.get())
        self.view.day_combobox.config(values=days)
        if self.view.day_var.get() not in days:
            self.view.day_var.set(days[-1])

    def set_task(self):
        def get_dt_from_ui():
            dt_str = f"{self.view.year_var.get()}-{self.view.month_var.get()}-{self.view.day_var.get()} " \
                     f"{self.view.hour_var.get()}:{self.view.minute_var.get()}:{self.view.second_var.get()}"
            return datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
        self.task_scheduler.set_task(get_dt_from_ui)

    def set_custom_timer_task(self):
        try:
            days = int(self.view.custom_timer_days_var.get())
            hours = int(self.view.custom_timer_hours_var.get())
            minutes = int(self.view.custom_timer_minutes_var.get())
            if days < 0 or hours < 0 or minutes < 0 or (days + hours + minutes == 0):
                raise ValueError("Invalid time values")
            
            delta = datetime.timedelta(days=days, hours=hours, minutes=minutes)
            self.task_scheduler.set_task(lambda: datetime.datetime.now() + delta)
        except ValueError:
            self.view.update_info_bar(self.localization.get_text(self.model.current_language, "invalid_timer_value"), is_success=False)

    def show_donate_qr(self):
        donate_view = DonateView(self.root, self.localization, self.model.current_language)
        donate_view.show()
    
    def set_task_for_weekday(self, weekday, hour, minute):
        task_dt = DateTimeUtils.get_weekday_task_time(weekday, hour, minute)
        self.task_scheduler.set_task(lambda: task_dt)

    def set_task_today_750(self):
        now = datetime.datetime.now()
        task_dt = now.replace(hour=7, minute=50, second=0, microsecond=0)
        if now > task_dt:
             task_dt += datetime.timedelta(days=1)
        self.task_scheduler.set_task(lambda: task_dt)

    def set_task_tomorrow_750(self):
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        task_dt = datetime.datetime.combine(tomorrow, datetime.time(7, 50))
        self.task_scheduler.set_task(lambda: task_dt)

    def set_task_tomorrow_800(self):
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        task_dt = datetime.datetime.combine(tomorrow, datetime.time(8, 0))
        self.task_scheduler.set_task(lambda: task_dt)

    def check_system_compatibility(self):
        if self.system_executor.system not in ["Windows", "Linux", "Darwin"]:
            messagebox.showerror(
                self.localization.get_text(self.model.current_language, "error"), 
                f"Unsupported operating system: {self.system_executor.system}"
            )
            self.root.after(100, self.root.destroy)
def main():
    root = ttk.Window(themename="superhero")
        # --- 在此处添加图标嵌入代码 ---
    # 确保 sd.ico 文件与此脚本位于同一目录
    if os.path.exists("sd.ico"):
        try:
            root.iconbitmap("sd.ico")
        except Exception as e:
            print(f"Error setting icon: {e}")
    # -----------------------------
    config_manager = ConfigManager()
    localization_manager = LocalizationManager()
    system_executor = SystemExecutor(platform.system())
    app = MainController(root, config_manager, localization_manager, system_executor)
    root.mainloop()

if __name__ == "__main__":
    main()
