# 墨笺 (Mojian) - M0JIAN127

<p align="center">
  <img src="https://img.shields.io/badge/version-M0JIAN127-blue.svg" alt="Version">
  <img src="https://img.shields.io/badge/platform-Windows-informational.svg" alt="Platform">
  <img src="https://img.shields.io/github/license/630StarFortune/Mojian" alt="License">
  <img src="https://img.shields.io/badge/made%20with-Python%20%26%20Nuitka-orange.svg" alt="Made with Python & Nuitka">
</p>

<p align="center">
  <i>化任意编辑器，为代码灵感之速记。</i>
</p>

---

**墨笺 (Mojian)** 是一款将任意文本编辑器升华为极简、高效、个性化代码片段速记启动器的 Windows 应用。它告别散乱的临时文件，让你轻点一下，用自己最爱的编辑器，瞬间开启一个纯净的书写空间。

[**访问官方展示页，感受墨笺之美**](https://mojian-inkpad--stella.on.websim.com/)  

## ✨ 核心理念

*   **静谧与专注 (Serenity & Focus):** 如同深夜书房中的一盏孤灯，界面需摒除一切不必要的干扰。
*   **传统与现代的融合 (Fusion of Tradition & Modernity):** 将东方书写美学与现代极简主义设计无缝结合。
*   **优雅的实用主义 (Elegant Pragmatism):** 每一个设计元素和交互动效都必须服务于功能，既要美观，更要实用。

## 🚀 主要特性 (M0JIAN127 - “锦书”功能集)

*   **✍️ 自由择器，随心而动:** 不再束缚于记事本。VS Code, Sublime Text, Notepad++... 选择你最顺手的兵器，墨笺为你铺开稿纸。
*   **⚡ 一步到位，流转自如:** 开启“完成时定位”，文件保存的瞬间，文件夹自动弹出，让你无缝拖拽至 AI 对话、代码仓库或任何地方。
*   **🛡️ 坚如磐石，告别卡死:** 彻底重构启动逻辑，从根源上解决了可能导致程序无响应或产生“幽灵进程”的底层Bug，确保在任何系统环境下都能稳定启动。
*   **📜 风雅命名，标准管理:** 配置文件被优雅地命名为《墨笺之卷.json》，并遵循行业标准存放于 `AppData/Roaming` 目录，与主程序完全分离，纯净可靠。
*   **📑 轻量备份，安心无忧:** 当您修改并保存一个已存在的 `墨笺n.txt` 文件时，程序会自动将旧版内容备份为 `墨笺n.txt.bak`，为您的创作提供多一重保障。
*   **🌍 双语内核，无界沟通:** 自动检测操作系统语言，为你呈现最亲切的中文或英文界面。
*   **🧠 智能引导，体验至上:** 内置“内部构建号”机制，可在程序更新后智能检测并建议用户重置配置，确保新旧版本平滑过渡。

## 🛠️ 如何使用

### 1. 快速开始 (最终用户)

1.  前往 [**Releases**](https://github.com/630StarFortune/Mojian/releases) 页面下载最新的 `墨笺.exe` 文件。
2.  将 `墨笺.exe` 放置于任何您喜欢的位置（如桌面）。
3.  双击运行，程序会引导你完成三步设置：
    *   **选择保存位置:** 指定一个文件夹用于存放所有“墨笺”文件。
    *   **选择编辑器:** 选择你常用的文本编辑器程序 (`.exe`)。
    *   **开启效率功能:** 决定是否在保存后自动打开文件所在位置（强烈推荐）。
4.  设置完成后，你的编辑器会自动打开一个新文件。完成记录，保存并关闭即可。

### 2. 从源码构建 (开发者)

本项目使用 **Nuitka** 进行编译，以获得最佳性能和独立性。

1.  **环境准备:**
    *   确保已安装 Python (本项目基于 3.13)。
    *   安装 Nuitka 及相关依赖:
        ```bash
        pip install nuitka zstandard ordered-set
        ```
    *   确保已安装 C++ 编译器 (如 Visual Studio 2022 Build Tools)。

2.  **一键构建:**
    *   将 `墨笺.py` 和 `build.bat` 脚本放在同一目录下。
    *   双击运行 `build.bat`。
    *   脚本将自动完成编译、移动 `墨笺.exe` 到桌面，并清理所有临时文件。

## 💖 贡献

尽管核心功能已趋于稳定，但我们依然欢迎任何形式的贡献！无论是提交 Issue、发起 Pull Request，还是分享你的想法。

1.  Fork 本仓库
2.  创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3.  提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4.  推送到分支 (`git push origin feature/AmazingFeature`)
5.  打开一个 Pull Request

## 📄 授权协议

本项目基于 [MIT License](LICENSE) 授权。

---
<p align="center">
  由 <a href="https://github.com/630StarFortune">星缘</a> 带着对简洁与效率的热爱而创造。
</p>