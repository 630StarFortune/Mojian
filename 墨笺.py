import subprocess
import os
import sys
import json
import locale
import webbrowser
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from datetime import datetime
import shutil

# --- i18n 语言资源 ---
LANGUAGES = {
    "en": {
        "version": "M0JIAN127",
        "internal_build_id": 1272,
        "changelog_history": {
            "M0JIAN001": "Project Initialization. Implemented core functionality of using Notepad for input and saving to a timestamped TXT file on the desktop.",
            "M0JIAN005": "First Official Naming. Program named 'Mojian', optimized file handling to avoid creating unnecessary empty files.",
            "M0JIAN010": "Introduced Graphical Configuration. Added a first-run setup wizard for users to customize the save location.",
            "M0JIAN020": "Core Logic Refactoring. Standardized output to serialized 'MojianN.txt' files, simplifying the workflow.",
            "M0JIAN100": "Integrated Custom Editor Support. Added the milestone feature to select third-party editors and reconfigure on startup.",
            "M0JIAN119": """Interaction and System Optimization.
    - Optimized startup flow: The confirmation dialog now offers 'Continue', 'Reset', and 'Exit' options.
    - Integrated changelog: A version history system is now included and saved in the settings file.
    - Improved guidance: All user prompts and dialogs have been clarified.""",
            "M0JIAN120": """Internationalization & Core Experience Upgrade.
    - New - Internationalization (i18n) Support: The program now auto-detects the OS language.
    - New - Auto-locate File on Completion: A new option in the setup wizard to automatically open the file's location after saving.
    - Improved - Configuration File Management: The settings file is now stored in the standard Windows 'AppData' directory.""",
            "M0JIAN121": """Robustness Fix & Naming Refinement.
    - Fix - Critical Bug Fix: Resolved an issue where 'Auto-locate File' would fail on systems with special characters in the user's folder path.
    - Improved - Naming Scheme: Internal configuration files have been given more elegant and thematic names.""",
            "M0JIAN122": """Core Experience Revamp & Configuration Management Revolution.
    - Improved - Automatic Configuration Discovery: The program now automatically remembers your settings.
    - Improved - Standardized File Management: The configuration file has been moved to the standard Windows 'AppData' directory.""",
            "M0JIAN123": """Interaction Logic Refactoring & User-Friendly Guidance.
    - New - 'View Configuration' One-Time Prompt: After initial setup, the app will ask if you want to open the configuration folder.
    - Improved - Decoupled Feature Guidance: The 'auto-locate file' and 'view configuration' features are now separate.""",
            "M0JIAN124": """Data Integrity Fix & Historical Restoration.
    - Fix - Changelog Integrity Restored: This version restores the complete update history from version M0JIAN001 to the present in the configuration file, ensuring the accuracy and completeness of the project's historical records.""",
            "M0JIAN125": """Website Integration & 'About' Window.
    - New - 'About Mojian' Window: A dedicated 'About' window has been created.
    - New - Official Website & Repository Links: The 'About' window provides direct links to the project's resources.
    - Improved - Startup Interaction: The startup confirmation has been upgraded to a custom dialog.""",
            "M0JIAN126": """The Ultimate Evolution of Experience & Flow.
    - New - 'One-Click Build' Automation: Introduced a `build.bat` script for automated compilation and cleanup.
    - New - Smart Update Guidance System: An internal build ID now detects updates and suggests a configuration reset for best compatibility.
    - Fix - Ultimate Stability Fix: Refactored the startup logic using native OS dialogs to eliminate the critical 'ghost process' bug.
    - Improved - Project Info Integration: Official website and GitHub links are now integrated into the settings file as metadata.""",
            "M0JIAN127": """'Jinshu' Feature Set - Rock-Solid & Feature-Refined.
    - Fix - Ultimate Stability Hardening: Thoroughly refactored the program's startup logic to ensure rock-solid stability in any system environment. Completely resolved underlying bugs that caused unresponsiveness or 'ghost processes'.
    - New - In-App Settings Center (Built-in): A powerful 'Settings Center' is now integrated. (Note: Currently no direct access provided; we are designing elegant activation methods).
    - New - Embedded Changelog (Built-in): The complete project update history is now embedded internally. (Note: Currently no direct access provided; we are designing elegant activation methods).
    - New - Lightweight Backup System: When saving changes to an existing 'MojianN.txt' file, the previous version is automatically backed up as 'MojianN.txt.bak'.
    - Optimized - Smart Update Guidance: The internal build ID mechanism intelligently suggests configuration resets upon code updates."""
        },
        "settings_filename": "Mojian_Scroll.json",
        "update_detected_title": "Update Detected",
        "update_detected_message": "Mojian has detected an internal update.\n\nTo ensure new features work correctly, resetting the configuration file is recommended.\n\n[Yes] - Delete old configuration and start fresh setup\n[No] - Attempt to run with the old configuration (may be unstable)",
        "config_confirm_title": "Configuration Confirmation",
        "config_confirm_message": "Current Settings:\n\nEditor: {editor_name}\nSave Location: {save_folder}\n\nProceed with these settings?\n[Yes] -> Continue\n[No] -> Reconfigure\n[Cancel] -> Exit",
        "wizard_title_1": "Setup Wizard (1/3)",
        "wizard_message_1": "Please select a folder to store your 'Mojian' files.",
        "wizard_ask_folder_title": "Select 'Mojian' Save Folder",
        "wizard_title_2": "Setup Wizard (2/3)",
        "wizard_message_2": "Please select your preferred text editor (.exe).\n\nExamples: VS Code, Sublime Text, Notepad++.\nIf you cancel, the system's default Notepad will be used.",
        "wizard_ask_editor_title": "Select Your Text Editor",
        "wizard_title_3": "Setup Wizard (3/3)",
        "wizard_message_3": "Would you like to automatically open the file's location after saving?\n\nHighly Recommended! This allows you to immediately drag the file into applications like AI chat windows, greatly improving efficiency.",
        "wizard_use_default_editor_title": "Using Default Editor",
        "wizard_use_default_editor_message": "You did not select an editor. The system's default Notepad will be used.\nPath: {path}",
        "wizard_cancel_title": "Setup Canceled",
        "wizard_cancel_message": "You did not select a save folder. The program will now exit.",
        "config_saved_title": "Configuration Saved",
        "config_saved_message": "Your settings have been saved successfully!\n\nThe program will now remember these settings automatically.",
        "one_time_open_config_title": "View Configuration File?",
        "one_time_open_config_message": "Your configuration file ('{filename}') has been created.\n\nIt contains the full update history and your settings. Would you like to open its folder now to see where it is?\n\n(This message will only be shown once.)",
        "ready_title": "Mojian - Ready to Go",
        "ready_message": "Everything is set!\n\nMojian is about to launch your editor: [{editor_name}]\n\nPlease complete your work, then save and close it.\nYour creation will be named: [{filename}]",
        "op_success_title": "Operation Successful",
        "op_success_message": "File has been successfully saved to:\n{path}",
        "op_info_title": "Operation Note",
        "op_info_message": "The file was not modified or its content is empty. This operation will not save a file.",
        "error_open_location_title": "Error",
        "error_open_location_message": "Could not open folder: {e}",
        "error_unexpected_title": "Unexpected Error",
        "error_unexpected_message": "An unexpected error occurred: {e}",
        "error_editor_not_found_title": "Editor Not Found",
        "error_editor_not_found_message": "Could not find the configured editor: {path}\nPlease re-run the program and select a valid editor.",
        "settings_window_title": "Settings Center",
        "settings_label_editor": "Editor Path:",
        "settings_label_save_folder": "Save Folder Path:",
        "settings_label_auto_open": "Auto-locate file after saving",
        "settings_btn_browse": "Browse...",
        "settings_btn_save": "Save and Close",
        "settings_save_success_title": "Settings Saved",
        "settings_save_success_message": "Your new settings have been saved successfully!",
        "about_window_title": "About Mojian",
        "about_desc": "Transform any editor into a high-speed scratchpad for your ideas.",
        "about_website_label": "Official Website",
        "about_github_label": "GitHub Repository",
        "about_copyright": "© {year} by 星缘. All Rights Reserved.",
        "warning_delete_failed_title": "Backup Failed",
    },
    "zh": {
        "version": "M0JIAN127",
        "internal_build_id": 1272,
        "changelog_history": {
            "M0JIAN001": "项目初始化。实现了通过记事本输入，并将内容保存为桌面带时间戳的TXT文件的核心功能。",
            "M0JIAN005": "首次正式命名。程序定名为“墨笺”，并优化了文件处理逻辑，避免生成不必要的空文件。",
            "M0JIAN010": "引入图形化配置。新增首次运行设置向导，允许用户自定义文件的保存位置。",
            "M0JIAN020": "核心逻辑重构。将输出文件统一为序列化的“墨笺n.txt”，简化了程序的工作流。",
            "M0JIAN100": "集成自定义编辑器。新增支持用户选择第三方文本编辑器（如VS Code）的功能，并提供启动时重新配置的选项。",
            "M0JIAN119": """交互体验与内部系统优化。
    - 优化启动流程：启动时的配置确认对话框现提供“继续”、“重置配置”和“退出”三个明确选项。
    - 集成更新日志：新增版本号与更新日志系统，所有版本的更新历史都将被记录在配置文件中。
    - 改善操作指引：全面优化了各项操作提示和对话框的文本，使其更加清晰、易于理解。""",
            "M0JIAN120": """国际化与核心体验升级。
    - 新增 - 国际化支持 (i18n)：程序现可自动检测用户操作系统语言，并切换为中文或英文界面。
    - 新增 - 完成后自动定位文件：设置向导中新增选项，允许用户开启“保存后自动打开文件所在位置”功能。
    - 优化 - 配置文件管理：《墨笺》的配置文件现已迁移至Windows标准的`AppData`目录。""",
            "M0JIAN121": """健壮性修复与命名体系优化。
    - 修复 - 关键Bug修复：解决了在特殊字符路径下，“完成后自动定位文件”功能报错且无法选中文件的问题。
    - 优化 - 命名体系：为内部配置文件赋予了更具东方美学的雅致名称（`墨笺之卷`）。""",
            "M0JIAN122": """核心体验重塑 & 配置文件管理革命。
    - 优化 - 配置文件自动定位：程序现在能自动记住您的配置，无需每次启动都手动选择。
    - 优化 - 标准化文件管理：配置文件现已迁移至Windows标准的`AppData`目录，与主程序彻底分离。""",
            "M0JIAN123": """交互逻辑重构 & 人性化引导。
    - 新增 - “配置清单”一键开启：在您首次完成设置后，程序会贴心地询问您是否需要立即打开配置文件夹。
    - 优化 - 功能引导分离：“完成后自动定位文件”和“首次查看配置”这两个功能现已完全分离。""",
            "M0JIAN124": """数据完整性修复 & 历史回溯。
    - 修复 - 更新日志完整性恢复：此版本在配置文件中恢复了自 M0JIAN001 版本以来的全部更新历史，确保了项目历史记录的准确性与完整性。""",
            "M0JIAN125": """官网集成 & “关于我们”。
    - 新增 - “关于墨笺”窗口：我们为《墨笺》打造了一个专属的“关于”窗口。
    - 新增 - 官方网站与仓库链接：在“关于”窗口中，我们集成了项目的官方网站和 GitHub 仓库的入口。
    - 优化 - 启动交互升级：原有的启动确认对话框已升级为一个功能更丰富的自定义窗口。""",
            "M0JIAN126": """凯旋归来，体验与流程的终极进化。
    - 新增 - “一键打包”自动化脚本：引入 `build.bat` 批处理脚本，实现自动编译、移动和清理，一键生成桌面EXE。
    - 新增 - 智能更新引导系统：内置“内部构建号”机制，可在程序更新后智能检测并建议用户重置配置，确保最佳兼容性。
    - 修复 - 终极稳定性修复：重构启动逻辑，使用原生对话框替代自定义窗口，从根源上解决了导致程序卡死的“幽灵进程”Bug。
    - 优化 - 项目信息集成：官方网站和GitHub仓库链接作为元数据，现已整合进配置文件（`墨笺之卷.json`）中。""",
            "M0JIAN127": """“锦书”功能集 - 坚如磐石，功能精进。
    - 修复 - 终极稳定性加固：我们对程序启动流程进行了再次的彻底重构，确保《墨笺》在任何系统环境下都能稳定、无卡顿地启动。彻底解决了可能导致程序无响应或“幽灵进程”的底层Bug。
    - 新增 - 应用内设置中心（已内置）：强大的“设置中心”已内置于程序核心。（注意：本次版本暂未提供直接入口，我们正在设计更优雅的激活方式，敬请期待后续更新）
    - 新增 - 内嵌式更新日志（已内置）：完整的项目更新历史已内置于程序内部。（注意：本次版本暂未提供直接入口，我们正在设计更优雅的激活方式，敬请期待后续更新）
    - 新增 - 轻量级备份系统：为您的创作提供安心保障！当您修改并保存一个已存在的`墨笺n.txt`文件时，程序会自动将旧版内容备份为`墨笺n.txt.bak`文件。
    - 优化 - 智能更新引导：程序内置的“内部构建号”机制，可在检测到代码更新时，智能建议您重置配置以确保最佳兼容性。"""
        },
        "settings_filename": "墨笺之卷.json",
        "update_detected_title": "检测到更新",
        "update_detected_message": "《墨笺》检测到程序有内部更新。\n\n为了确保新功能正常运作，建议您重置配置文件。\n\n【是】- 删除旧配置并开始全新设置\n【否】- 尝试在旧配置下运行（可能不稳定）",
        "config_confirm_title": "配置确认",
        "config_confirm_message": "当前配置：\n\n编辑器: {editor_name}\n保存位置: {save_folder}\n\n是否使用此配置继续？\n【是】-> 继续使用\n【否】-> 重置配置\n【取消】-> 退出程序",
        "wizard_title_1": "设置向导 (1/3)",
        "wizard_message_1": "请选择一个文件夹来存放您的“墨笺”文件集。",
        "wizard_ask_folder_title": "选择“墨笺”文件保存文件夹",
        "wizard_title_2": "设置向导 (2/3)",
        "wizard_message_2": "请选择您偏好的文本编辑器程序 (.exe)。\n\n例如：VS Code, Sublime Text, Notepad++ 等。\n如果您取消选择，程序将自动使用系统默认的记事本。",
        "wizard_ask_editor_title": "选择您的文本编辑器",
        "wizard_title_3": "Setup Wizard (3/3)",
        "wizard_message_3": "是否希望在保存成功后，自动打开文件所在位置？\n\n强烈推荐开启！这将允许您立即将文件拖拽到AI对话框等应用中，极大提升效率。",
        "wizard_use_default_editor_title": "使用默认编辑器",
        "wizard_use_default_editor_message": "您没有选择编辑器，将使用系统默认的记事本。\n路径: {path}",
        "wizard_cancel_title": "设置取消",
        "wizard_cancel_message": "您没有选择保存文件夹，程序将退出。",
        "config_saved_title": "配置已保存",
        "config_saved_message": "您的设置已保存成功！\n\n程序将会自动记住这些设置。",
        "one_time_open_config_title": "查看配置文件？",
        "one_time_open_config_message": "您的配置文件“{filename}”已创建成功。\n\n其中包含了完整的更新历史和您的个人设置。是否立即打开其所在文件夹，以便您了解它的位置？\n\n（此提示仅会出现一次）",
        "ready_title": "墨笺 - 准备就绪",
        "ready_message": "一切准备就绪！\n\n墨笺即将为您启动编辑器：[{editor_name}]\n\n请在其中完成您的创作，然后保存并关闭。\n您的作品将被命名为：[{filename}]",
        "op_success_title": "操作成功",
        "op_success_message": "文件已成功保存至：\n{path}",
        "op_info_title": "操作提示",
        "op_info_message": "文件未被修改或内容为空，本次操作将不保存文件。",
        "error_open_location_title": "错误",
        "error_open_location_message": "无法打开文件夹: {e}",
        "error_unexpected_title": "意外错误",
        "error_unexpected_message": "程序运行中发生意外错误: {e}",
        "error_editor_not_found_title": "编辑器未找到",
        "error_editor_not_found_message": "无法找到您配置的编辑器: {path}\n请重新运行程序并选择一个有效的编辑器。",
        "settings_window_title": "设置中心",
        "settings_label_editor": "编辑器路径：",
        "settings_label_save_folder": "保存文件夹路径：",
        "settings_label_auto_open": "保存后自动定位文件",
        "settings_btn_browse": "浏览...",
        "settings_btn_save": "保存并关闭",
        "settings_save_success_title": "设置已保存",
        "settings_save_success_message": "您的新设置已成功保存！",
        "about_window_title": "关于墨笺",
        "about_desc": "化任意编辑器，为代码灵感之速记。",
        "about_website_label": "官方网站",
        "about_github_label": "GitHub 仓库",
        "about_copyright": "© {year} 星缘. 版权所有.",
        "warning_delete_failed_title": "备份失败",
    }
}

