# 墨笺 (Mojian)

<p align="center">
  <a href="https://deepwiki.com/630StarFortune/Mojian" target="_blank"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki"></a>
  <img src="https://img.shields.io/badge/version-v1.2.1-blue.svg" alt="Version">
  <img src="https://img.shields.io/badge/platform-Windows-informational.svg" alt="Platform">
  <img src="https://img.shields.io/github/license/630StarFortune/Mojian" alt="License">
  <img src="https://img.shields.io/badge/made%20with-Python%20%26%20Tkinter-orange.svg" alt="Made with Python & Tkinter">
</p>

<p align="center">
  <i>化任意编辑器，为代码灵感之速记。</i>
</p>

---

**墨笺 (Mojian)** 是一款将系统记事本升华为极简、高效、个性化代码片段速记启动器的 Windows 应用。它告别散乱的代码片段，让你轻点一下，用自己最爱的编辑器，瞬间开启一个纯净的书写空间。

[**访问官方展示页，感受墨笺之美**](https://mojian-inkpad--stella.on.websim.com/)  

## ✨ 核心理念

*   **静谧与专注 (Serenity & Focus):** 如同深夜书房中的一盏孤灯，界面需摒除一切不必要的干扰。
*   **传统与现代的融合 (Fusion of Tradition & Modernity):** 将东方书写美学与现代极简主义设计无缝结合。
*   **优雅的实用主义 (Elegant Pragmatism):** 每一个设计元素和交互动效都必须服务于功能，既要美观，更要实用。

## 🚀 主要特性

*   **✍️ 自由择器，随心而动:** 不再束缚于记事本。VS Code, Sublime Text, Notepad++... 选择你最顺手的兵器，墨笺为你铺开稿纸。
*   **⚡ 一步到位，流转自如:** 开启“完成时定位”，文件保存的瞬间，文件夹自动弹出，让你无缝拖拽至 AI 对话、代码仓库或任何地方。
*   **📜 风雅命名，东方神韵:** 摒弃冰冷的 `settings.json`，代之以《墨笺之引》与《墨笺之卷》，让每一次配置都充满仪式感。
*   **🌍 双语内核，无界沟通:** 自动检测操作系统语言，为你呈现最亲切的中文或英文界面。
*   **🧠 智能管理:** 自动为文件编号，并填补被删除的序号空缺；不保存空文件，保持文件夹清爽。

## 🛠️ 如何使用

### 1. 快速开始 (推荐)

1.  前往 [**Releases**](https://github.com/630StarFortune/Mojian/releases) 页面下载最新的 `墨笺.exe` 文件。
2.  将 `墨笺.exe` 放置于任何你喜欢的位置。
3.  双击运行，程序会引导你完成三步设置：
    *   **选择保存位置:** 指定一个文件夹用于存放所有“墨笺”文件。
    *   **选择编辑器:** 选择你常用的文本编辑器程序 (`.exe`)。
    *   **开启效率功能:** 决定是否在保存后自动打开文件所在位置（强烈推荐）。
4.  设置完成后，你的编辑器会自动打开一个新文件。完成记录，保存并关闭即可。

### 2. 从源码运行 (适合开发者)

1.  确保你的系统已安装 Python 3 和 Tkinter。
2.  克隆本仓库：
    ```bash
    git clone https://github.com/630StarFortune/Mojian.git
    ```
3.  进入项目目录并运行：
    ```bash
    cd Mojian
    python 墨笺.py 
    ```
    *(请确保您的 Python 脚本文件名为 `墨笺.py`)*

### 3. 自行打包

1.  安装 `pyinstaller`:
    ```bash
    pip install pyinstaller
    ```
2.  在项目根目录运行打包命令：
    ```bash
    pyinstaller --onefile --windowed --name 墨笺 墨笺.py
    ```
3.  打包完成的 `墨笺.exe` 文件会出现在 `dist` 文件夹内。

## 💖 贡献

欢迎任何形式的贡献！无论是提交 Issue、发起 Pull Request，还是分享你的想法。

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
