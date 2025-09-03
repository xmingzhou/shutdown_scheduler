### **Binary encapsulated exe software**
您可以在release区域下载“.exe”格式的软件
You can download software for '.exe' format in the release area
<img width="345" height="117" alt="image" src="https://github.com/user-attachments/assets/19433020-e706-47c8-b00f-b1049a59ac29" />
<img width="241" height="137" alt="image" src="https://github.com/user-attachments/assets/eac15e6c-ec0a-421d-bfd6-b393126b71ad" />



### **GUI interface**
GUI interface


<img width="683" height="590" alt="image" src="https://github.com/user-attachments/assets/688a4001-d450-4737-bc70-ca12fb76d8df" />

<img width="684" height="598" alt="image" src="https://github.com/user-attachments/assets/de185f61-dda5-48d5-9e0e-28299bd6c22a" />

### **License Description**

 The Shutdown Scheduler program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program. If not, see <https://www.gnu.org/licenses/>.

 Copyright (c) 2025 Xiangming Zhou

 SUPPLEMENTARY DISCLAIMER
 The copyright holder assumes no responsibility for any illegal use of this software,
 or for any data loss, damages, or other liabilities arising directly or indirectly
 from its use. The user of this software assumes all risks and full responsibility
 for compliance with all applicable local, national, and international laws.
 If you find this software useful, a voluntary economic contribution to the author
 is appreciated but not required.


 自动关机程序软件是自由软件：您可以根据自由软件基金会发布的GNU通用公共许可证条款重新分发和/或修改它，
 无论是许可证的第3版，或者是（由您选择）任何后续版本。

 此程序是本着对您有用的目的而分发的，
 但不提供任何担保；甚至不包括适销性或适用于特定用途的隐含担保。有关更多详情，请参阅GNU通用公共许可证。

 您应该已经随此程序一起收到了GNU通用公共许可证的副本。
 如果没有，请参见<https://www.gnu.org/licenses/>.

 Copyright (c) 2025 Xiangming Zhou

 补充免责声明
 版权持有人不对本软件的任何非法使用，或因使用本软件直接或间接引起的数据丢失、损害或其他责任承担任何责任。
 本软件的使用者需自行承担所有风险，并对遵守所有适用的地方、国家和国际法律负全责。
 如果您发现此软件有用，虽然作者感激您的自愿经济贡献，但这并不是强制要求的。


---

### **中文版**

### 简介

这是一个使用 **Python** 和 **`ttkbootstrap`** 库开发的桌面应用程序，旨在为用户提供一个直观、易用的定时关机或重启工具。它支持  **Windows** 、**Linux** 和 **macOS** 三大主流操作系统，并内置了多种语言，以满足不同用户的需求。程序的界面简洁美观，核心功能强大，可以精确到秒来设置定时任务。

---

### 主要功能

* **跨平台支持** : 程序通过适配不同操作系统的系统命令，确保其在 **Windows、Linux 和 macOS (Darwin)** 上都能稳定运行。
* **多语言界面** : 内置 **中文、英文、法文和日文** 四种语言，用户可以轻松切换。
* **灵活的任务设置** :
  * **具体时间** : 可通过下拉菜单精确设置到年、月、日、时、分、秒的执行时间。
  * **自定义倒计时** : 可按天、小时和分钟设置相对当前时间的倒计时任务。
* **丰富的快捷选项** : 为了提升效率，程序提供了一系列预设的快捷按钮，包括倒计时和固定时间点，如“30分钟后”、“明日 8:00”、“周六 7:50”等。
* **实时状态与反馈** : 界面底部设有状态栏和信息栏，实时显示任务状态，并提供操作成功或失败的即时反馈。
* **任务管理** : 可随时通过点击**“取消任务”**按钮来中断或取消已设置的任务。
* **用户配置持久化** : 程序会自动将用户上次选择的语言和默认的倒计时分钟数保存到 `config.json` 文件中。

---

### 技术解析

#### 程序架构

本程序采用清晰的  **模块化设计** ，将不同功能划分到独立的类中，遵循了  **单一职责原则** ，便于代码的维护和扩展。其核心架构可以被视为一个精简的 MVC（模型-视图-控制器）模式：

