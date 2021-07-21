@echo off

set PYTHONPATH=%~dp0\src\InterpreterModule;%~dp0\src
start "" "%~dp0\Python\pythonw.exe" "%~dp0\src\main.py"