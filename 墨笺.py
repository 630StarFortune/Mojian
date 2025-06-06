import subprocess
import os
import sys
import json
import locale
import webbrowser
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

# --- i18n 语言资源 ---
LANGUAGES = {
    "en": {
        "version": "M0JIAN125",
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
    - New - 'About Mojian' Window: A dedicated 'About' window has been created, accessible at startup.
    - New - Official Website & Repository Links: The 'About' window provides direct links to the official project website and its GitHub repository.
    - Improved - Startup Interaction: The startup confirmation has been upgraded to a custom dialog, elegantly integrating the 'Continue', 'Reconfigure', and new 'About' options."""
        },
        "settings_filename": "Mojian_Scroll.json",
        "welcome_title": "Welcome to Mojian v{version}",
        "welcome_message": "What's new in this version:\n\n{changelog}",
        "startup_dialog_title": "Welcome Back",
        "startup_dialog_message": "Current Settings:\n\nEditor: {editor_name}\nSave Location: {save_folder}",
        "startup_btn_continue": "Continue",
        "startup_btn_reconfigure": "Reconfigure",
        "startup_btn_about": "About Mojian",
        "about_window_title": "About Mojian",
        "about_desc": "Transform any editor into a high-speed scratchpad for your ideas.",
        "about_website_label": "Official Website",
        "about_github_label": "GitHub Repository",
        "about_copyright": "© {year} by 星缘. All Rights Reserved.",
        "about_btn_close": "Close",
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
        "error_open_location_message": "Could not open folder: {e}"
    },
    "zh": {
        "version": "M0JIAN125",
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
    - 新增 - “关于墨笺”窗口：我们为《墨笺》打造了一个专属的“关于”窗口。现在，您可以在程序启动时，通过一个全新的选项，随时打开它。
    - 新增 - 官方网站与仓库链接：在“关于”窗口中，我们集成了项目的官方网站和 GitHub 仓库的入口。只需轻轻一点，即可深入了解《墨笺》的设计理念或参与到开源共创中来。
    - 优化 - 启动交互升级：原有的启动确认对话框已升级为一个功能更丰富的自定义窗口，将“继续使用”、“重置配置”和新增的“关于墨笺”功能优雅地整合在一起。"""
        },
        "settings_filename": "墨笺之卷.json",
        "welcome_title": "欢迎使用 墨笺 v{version}",
        "welcome_message": "本次更新内容：\n\n{changelog}",
        "startup_dialog_title": "欢迎回来",
        "startup_dialog_message": "当前配置：\n\n编辑器: {editor_name}\n保存位置: {save_folder}",
        "startup_btn_continue": "继续使用",
        "startup_btn_reconfigure": "重置配置",
        "startup_btn_about": "关于墨笺",
        "about_window_title": "关于墨笺",
        "about_desc": "化任意编辑器，为代码灵感之速记。",
        "about_website_label": "官方网站",
        "about_github_label": "GitHub 仓库",
        "about_copyright": "© {year} 星缘. 版权所有.",
        "about_btn_close": "关闭",
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
        "error_open_location_message": "无法打开文件夹: {e}"
    }
}

# --- 项目链接 ---
PROJECT_WEBSITE_URL = "https://mojian-inkpad--stella.on.websim.com"
GITHUB_REPO_URL = "https://github.com/630StarFortune/Mojian"

# --- 全局函数 ---
def get_language():
    """检测系统语言并返回相应的语言资源"""
    try:
        lang_code, _ = locale.getdefaultlocale()
        if lang_code and lang_code.lower().startswith('zh'):
            return LANGUAGES['zh']
    except Exception:
        pass
    return LANGUAGES['en']

L = get_language()

def get_settings_path():
    """获取配置文件的标准路径 (AppData/Roaming/Mojian)"""
    app_data_path = os.getenv('APPDATA')
    if not app_data_path:
        app_data_path = os.path.expanduser('~')
    mojian_config_dir = os.path.join(app_data_path, "Mojian")
    return os.path.join(mojian_config_dir, L["settings_filename"])

def load_settings():
    """从标准路径加载设置"""
    config_path = get_settings_path()
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return None

def save_settings(settings):
    """保存设置到标准路径"""
    config_path = get_settings_path()
    config_dir = os.path.dirname(config_path)
    try:
        os.makedirs(config_dir, exist_ok=True)
        settings["changelog_history"] = L["changelog_history"]
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(settings, f, ensure_ascii=False, indent=4)
        return True
    except IOError:
        return False