* `SchedulerModel`: 作为  **模型层** ，存储程序的状态数据，如当前选定的任务类型、时间和语言。
* `SchedulerView`: 作为  **视图层** ，负责所有 GUI 界面的构建和渲染。它只处理界面的显示逻辑，不包含任何业务处理。
* `TaskScheduler`: 包含核心  **业务逻辑** ，处理任务设置、时间验证和任务取消的调度。
* `MainController`: 作为  **控制器层** ，连接模型、视图和业务逻辑，处理用户输入和事件响应，例如按钮点击、菜单选择等。

#### 关键模块

* `ConfigManager`: 管理配置文件的读写和持久化，确保用户设置在下次启动时依然有效。
* `LocalizationManager`: 集中管理所有语言的文本资源，通过一个多层字典结构实现多语言支持，便于添加新语言或修改现有文本。
* `SystemExecutor`: 抽象出系统命令的执行逻辑，通过判断 `platform.system()` 的返回值来调用不同操作系统下的关机和重启命令，实现了跨平台兼容性。
* `threading` 模块：用于异步执行耗时的系统命令，确保在执行关机/重启操作时，GUI 界面不会出现无响应或“冻结”的情况，提升了用户体验。

---

### 文件结构

本程序通常包含以下文件，建议将它们放置在同一目录下：

```
.
├── shutdown_scheduler_multi_lang.py  # 主程序文件
├── sd.ico                            # 程序图标文件（可选）
└── config.json                       # 用户配置文件（程序首次运行自动生成）
```

---

### 使用方法

#### 1. 运行依赖

本程序基于 Python 3.x 编写，并使用了 `tkinter`、`datetime` 等内置的标准库。但它还依赖一个  **第三方库** ，因此在首次运行前，请通过以下命令安装：

**Bash**

```
pip install ttkbootstrap
```

#### 2. 运行程序

在终端或命令行中，导航到程序文件所在的目录，然后执行以下命令：

**Bash**

```
python shutdown_scheduler_multi_lang.py
```

> **注意** : 在 Windows、Linux 和 macOS 上，执行关机或重启命令通常需要  **管理员（或 root）权限** 。如果程序运行时提示“命令执行失败”，请关闭程序后，以管理员身份重新运行。

---

### 封装与分发

如果你希望将程序打包成一个独立的可执行文件，以便在没有 Python 环境的机器上运行，可以使用  **PyInstaller** 。

#### 1. 安装 PyInstaller

首先，请安装 PyInstaller：

**Bash**

```
pip install pyinstaller
```

#### 2. 执行打包命令

在程序文件所在的目录下，运行以下命令。该命令会将所有依赖项打包成一个独立的 `.exe` 或 `.app` 文件，并隐藏控制台窗口。

**Bash**

```
pyinstaller --onefile --windowed --icon=sd.ico shutdown_scheduler_multi_lang.pyw
```

* `--onefile`: 生成单个可执行文件。
* `--windowed` 或 `-w`: 隐藏控制台窗口。
* `--icon=sd.ico` 或 `-i sd.ico`: 指定程序图标。

打包完成后，你会在 `dist` 文件夹中找到最终的可执行文件。

---

### 开发者信息与捐赠

* **作者** : Xiangming Zhou
* **邮箱** : zhouxmmail@163.com
* **版权所有** : © Copyright Xiangming Zhou

如果你对本程序感到满意，欢迎点击“捐助作者”按钮，以支持作者的持续开发和维护工作。

---

### **英文版 (English)**

### Introduction

This is a desktop application developed with **Python** and the **`ttkbootstrap`** library, designed to provide users with an intuitive and easy-to-use tool for scheduled shutdown or restart. It supports the three major operating systems— **Windows** ,  **Linux** , and  **macOS** —and includes built-in support for multiple languages to meet the needs of different users. The program has a clean and aesthetically pleasing interface, with powerful core functionality that allows for setting tasks with second-level precision.

---

### Key Features

* **Cross-platform Support** : The application ensures stable operation on **Windows, Linux, and macOS (Darwin)** by adapting to the system commands of different operating systems.
* **Multi-language Interface** : Includes built-in support for  **Chinese, English, French, and Japanese** , allowing users to easily switch between languages.
* **Flexible Task Settings** :
* **Specific Time** : Allows users to set the execution time with precision down to the year, month, day, hour, minute, and second using dropdown menus.
* **Custom Countdown** : Tasks can be set as a countdown relative to the current time, specified in days, hours, and minutes.
* **Rich Quick Options** : To improve efficiency, the program provides a series of preset quick buttons, including countdowns and fixed time points, such as "in 30 minutes," "tomorrow at 8:00 AM," or "Saturday at 7:50 PM."
* **Real-time Status and Feedback** : A status bar and info bar at the bottom of the interface display the real-time task status and provide instant feedback on the success or failure of an operation.
* **Task Management** : Users can interrupt or cancel a set task at any time by clicking the **"Cancel Task"** button.
* **Persistent User Configuration** : The program automatically saves the user's last selected language and default countdown minutes to the `config.json` file.

