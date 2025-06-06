@echo off
:: 将当前命令行的代码页切换为UTF-8，以正确处理中文字符
chcp 65001 > nul

@echo off
echo [墨笺] 开始编译，请稍候...

:: 定义变量
set SCRIPT_NAME=墨笺.py
set OUTPUT_DIR=nuitka_dist
set DESKTOP_PATH=%USERPROFILE%\Desktop

:: 1. 执行Nuitka编译
:: 我们在这里不再使用 --remove-output，因为我们需要手动处理文件
python -m nuitka --onefile --windows-console-mode=disable --enable-plugin=tk-inter --output-dir=%OUTPUT_DIR% %SCRIPT_NAME%

:: 2. 检查编译是否成功
:: Nuitka成功时，目标EXE会存在。
if not exist "%OUTPUT_DIR%\%SCRIPT_NAME:.py=.exe%" (
    echo [墨笺] 编译失败，请检查错误信息。
    pause
    exit /b
)

echo [墨笺] 编译成功！正在整理文件...

:: 3. 移动EXE到桌面
:: /Y 参数表示如果桌面已存在同名文件，则直接覆盖
move /Y "%OUTPUT_DIR%\%SCRIPT_NAME:.py=.exe%" "%DESKTOP_PATH%\"

:: 4. 清理所有临时文件和文件夹
:: /S 表示删除目录及其子目录，/Q 表示安静模式，不需确认
echo [墨笺] 正在清理临时文件...
rmdir /S /Q "%OUTPUT_DIR%"
rmdir /S /Q "%SCRIPT_NAME:.py=.build%"
del "%SCRIPT_NAME:.py=.spec%" 2>nul

echo [墨笺] 打包完成！新的 墨笺.exe 已放置在您的桌面。
pause