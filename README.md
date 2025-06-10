

# Shutdown/Restart Scheduler

A simple and easy-to-use desktop application to schedule a shutdown or restart for your computer. It supports multiple languages and offers various quick-setting options.

## Features

* **Multi-language Support**: Currently supports Chinese, English, French, and Japanese.
* **Operation Type Selection**: Choose between "Shutdown" or "Restart" operations.
* **Precise Time Setting**: Users can precisely set the year, month, day, hour, minute, and second to schedule the task.
* **Quick Setting Options**:
    * Shutdown/restart after 10, 30 minutes, 1, 2, 4, or 8 hours.
    * Shutdown/restart tomorrow morning at 7:30 AM.
    * Shutdown/restart tomorrow morning at 8:00 AM.
    * Shutdown/restart next Saturday morning at 7:30 AM.
* **Task Status Display**: Shows the current status of any scheduled task.
* **Task Cancellation**: Easily cancel any scheduled task at any time.
* **Cross-platform Compatibility**: Supports Windows, Linux, and macOS operating systems.

## Screenshots

As I cannot generate images directly, please run the application to see the interface.

## How to Run

1.  **Prepare Python Environment**:
    Ensure you have Python 3.x installed on your computer. You can download and install it from the [official Python website](https://www.python.org/downloads/).

2.  **Install Dependencies**:
    This project relies on `tkinter`, which usually comes bundled with Python. If it's missing from your Python environment, you might need to install it separately (though this is uncommon).

3.  **Download the Code**:
    Download the `shutdown_scheduler_multi_lang.py` file to your local machine.

4.  **Run the Application**:
    Open a terminal or command prompt, navigate to the directory where you saved the file, and run the following command:

    ```bash
    python shutdown_scheduler_multi_lang.py
    ```

    The application window will appear.

## Usage

1.  **Select Language**: Choose your preferred language from the top-right corner of the interface.
2.  **Select Operation Type**: In the "Operation Type" section, choose either "Shutdown" or "Restart".
3.  **Set Time**:
    * **Manual Setting**: Use the dropdown menus for year, month, day, hour, minute, and second to precisely set when you want the task to execute.
    * **Quick Settings**: Click on the "Quick Shutdown Options" buttons below, such as "30 minutes later", "Tomorrow 7:30", etc., to quickly set a task for a predefined time.
4.  **Set Task**: Click the "Set Task" button to schedule your chosen operation.
5.  **Cancel Task**: If you wish to cancel a scheduled task, click the "Cancel Task" button.
6.  **View Status**: The "Status" area will display the current task status.

## Important Notes

* On Linux or macOS systems, setting shutdown/restart tasks might require `sudo` privileges. The application will attempt to execute `sudo shutdown` commands, which may prompt you for your administrator password.
* Ensure that the time you set is later than the current time; otherwise, the application will display an error.
* When canceling a task on Windows, the application will attempt to execute the cancellation command (`shutdown /a`) even if no task is actively scheduled. This is to ensure any potential pending tasks are cleared.

## Developer

© 2025 ZXM












# 定时关机/重启程序

一个简单易用的桌面应用程序，用于定时关机或重启你的电脑。支持多语言，并提供多种快速设置选项。

## 功能特性

* **多语言支持**: 目前支持中文、英语、法语和日语。
* **操作类型选择**: 可以选择执行“关机”或“重启”操作。
* **精确时间设置**: 用户可以精确设置年、月、日、时、分、秒，来安排任务。
* **快速设置选项**:
    * 10分钟后、30分钟后、1小时后、2小时后、4小时后、8小时后关机/重启。
    * 次日早晨7:30关机/重启。
    * 次日早晨8:00关机/重启。
    * 下周六早晨7:30关机/重启。
* **任务状态显示**: 实时显示当前是否有任务正在进行。
* **任务取消**: 随时取消已设置的定时任务。
* **跨平台兼容**: 支持 Windows、Linux 和 macOS 操作系统。

## 截图

由于无法直接生成截图，请自行运行程序查看界面。

## 如何运行

1.  **准备 Python 环境**:
    确保你的电脑上安装了 Python 3.x。你可以从 [Python 官方网站](https://www.python.org/downloads/) 下载并安装。

2.  **安装依赖**:
    本项目依赖 `tkinter`，它通常随 Python 一起安装。如果你的 Python 环境缺少它，可能需要单独安装（但这种情况不常见）。

3.  **下载代码**:
    将 `shutdown_scheduler_multi_lang.py` 文件下载到你的本地。

4.  **运行程序**:
    打开终端或命令提示符，导航到文件所在的目录，然后运行以下命令：

    ```bash
    python shutdown_scheduler_multi_lang.py
    ```

    程序界面将会弹出。

## 使用方法

1.  **选择语言**: 在界面右上角选择你偏好的语言。
2.  **选择操作类型**: 在“操作类型”部分选择“关机”或“重启”。
3.  **设置时间**:
    * **手动设置**: 使用年份、月份、日期、小时、分钟和秒的下拉菜单来精确设置你希望任务执行的时间。
    * **快速设置**: 点击下方的“快捷关机选项”按钮，例如“30分钟后”、“明日7:30”等，即可快速设置一个预定义时间的任务。
4.  **设置任务**: 点击“设置任务”按钮来安排你的定时操作。
5.  **取消任务**: 如果你想取消已设置的任务，点击“取消任务”按钮。
6.  **查看状态**: “状态”区域会显示当前任务的状态。

## 注意事项

* 在 Linux 或 macOS 系统上，设置关机/重启任务可能需要 `sudo` 权限。程序会尝试执行 `sudo shutdown` 命令，这可能会要求你输入管理员密码。
* 请确保你设置的时间晚于当前时间，否则程序会提示错误。
* 取消任务时，在 Windows 系统上，即使没有任务在运行，程序也会尝试执行取消命令（`shutdown /a`），这是为了确保任何潜在的待处理任务都被取消。

## 开发者

© 2025 ZXM