---

### Technical Analysis

#### Program Architecture

This program uses a clear  **modular design** , dividing different functionalities into independent classes, following the **Single Responsibility Principle** for easy maintenance and extension. Its core architecture can be seen as a simplified MVC (Model-View-Controller) pattern:

* `SchedulerModel`: Serves as the  **Model layer** , storing the program's state data, such as the currently selected task type, time, and language.
* `SchedulerView`: Serves as the  **View layer** , responsible for building and rendering all GUI interfaces. It only handles display logic and does not contain any business processing.
* `TaskScheduler`: Contains the core  **business logic** , handling task setup, time validation, and task cancellation scheduling.
* `MainController`: Acts as the  **Controller layer** , connecting the Model, View, and business logic, and handling user input and event responses, such as button clicks and menu selections.

#### Key Modules

* `ConfigManager`: Manages reading, writing, and persistence of the configuration file, ensuring user settings are retained for the next launch.
* `LocalizationManager`: Centralizes the management of text resources for all languages, implementing multi-language support through a multi-level dictionary structure, which makes it easy to add new languages or modify existing text.
* `SystemExecutor`: Abstracts the execution logic of system commands, calling different shutdown and restart commands based on the return value of `platform.system()`, achieving cross-platform compatibility.
* `threading` module: Used to asynchronously execute time-consuming system commands, ensuring the GUI does not become unresponsive or "frozen" during shutdown/restart operations, thereby improving the user experience.

---

### File Structure

This program typically includes the following files, and it is recommended to place them in the same directory:

```
.
├── shutdown_scheduler_multi_lang.py  # Main program file
├── sd.ico                            # Program icon file (optional)
└── config.json                       # User configuration file (automatically generated on first run)
```

---

### Usage

#### 1. Running Dependencies

This program is written in Python 3.x and uses built-in standard libraries like `tkinter` and `datetime`. However, it also depends on one  **third-party library** , so please install it with the following command before the first run:

**Bash**

```
pip install ttkbootstrap
```

#### 2. Running the Program

In a terminal or command line, navigate to the directory where the program file is located, then execute the following command:

**Bash**

```
python shutdown_scheduler_multi_lang.py
```

> **Note** : Executing shutdown or restart commands on Windows, Linux, and macOS typically requires  **administrator (or root) privileges** . If the program shows "command execution failed," please close the program and re-run it with administrator privileges.

---

### Packaging and Distribution

If you wish to package the program into a standalone executable file so that it can be run on machines without a Python environment, you can use  **PyInstaller** .

#### 1. Installing PyInstaller

First, please install PyInstaller:

**Bash**

```
pip install pyinstaller
```

#### 2. Executing the Packaging Command

In the directory where the program file is located, run the following command. This command will package all dependencies into a single `.exe` or `.app` file and hide the console window.

**Bash**

```
pyinstaller --onefile --windowed --icon=sd.ico shutdown_scheduler_multi_lang.pyw
```

* `--onefile`: Generates a single executable file.
* `--windowed` or `-w`: Hides the console window.
* `--icon=sd.ico` or `-i sd.ico`: Specifies the program icon.

After packaging is complete, you will find the final executable file in the `dist` folder.

---

### Developer Information & Donation

* **Author** : Xiangming Zhou
* **Email** : zhouxmmail@163.com
* **Copyright** : © Copyright Xiangming Zhou

If you are satisfied with this program, please consider clicking the "Donate to Author" button to support the author's continued development and maintenance work.

---

### **日语版 (日本語)**

### 概要

これは、**Python** と **`ttkbootstrap`** ライブラリを使用して開発されたデスクトップアプリケーションで、ユーザーに直感的で使いやすいシャットダウンまたは再起動のスケジュール設定ツールを提供することを目的としています。 **Windows** 、 **Linux** 、**macOS** の3つの主要なオペレーティングシステムに対応しており、さまざまなユーザーのニーズを満たすために複数の言語が組み込まれています。プログラムのインターフェースはシンプルで美しく、強力なコア機能により、秒単位で精密なタスクを設定できます。

