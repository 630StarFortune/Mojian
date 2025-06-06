import subprocess
import os
import sys
import json
import locale
import tkinter as tk
from tkinter import filedialog, messagebox

# --- i18n 语言资源 ---
LANGUAGES = {
    "en": {
        "version": "M0JIAN121",
        "changelog_history": {
            "M0JIAN120": """Internationalization & Core Experience Upgrade.
    - New - Internationalization (i18n) Support: The program now auto-detects the OS language to switch between Chinese and English interfaces.
    - New - Auto-locate File on Completion: A new option in the setup wizard to automatically open the file's location after saving, boosting workflow efficiency.
    - Improved - Configuration File Management: The settings file is now stored in your designated 'Mojian' folder, completely separate from the EXE.
    - Improved - Startup Flow: The confirmation dialog now defaults to 'No', allowing frequent users to press Enter and proceed immediately.
    - Improved - UI Prompts: All user-facing text has been refined for better clarity and timing.""",
            "M0JIAN121": """Robustness Fix & Naming Refinement.
    - Fix - Critical Bug Fix: Resolved an issue where 'Auto-locate File' would fail on systems with special characters (e.g., apostrophes) in the user's folder path. The feature is now stable across all environments.
    - Improved - Naming Scheme: Internal configuration files have been given more elegant and thematic names to enhance the project's overall design and detail."
"""
        },
        "pointer_filename": "Mojian_Guide.mjp",
        "settings_filename": "Mojian_Scroll.json",
        "welcome_title": "Welcome to Mojian v{version}",
        "welcome_message": "What's new in this version:\n\n{changelog}",
        "config_confirm_title": "Configuration Confirmation",
        "config_confirm_message": "Current Settings:\n\nEditor: {editor_name}\nSave Location: {save_folder}\n\nWould you like to change these settings?\n[Yes] -> Reset Configuration\n[No] -> Continue with current settings\n[Cancel] -> Exit Program",
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
        "config_saved_message": "Your settings have been saved successfully!\n\nYou can find the '{settings_filename}' file in your designated save folder to view or modify settings. The complete update history is also recorded there.",
        "ready_title": "Mojian - Ready to Go",
        "ready_message": "Everything is set!\n\nMojian is about to launch your editor: [{editor_name}]\n\nPlease complete your work, then save and close it.\nYour creation will be named: [{filename}]",
        "op_success_title": "Operation Successful",
        "op_success_message": "File has been successfully saved to:\n{path}",
        "op_info_title": "Operation Note",
        "op_info_message": "The file was not modified or its content is empty. This operation will not save a file.",
        "error_open_location_title": "Error",
        "error_open_location_message": "Could not open file location: {e}",
        "load_config_title": "Load Configuration",
        "load_config_message": "Do you want to load an existing '{settings_filename}' file?\n\n[Yes] -> Manually select the settings file\n[No] -> Start a fresh setup"
    },
    "zh": {
        "version": "M0JIAN121",
        "changelog_history": {
            "M0JIAN120": """国际化与核心体验升级。
    - 新增 - 国际化支持 (i18n)：程序现可自动检测用户操作系统语言，并切换为中文或英文界面。
    - 新增 - 完成后自动定位文件：设置向导中新增选项，允许用户开启“保存后自动打开文件所在位置”功能，提升工作流效率。
    - 优化 - 配置文件管理：`Mojian_settings.json` 文件现在将保存在您指定的“墨笺”文件夹中，与主程序分离。
    - 优化 - 启动流程：启动确认对话框的默认焦点已设为“否”，方便高频用户直接按回车键继续。
    - 优化 - 界面提示：全面优化了程序内的提示文本，使其在时序和表达上更加精准、亲切。""",
            "M0JIAN121": """健壮性修复与命名体系优化。
    - 修复 - 关键Bug修复：解决了在Windows用户名或路径包含特殊字符（如单引号“'”）时，“完成后自动定位文件”功能报错且无法选中文件的问题。现在该功能在所有路径下都能稳定运行。
    - 优化 - 命名体系：为配置文件赋予了更具东方美学的雅致名称（墨笺之引、墨笺之卷），提升了项目的整体感与设计细节。"""
        },
        "pointer_filename": "墨笺之引.mjp",
        "settings_filename": "墨笺之卷.json",
        "welcome_title": "欢迎使用 墨笺 v{version}",
        "welcome_message": "本次更新内容：\n\n{changelog}",
        "config_confirm_title": "配置确认",
        "config_confirm_message": "当前配置：\n\n编辑器: {editor_name}\n保存位置: {save_folder}\n\n是否要修改当前配置？\n【是】-> 重置配置\n【否】-> 使用当前配置继续\n【取消】-> 退出程序",
        "wizard_title_1": "设置向导 (1/3)",
        "wizard_message_1": "请选择一个文件夹来存放您的“墨笺”文件集。",
        "wizard_ask_folder_title": "选择“墨笺”文件保存文件夹",
        "wizard_title_2": "设置向导 (2/3)",
        "wizard_message_2": "请选择您偏好的文本编辑器程序 (.exe)。\n\n例如：VS Code, Sublime Text, Notepad++ 等。\n如果您取消选择，程序将自动使用系统默认的记事本。",
        "wizard_ask_editor_title": "选择您的文本编辑器",
        "wizard_title_3": "设置向导 (3/3)",
        "wizard_message_3": "是否希望在保存成功后，自动打开文件所在位置？\n\n强烈推荐开启！这将允许您立即将文件拖拽到AI对话框等应用中，极大提升效率。",
        "wizard_use_default_editor_title": "使用默认编辑器",
        "wizard_use_default_editor_message": "您没有选择编辑器，将使用系统默认的记事本。\n路径: {path}",
        "wizard_cancel_title": "设置取消",
        "wizard_cancel_message": "您没有选择保存文件夹，程序将退出。",
        "config_saved_title": "配置已保存",
        "config_saved_message": "您的设置已保存成功！\n\n您可以在您指定的保存文件夹中找到“{settings_filename}”文件，随时查看或修改配置。该文件也包含了完整的更新历史记录。",
        "ready_title": "墨笺 - 准备就绪",
        "ready_message": "一切准备就绪！\n\n墨笺即将为您启动编辑器：[{editor_name}]\n\n请在其中完成您的创作，然后保存并关闭。\n您的作品将被命名为：[{filename}]",
        "op_success_title": "操作成功",
        "op_success_message": "文件已成功保存至：\n{path}",
        "op_info_title": "操作提示",
        "op_info_message": "文件未被修改或内容为空，本次操作将不保存文件。",
        "error_open_location_title": "错误",
        "error_open_location_message": "无法打开文件位置: {e}",
        "load_config_title": "加载配置",
        "load_config_message": "是否要加载一个已存在的“{settings_filename}”配置文件？\n\n【是】-> 手动选择配置文件\n【否】-> 开始全新设置"
    }
}

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