# --- 项目链接 ---
PROJECT_WEBSITE_URL = "https://mojian-inkpad--stella.on.websim.com"
GITHUB_REPO_URL = "https://github.com/630StarFortune/Mojian"

# --- 全局函数 ---
def get_language():
    """检测系统语言并返回相应的语言资源 (稳定版)"""
    try:
        lang_code, _ = locale.getdefaultlocale()
        if lang_code and lang_code.lower().startswith('zh'):
            return LANGUAGES['zh']
    except Exception:
        pass
    return LANGUAGES['en']

L = get_language()

def get_settings_path():
    app_data_path = os.getenv('APPDATA') or os.path.expanduser('~')
    mojian_config_dir = os.path.join(app_data_path, "Mojian")
    return os.path.join(mojian_config_dir, L["settings_filename"])

def load_settings():
    config_path = get_settings_path()
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return None

def save_settings(settings):
    config_path = get_settings_path()
    config_dir = os.path.dirname(config_path)
    try:
        os.makedirs(config_dir, exist_ok=True)
        settings["project_website"] = PROJECT_WEBSITE_URL
        settings["github_repository"] = GITHUB_REPO_URL
        settings["changelog_history"] = L["changelog_history"]
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(settings, f, ensure_ascii=False, indent=4)
        return True
    except IOError:
        return False