---

### 主な機能

* **クロスプラットフォーム対応** : プログラムは、異なるオペレーティングシステムのシステムコマンドに適応することで、**Windows、Linux、macOS (Darwin)** のすべてで安定して動作することを保証します。
* **多言語インターフェース** : **中国語、英語、フランス語、日本語** の4つの言語が内蔵されており、ユーザーは簡単に切り替えることができます。
* **柔軟なタスク設定** :
  * **特定の日時** : プルダウンメニューを使用して、年、月、日、時、分、秒まで正確に実行時間を設定できます。
  * **カスタムカウントダウン** : 現在時刻を基準として、日、時間、分単位でカウントダウンタスクを設定できます。
* **豊富なクイックオプション** : 効率を高めるため、プログラムには「30分後」、「明日 8:00」、「土曜 7:50」など、カウントダウンや固定時刻を含む一連のプリセットされたクイックボタンが提供されています。
* **リアルタイムの状態とフィードバック** : インターフェースの下部にあるステータスバーと情報バーは、タスクの状態をリアルタイムで表示し、操作の成功または失敗に関する即時のフィードバックを提供します。
* **タスク管理** : **「タスクキャンセル」** ボタンをクリックすることで、設定済みのタスクをいつでも中断またはキャンセルできます。
* **ユーザー設定の永続化** : プログラムは、ユーザーが前回選択した言語とデフォルトのカウントダウン分数値を自動的に `config.json` ファイルに保存します。

---

### 技術分析

#### プログラムアーキテクチャ

このプログラムは、クリアな **モジュール化設計** を採用しており、異なる機能を独立したクラスに分割し、**単一責任の原則** に従っています。これにより、コードの保守と拡張が容易になります。そのコアアーキテクチャは、簡素化されたMVC（モデル・ビュー・コントローラー）パターンと見なすことができます。

* `SchedulerModel`: **モデル層** として、現在のタスクタイプ、時間、言語など、プログラムの状態データを格納します。
* `SchedulerView`: **ビュー層** として、すべてのGUIインターフェースの構築とレンダリングを担当します。表示ロジックのみを扱い、ビジネスロジックは一切含まれません。
* `TaskScheduler`: コアとなる **ビジネスロジック** を含み、タスクの設定、時間の検証、タスクキャンセルのスケジューリングを処理します。
* `MainController`: **コントローラー層** として、モデル、ビュー、およびビジネスロジックを接続し、ボタンのクリックやメニューの選択などのユーザー入力とイベント応答を処理します。

#### 主要モジュール

* `ConfigManager`: 設定ファイルの読み書きと永続化を管理し、次回の起動時にもユーザー設定が有効であることを保証します。
* `LocalizationManager`: すべての言語のテキストリソースを一元管理し、多層辞書構造を介して多言語サポートを実現します。これにより、新しい言語の追加や既存のテキストの修正が容易になります。
* `SystemExecutor`: システムコマンドの実行ロジックを抽象化し、`platform.system()` の戻り値に基づいて異なるOSのシャットダウンおよび再起動コマンドを呼び出すことで、クロスプラットフォーム互換性を実現します。
* `threading` モジュール：時間のかかるシステムコマンドを非同期で実行するために使用され、シャットダウン/再起動操作中にGUIインターフェースが応答不能になったり「フリーズ」したりするのを防ぎ、ユーザーエクスペリエンスを向上させます。

---

### ファイル構造

このプログラムは通常、以下のファイルを含み、これらを同じディレクトリに配置することをお勧めします。

```
.
├── shutdown_scheduler_multi_lang.py  # メインプログラムファイル
├── sd.ico                            # プログラムアイコンファイル（オプション）
└── config.json                       # ユーザー設定ファイル（プログラムの初回実行時に自動生成）
```

---

### 使用方法

#### 1. 実行に必要な依存関係

このプログラムは Python 3.x で記述されており、`tkinter`、`datetime` などの組み込み標準ライブラリを使用しています。しかし、もう1つの **サードパーティライブラリ** に依存しているため、初回実行前に以下のコマンドでインストールしてください。

**Bash**

```
pip install ttkbootstrap
```

#### 2. プログラムの実行

ターミナルまたはコマンドラインで、プログラムファイルが置かれているディレクトリに移動し、以下のコマンドを実行します。

**Bash

```
python shutdown_scheduler_multi_lang.py
```