def get_script_dir():
    """获取脚本（或EXE）所在的目录"""
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))

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

def load_settings(root_window):
    """加载设置。由于配置文件位置不固定，需要引导用户。"""
    pointer_path = os.path.join(get_script_dir(), L["pointer_filename"])
    if os.path.exists(pointer_path):
        with open(pointer_path, 'r', encoding='utf-8') as f:
            config_path = f.read().strip()
            if os.path.exists(config_path):
                try:
                    with open(config_path, 'r', encoding='utf-8') as sf:
                        return json.load(sf)
                except (json.JSONDecodeError, IOError):
                    pass

    choice = messagebox.askyesno(L["load_config_title"].format(settings_filename=L["settings_filename"]), L["load_config_message"].format(settings_filename=L["settings_filename"]), parent=root_window)
    if choice:
        config_path = filedialog.askopenfilename(title=f"请选择您的 {L['settings_filename']} 文件", filetypes=[("JSON files", "*.json")], parent=root_window)
        if config_path and os.path.basename(config_path) == L["settings_filename"]:
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    settings = json.load(f)
                    with open(pointer_path, 'w', encoding='utf-8') as pf:
                        pf.write(config_path)
                    return settings
            except (json.JSONDecodeError, IOError) as e:
                messagebox.showerror(L["error_config_title"], L["error_config_message"].format(file=config_path, e=e), parent=root_window)
    return None

def save_settings(settings, save_folder_path):
    """保存设置到用户指定的文件夹"""
    settings_path = os.path.join(save_folder_path, L["settings_filename"])
    settings["changelog_history"] = L["changelog_history"]
    try:
        with open(settings_path, 'w', encoding='utf-8') as f:
            json.dump(settings, f, ensure_ascii=False, indent=4)
        pointer_path = os.path.join(get_script_dir(), L["pointer_filename"])
        with open(pointer_path, 'w', encoding='utf-8') as pf:
            pf.write(settings_path)
        return True
    except IOError as e:
        messagebox.showerror(L["error_save_config_title"], L["error_save_config_message"].format(file=settings_path, e=e))
        return False

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
    except OSError as e:
        messagebox.showerror(L["error_create_folder_title"], L["error_create_folder_message"].format(path=folder_path, e=e))
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
        # *** 核心修正 ***
        # 移除 check=True，因为 explorer.exe 即使成功也可能返回非零状态码
        subprocess.run(['explorer', '/select,', normalized_path], creationflags=subprocess.CREATE_NO_WINDOW)
    except Exception as e:
        # 如果 /select 失败，尝试只打开文件夹作为备选方案
        try:
            folder = os.path.dirname(normalized_path)
            subprocess.run(['explorer', folder], creationflags=subprocess.CREATE_NO_WINDOW)
        except Exception as final_e:
            messagebox.showwarning(L["error_open_location_title"], L["error_open_location_message"].format(e=final_e))

# --- 主程序逻辑 ---
def main():
    root = tk.Tk()
    root.withdraw()

    try:
        settings = load_settings(root)
        
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
                user_choice = messagebox.askyesnocancel(
                    L["config_confirm_title"],
                    L["config_confirm_message"].format(editor_name=editor_name, save_folder=save_folder_path),
                    default=messagebox.NO,
                    parent=root
                )
                if user_choice is True:
                    should_reconfigure = True
                elif user_choice is None:
                    return
                else:
                    should_reconfigure = False

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
            if save_settings(settings, save_folder_path):
                messagebox.showinfo(L["config_saved_title"], L["config_saved_message"].format(settings_filename=L["settings_filename"]), parent=root)
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
            except OSError as e:
                messagebox.showwarning(L["warning_delete_failed_title"], L["warning_delete_failed_message"].format(e=e), parent=root)
        else:
            messagebox.showinfo(L["op_success_title"], L["op_success_message"].format(path=final_mojian_file_path), parent=root)
            if auto_open_location:
                open_file_location(final_mojian_file_path)

    except FileNotFoundError:
        messagebox.showerror(L["error_editor_not_found_title"], L["error_editor_not_found_message"].format(path=settings.get('editor_path')), parent=root)
    except Exception as e:
        messagebox.showerror(L["error_unexpected_title"], L["error_unexpected_message"].format(e=e), parent=root)
    finally:
        root.destroy()

if __name__ == "__main__":
    main()