def open_link(url):
    """在新浏览器标签页中打开链接"""
    webbrowser.open_new_tab(url)

def show_about_window(parent):
    """显示“关于”窗口"""
    about_win = tk.Toplevel(parent)
    about_win.title(L["about_window_title"])
    about_win.geometry("400x250")
    about_win.resizable(False, False)
    about_win.transient(parent)
    about_win.grab_set()

    parent.update_idletasks()
    x = parent.winfo_x() + (parent.winfo_width() // 2) - (400 // 2)
    y = parent.winfo_y() + (parent.winfo_height() // 2) - (250 // 2)
    about_win.geometry(f"+{x}+{y}")

    main_frame = tk.Frame(about_win, padx=20, pady=20)
    main_frame.pack(expand=True, fill="both")

    tk.Label(main_frame, text="墨笺", font=("Noto Serif SC", 24, "bold")).pack(pady=(0, 5))
    tk.Label(main_frame, text=L["about_desc"], font=("Noto Sans SC", 10)).pack(pady=(0, 20))

    website_label = tk.Label(main_frame, text=L["about_website_label"], fg="blue", cursor="hand2", font=("Noto Sans SC", 10, "underline"))
    website_label.pack()
    website_label.bind("<Button-1>", lambda e: open_link(PROJECT_WEBSITE_URL))

    github_label = tk.Label(main_frame, text=L["about_github_label"], fg="blue", cursor="hand2", font=("Noto Sans SC", 10, "underline"))
    github_label.pack(pady=5)
    github_label.bind("<Button-1>", lambda e: open_link(GITHUB_REPO_URL))

    tk.Label(main_frame, text=L["about_copyright"].format(year=datetime.now().year), font=("Noto Sans SC", 8), fg="grey").pack(side="bottom", pady=(10, 0))
    
    about_win.wait_window()

def ask_startup_action(parent, editor_name, save_folder):
    """显示自定义的启动确认对话框"""
    dialog = tk.Toplevel(parent)
    dialog.title(L["startup_dialog_title"])
    dialog.resizable(False, False)
    dialog.transient(parent)
    
    result = "cancel"

    def set_result(choice):
        nonlocal result
        result = choice
        dialog.destroy()

    main_frame = tk.Frame(dialog, padx=20, pady=15)
    main_frame.pack()

    message = L["startup_dialog_message"].format(editor_name=editor_name, save_folder=save_folder)
    tk.Label(main_frame, text=message, justify="left").pack(pady=(0, 15))

    button_frame = tk.Frame(main_frame)
    button_frame.pack(fill="x")

    continue_btn = tk.Button(button_frame, text=L["startup_btn_continue"], command=lambda: set_result("continue"), default="active")
    continue_btn.pack(side="left", expand=True, padx=5)
    continue_btn.focus_set()

    reconfigure_btn = tk.Button(button_frame, text=L["startup_btn_reconfigure"], command=lambda: set_result("reconfigure"))
    reconfigure_btn.pack(side="left", expand=True, padx=5)

    about_btn = tk.Button(button_frame, text=L["startup_btn_about"], command=lambda: set_result("about"))
    about_btn.pack(side="left", expand=True, padx=5)

    dialog.protocol("WM_DELETE_WINDOW", lambda: set_result("cancel"))
    dialog.wait_window()
    return result

def get_default_notepad_path():
    """找到系统默认的记事本路径"""
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
    """运行设置向导"""
    messagebox.showinfo(L["wizard_title_1"], L["wizard_message_1"], parent=root_window)
    save_folder = filedialog.askdirectory(title=L["wizard_ask_folder_title"], initialdir=os.path.expanduser('~'), parent=root_window)
    if not save_folder:
        messagebox.showwarning(L["wizard_cancel_title"], L["wizard_cancel_message"], parent=root_window)
        return None, None, None

    messagebox.showinfo(L["wizard_title_2"], L["wizard_message_2"], parent=root_window)
    editor_path = filedialog.askopenfilename(title=L["wizard_ask_editor_title"], filetypes=[("Executable files", "*.exe"), ("All files", "*.*")], initialdir="C:/Program Files", parent=root_window)
    if not editor_path:
        default_notepad = get_default_notepad_path()
        messagebox.showinfo(L["wizard_use_default_editor_title"], L["wizard_use_default_editor_message"].format(path=default_notepad), parent=root_window)
        editor_path = default_notepad
    
    auto_open = messagebox.askyesno(L["wizard_title_3"], L["wizard_message_3"], parent=root_window)
    return save_folder, editor_path, auto_open

def find_next_mojian_filename(folder_path, base_name="墨笺", extension=".txt"):
    """查找下一个可用的文件名"""
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

def open_file_location(filepath):
    """打开文件所在位置并选中文件"""
    normalized_path = os.path.normpath(filepath)
    try:
        subprocess.run(['explorer', '/select,', normalized_path], creationflags=subprocess.CREATE_NO_WINDOW)
    except Exception as e:
        open_directory(os.path.dirname(normalized_path), e)

def open_directory(dir_path, original_error=None):
    """只打开文件夹"""
    try:
        os.startfile(os.path.normpath(dir_path))
    except Exception as e:
        error_to_show = original_error if original_error else e
        messagebox.showwarning(L["error_open_location_title"], L["error_open_location_message"].format(e=error_to_show))

# --- 主程序逻辑 ---
def main():
    root = tk.Tk()
    root.withdraw()

    try:
        while True:
            settings = load_settings()
            
            should_reconfigure = False
            if not settings:
                should_reconfigure = True
            else:
                last_version_run = settings.get("last_version_run")
                if last_version_run != L["version"]:
                    changelog_text = L["changelog_history"].get(L["version"], "No changelog found for this version.")
                    messagebox.showinfo(L["welcome_title"].format(version=L["version"]), L["welcome_message"].format(changelog=changelog_text), parent=root)
                    settings["last_version_run"] = L["version"]
                
                save_folder_path = settings.get("save_folder_path")
                editor_path = settings.get("editor_path")

                config_is_valid = save_folder_path and os.path.isdir(save_folder_path) and \
                                  editor_path and (os.path.isfile(editor_path) or editor_path == 'notepad.exe')
                
                if not config_is_valid:
                    should_reconfigure = True
                else:
                    editor_name = os.path.basename(editor_path)
                    user_choice = ask_startup_action(root, editor_name, save_folder_path)
                    
                    if user_choice == "continue":
                        should_reconfigure = False
                    elif user_choice == "reconfigure":
                        should_reconfigure = True
                    elif user_choice == "about":
                        show_about_window(root)
                        continue
                    else:
                        return

            if should_reconfigure:
                save_folder_path, editor_path, auto_open = run_configuration_wizard(root)
                if not (save_folder_path and editor_path):
                    return

                settings = {
                    "save_folder_path": save_folder_path, 
                    "editor_path": editor_path,
                    "auto_open_location": auto_open,
                    "last_version_run": L["version"]
                }
                if save_settings(settings):
                    messagebox.showinfo(L["config_saved_title"], L["config_saved_message"], parent=root)
                    user_wants_to_see_config = messagebox.askyesno(
                        L["one_time_open_config_title"],
                        L["one_time_open_config_message"].format(filename=L["settings_filename"]),
                        parent=root
                    )
                    if user_wants_to_see_config:
                        open_directory(os.path.dirname(get_settings_path()))
                else:
                    return
            
            save_folder_path = settings.get("save_folder_path")
            editor_path = settings.get("editor_path")
            auto_open_location = settings.get("auto_open_location", False)

            final_mojian_file_path = find_next_mojian_filename(save_folder_path)
            if not final_mojian_file_path:
                return

            editor_name = os.path.basename(editor_path)
            filename = os.path.basename(final_mojian_file_path)
            messagebox.showinfo(
                L["ready_title"],
                L["ready_message"].format(editor_name=editor_name, filename=filename),
                parent=root
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
                messagebox.showinfo(L["op_info_title"], L["op_info_message"], parent=root)
                try:
                    os.remove(final_mojian_file_path)
                except OSError:
                    pass
            else:
                messagebox.showinfo(L["op_success_title"], L["op_success_message"].format(path=final_mojian_file_path), parent=root)
                if auto_open_location:
                    open_file_location(final_mojian_file_path)
            
            break

    except Exception as e:
        messagebox.showerror("Unexpected Error", f"An unexpected error occurred: {e}")
    finally:
        root.destroy()

if __name__ == "__main__":
    main()