> **注意** : Windows、Linux、macOSでシャットダウンや再起動コマンドを実行するには、通常 **管理者（またはroot）権限** が必要です。プログラムの実行時に「コマンド実行失敗」と表示された場合は、プログラムを閉じてから、管理者として再実行してください。

---

### パッケージ化と配布

Python環境がないマシンでも実行できるスタンドアロンの実行可能ファイルとしてプログラムをパッケージ化したい場合は、**PyInstaller** を使用できます。

#### 1. PyInstaller のインストール

まず、PyInstaller をインストールしてください。

**Bash

```
pip install pyinstaller
```

#### 2. パッケージ化コマンドの実行

プログラムファイルが置かれているディレクトリで、以下のコマンドを実行します。このコマンドは、すべての依存関係を単一の `.exe` または `.app` ファイルにパッケージ化し、コンソールウィンドウを非表示にします。

**Bash

```
pyinstaller --onefile --windowed --icon=sd.ico shutdown_scheduler_multi_lang.pyw
```

* `--onefile`: 単一の実行可能ファイルを生成します。
* `--windowed` または `-w`: コンソールウィンドウを非表示にします。
* `--icon=sd.ico` または `-i sd.ico`: プログラムアイコンを指定します。

パッケージ化が完了すると、`dist` フォルダ内に最終的な実行可能ファイルが見つかります。

---

### 開発者情報と寄付

* **作者** : Xiangming Zhou
* **メール** : zhouxmmail@163.com
* **著作権** : © Copyright Xiangming Zhou

このプログラムに満足していただけた場合は、「作者に寄付する」ボタンをクリックして、作者の継続的な開発と保守作業を支援していただければ幸いです。

---

### **法语版 (Français)**

### Introduction

Ceci est une application de bureau développée en **Python** avec la bibliothèque  **`ttkbootstrap`** , conçue pour fournir aux utilisateurs un outil intuitif et facile à utiliser pour programmer l'arrêt ou le redémarrage. Elle est compatible avec les trois principaux systèmes d'exploitation— **Windows** ,  **Linux** , et  **macOS** —et inclut la prise en charge de plusieurs langues pour répondre aux besoins de différents utilisateurs. L'interface du programme est simple et esthétique, et sa fonctionnalité de base est puissante, permettant de définir des tâches avec une précision à la seconde près.

---

### Fonctionnalités principales

* **Support multiplateforme** : Le programme adapte les commandes du système pour garantir un fonctionnement stable sur  **Windows, Linux et macOS (Darwin)** .
* **Interface multilingue** : Intègre le support pour quatre langues :  **chinois, anglais, français et japonais** , permettant aux utilisateurs de basculer facilement entre elles.
* **Paramètres de tâche flexibles** :
  * **Heure précise** : Permet de définir l'heure d'exécution avec une précision jusqu'à l'année, le mois, le jour, l'heure, la minute et la seconde via des menus déroulants.
  * **Compte à rebours personnalisé** : Les tâches peuvent être définies comme un compte à rebours par rapport à l'heure actuelle, spécifié en jours, heures et minutes.
* **Options rapides étendues** : Pour améliorer l'efficacité, le programme propose une série de boutons rapides prédéfinis, incluant des comptes à rebours et des heures fixes, tels que "dans 30 minutes", "demain à 8h00", ou "samedi à 19h50".
* **Statut et retour en temps réel** : Une barre de statut et une barre d'information en bas de l'interface affichent l'état de la tâche en temps réel et fournissent un retour immédiat sur le succès ou l'échec d'une opération.
* **Gestion des tâches** : Les utilisateurs peuvent interrompre ou annuler une tâche programmée à tout moment en cliquant sur le bouton  **"Annuler la tâche"** .
* **Persistance de la configuration utilisateur** : Le programme enregistre automatiquement la dernière langue sélectionnée par l'utilisateur et le nombre de minutes par défaut pour le compte à rebours dans le fichier `config.json`.

---

### Analyse technique

#### Architecture du programme

Ce programme utilise une **conception modulaire** claire, divisant les différentes fonctionnalités en classes indépendantes, suivant le **principe de responsabilité unique** pour une maintenance et une extension faciles du code. Son architecture de base peut être vue comme un modèle MVC (Modèle-Vue-Contrôleur) simplifié :