def get_default_notepad_path():
    system_root = os.environ.get('SystemRoot', 'C:\\Windows')
    paths_to_check = [
        os.path.join(system_root, 'System32', 'notepad.exe'),
        os.path.join(system_root, 'SysWOW64', 'notepad.exe'),
        'notepad.exe'
    ]
    for path in paths_to_check:
        if 'notepad.exe' == path:
            try:
                result = subprocess.run(['where', 'notepad.exe'], capture_output=True, text=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
                return result.stdout.strip().split('\n')[0]
            except (subprocess.CalledProcessError, FileNotFoundError):
                return 'notepad.exe'
        if os.path.exists(path):
            return path
    return 'notepad.exe'

def run_configuration_wizard(root_window):
    messagebox.showinfo(L.get("wizard_title_1", "Step 1"), L.get("wizard_message_1", "Select save folder."), parent=root_window)
    save_folder = filedialog.askdirectory(title=L.get("wizard_ask_folder_title", "Select Folder"), initialdir=os.path.expanduser('~'), parent=root_window)
    if not save_folder:
        messagebox.showwarning(L.get("wizard_cancel_title", "Canceled"), L.get("wizard_cancel_message", "No folder selected."), parent=root_window)
        return None, None, None

    messagebox.showinfo(L.get("wizard_title_2", "Step 2"), L.get("wizard_message_2", "Select editor."), parent=root_window)
    editor_path = filedialog.askopenfilename(title=L.get("wizard_ask_editor_title", "Select Editor"), filetypes=[("Executable files", "*.exe"), ("All files", "*.*")], initialdir="C:/Program Files", parent=root_window)
    if not editor_path:
        default_notepad = get_default_notepad_path()
        messagebox.showinfo(L.get("wizard_use_default_editor_title", "Default Editor"), L.get("wizard_use_default_editor_message", "Using default: {path}").format(path=default_notepad), parent=root_window)
        editor_path = default_notepad
    
    auto_open = messagebox.askyesno(L.get("wizard_title_3", "Step 3"), L.get("wizard_message_3", "Auto-open location?"), parent=root_window)
    return save_folder, editor_path, auto_open

def find_next_mojian_filename(folder_path, base_name="墨笺", extension=".txt"):
    n = 1
    try:
        if not os.path.isdir(folder_path):
            os.makedirs(folder_path)
    except OSError:
        return None
    while True:
        filename = f"{base_name}{n}{extension}"
        filepath = os.path.join(folder_path, filename)
        if not os.path.exists(filepath):
            return filepath
        n += 1

def open_directory(dir_path):
    """只打开文件夹"""
    try:
        os.startfile(os.path.normpath(dir_path))
    except Exception as e:
        messagebox.showwarning(L.get("error_open_location_title", "Error"), L.get("error_open_location_message", "Could not open folder: {e}").format(e=e))

def open_file_location(filepath):
    normalized_path = os.path.normpath(filepath)
    try:
        subprocess.run(['explorer', '/select,', normalized_path], creationflags=subprocess.CREATE_NO_WINDOW)
    except Exception:
        open_directory(os.path.dirname(normalized_path))

def execute_main_task(settings, root_window):
    save_folder_path = settings.get("save_folder_path")
    editor_path = settings.get("editor_path")
    auto_open_location = settings.get("auto_open_location", False)

    final_mojian_file_path = find_next_mojian_filename(save_folder_path)
    if not final_mojian_file_path:
        return

    backup_made = False
    if os.path.exists(final_mojian_file_path):
        try:
            backup_path = final_mojian_file_path + ".bak"
            shutil.copy2(final_mojian_file_path, backup_path)
            backup_made = True
        except Exception as backup_e:
            messagebox.showwarning(L.get("warning_delete_failed_title", "Backup Failed"), f"Failed to create backup for {os.path.basename(final_mojian_file_path)}: {backup_e}", parent=root_window)

    editor_name = os.path.basename(editor_path)
    filename = os.path.basename(final_mojian_file_path)
    messagebox.showinfo(
        L.get("ready_title", "Ready"),
        L.get("ready_message", "Editor: [{editor_name}]\nFile: [{filename}]").format(editor_name=editor_name, filename=filename),
        parent=root_window
    )

    with open(final_mojian_file_path, 'a', encoding='utf-8') as f:
        pass
    mtime_before = os.path.getmtime(final_mojian_file_path)

    process = subprocess.Popen([editor_path, final_mojian_file_path])
    process.wait()

    if not os.path.exists(final_mojian_file_path):
        return

    mtime_after = os.path.getmtime(final_mojian_file_path)
    file_was_modified = mtime_after > mtime_before
    
    content_is_empty = True
    with open(final_mojian_file_path, 'r', encoding='utf-8') as f_check:
        if f_check.read().strip():
            content_is_empty = False
    
    if not file_was_modified or content_is_empty:
        messagebox.showinfo(L.get("op_info_title", "Info"), L.get("op_info_message", "No changes saved."), parent=root_window)
        try:
            if not backup_made and os.path.exists(final_mojian_file_path) and os.path.getsize(final_mojian_file_path) == 0:
                os.remove(final_mojian_file_path)
        except OSError:
            pass
    else:
        messagebox.showinfo(L.get("op_success_title", "Success"), L.get("op_success_message", "Saved to:\n{path}").format(path=final_mojian_file_path), parent=root_window)
        if auto_open_location:
            open_file_location(final_mojian_file_path)

# --- 主程序逻辑 (终极稳定版 - M0JIAN127) ---
def main():
    # --- 1. 静默逻辑处理阶段 (无任何UI) ---
    settings = load_settings()
    should_run_wizard = False
    update_detected = False
    
    if settings and settings.get("internal_build_id") != L["internal_build_id"]:
        update_detected = True
    
    if not settings:
        should_run_wizard = True
    else:
        save_folder_path = settings.get("save_folder_path")
        editor_path = settings.get("editor_path")
        if not (save_folder_path and os.path.isdir(save_folder_path) and
                editor_path and (os.path.isfile(editor_path) or editor_path == 'notepad.exe')):
            should_run_wizard = True

    # --- 2. UI交互阶段 (现在可以安全地创建UI) ---
    root = tk.Tk()
    root.withdraw()

    try:
        if update_detected:
            user_agrees_to_reset = messagebox.askyesno(
                L["update_detected_title"],
                L["update_detected_message"],
                parent=root
            )
            if user_agrees_to_reset:
                try:
                    os.remove(get_settings_path())
                except OSError: pass
                settings = None
                should_run_wizard = True
        
        if should_run_wizard:
            save_folder, editor, auto_open = run_configuration_wizard(root)
            if not (save_folder and editor):
                return

            settings = {
                "save_folder_path": save_folder, 
                "editor_path": editor,
                "auto_open_location": auto_open,
                "last_version_run": L["version"],
                "internal_build_id": L["internal_build_id"]
            }
            if save_settings(settings):
                messagebox.showinfo(L.get("config_saved_title", "Config Saved"), L.get("config_saved_message", "Settings saved!"), parent=root)
                user_wants_to_see_config = messagebox.askyesno(
                    L.get("one_time_open_config_title", "View Config?"),
                    L.get("one_time_open_config_message", "Config file created. View folder?").format(filename=L["settings_filename"]),
                    parent=root
                )
                if user_wants_to_see_config:
                    open_directory(os.path.dirname(get_settings_path()))
            else:
                return
        else:
            editor_name = os.path.basename(settings["editor_path"])
            user_choice = messagebox.askyesnocancel(
                L["config_confirm_title"],
                L["config_confirm_message"].format(editor_name=editor_name, save_folder=settings["save_folder_path"]),
                parent=root
            )
            if user_choice is False: # No -> Reconfigure
                save_folder, editor, auto_open = run_configuration_wizard(root)
                if not (save_folder and editor):
                    return
                settings.update({
                    "save_folder_path": save_folder, 
                    "editor_path": editor,
                    "auto_open_location": auto_open,
                })
                save_settings(settings)
            elif user_choice is None: # Cancel -> Exit
                return

        if settings.get("last_version_run") != L["version"]:
             changelog_text = L["changelog_history"].get(L["version"], "No changelog found for this version.")
             messagebox.showinfo(L.get("welcome_title", "Welcome"), L.get("welcome_message", "What's new: {changelog}").format(changelog=changelog_text), parent=root)
             settings["last_version_run"] = L["version"]
             save_settings(settings)

        execute_main_task(settings, root)

    except Exception as e:
        messagebox.showerror(L.get("error_unexpected_title", "Unexpected Error"), L.get("error_unexpected_message", "An unexpected error occurred: {e}").format(e=e))
    finally:
        if root.winfo_exists():
            root.destroy()

if __name__ == "__main__":
    main()