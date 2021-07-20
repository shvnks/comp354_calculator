@echo off

set PYTHONPATH=%~dp0\src;%~dp0\src\Interpreter
start "" "%~dp0\Python\pythonw.exe" "%~dp0\src\main.py"