* `SchedulerModel` : Sert de  **couche Modèle** , stockant les données d'état du programme, telles que le type de tâche, l'heure et la langue actuellement sélectionnés.
* `SchedulerView` : Sert de  **couche Vue** , responsable de la construction et du rendu de toutes les interfaces graphiques (GUI). Il ne gère que la logique d'affichage et ne contient aucun traitement métier.
* `TaskScheduler` : Contient la **logique métier** de base, gérant la configuration des tâches, la validation de l'heure et la programmation de l'annulation des tâches.
* `MainController` : Agit comme la  **couche Contrôleur** , connectant le Modèle, la Vue et la logique métier, et gérant les entrées utilisateur et les réponses aux événements, tels que les clics sur les boutons et les sélections de menu.

#### Modules clés

* `ConfigManager` : Gère la lecture, l'écriture et la persistance du fichier de configuration, garantissant que les paramètres de l'utilisateur sont conservés pour le prochain lancement.
* `LocalizationManager` : Centralise la gestion des ressources textuelles pour toutes les langues, en mettant en œuvre le support multilingue via une structure de dictionnaire à plusieurs niveaux, ce qui facilite l'ajout de nouvelles langues ou la modification des textes existants.
* `SystemExecutor` : Gère de manière abstraite la logique d'exécution des commandes système, en appelant différentes commandes d'arrêt et de redémarrage en fonction de la valeur de retour de `platform.system()`, assurant ainsi la compatibilité multiplateforme.
* Module `threading` : Utilisé pour exécuter de manière asynchrone les commandes système de longue durée, garantissant que l'interface graphique ne devient pas non réactive ou "gelée" pendant les opérations d'arrêt/redémarrage, améliorant ainsi l'expérience utilisateur.

---

### Structure des fichiers

Ce programme comprend généralement les fichiers suivants, et il est recommandé de les placer dans le même répertoire :

```
.
├── shutdown_scheduler_multi_lang.py  # Fichier principal du programme
├── sd.ico                            # Fichier d'icône du programme (optionnel)
└── config.json                       # Fichier de configuration utilisateur (généré automatiquement lors de la première exécution)
```

---

### Utilisation

#### 1. Dépendances d'exécution

Ce programme est écrit en Python 3.x et utilise des bibliothèques standard intégrées comme `tkinter` et `datetime`. Cependant, il dépend également d'une  **bibliothèque tierce** , veuillez donc l'installer avec la commande suivante avant la première exécution :

**Bash**

```
pip install ttkbootstrap
```

#### 2. Exécution du programme

Dans un terminal ou une ligne de commande, naviguez vers le répertoire où se trouve le fichier du programme, puis exécutez la commande suivante :

**Bash**

```
python shutdown_scheduler_multi_lang.py
```

> **Remarque** : L'exécution des commandes d'arrêt ou de redémarrage sur Windows, Linux et macOS nécessite généralement des  **privilèges d'administrateur (ou de root)** . Si le programme affiche "échec de l'exécution de la commande", veuillez fermer le programme et le relancer avec les privilèges d'administrateur.

---

### Packaging et distribution

Si vous souhaitez empaqueter le programme dans un fichier exécutable autonome afin qu'il puisse être exécuté sur des machines sans environnement Python, vous pouvez utiliser  **PyInstaller** .

#### 1. Installation de PyInstaller

Tout d'abord, veuillez installer PyInstaller :

**Bash**

```
pip install pyinstaller
```

#### 2. Exécution de la commande de packaging

Dans le répertoire où se trouve le fichier du programme, exécutez la commande suivante. Cette commande empaquettera toutes les dépendances dans un seul fichier `.exe` ou `.app` et masquera la fenêtre de la console.

**Bash**

```
pyinstaller --onefile --windowed --icon=sd.ico shutdown_scheduler_multi_lang.pyw
```

* `--onefile` : Génère un seul fichier exécutable.
* `--windowed` ou `-w` : Masque la fenêtre de la console.
* `--icon=sd.ico` ou `-i sd.ico` : Spécifie l'icône du programme.

Une fois le packaging terminé, vous trouverez le fichier exécutable final dans le dossier `dist`.

---

### Informations sur le développeur et dons

* **Auteur** : Xiangming Zhou
* **Email** : zhouxmmail@163.com
* **Copyright** : © Copyright Xiangming Zhou

Si vous êtes satisfait de ce programme, n'hésitez pas à cliquer sur le bouton "Faire un don à l'auteur" pour soutenir le travail de développement et de maintenance continu de l'auteur.
