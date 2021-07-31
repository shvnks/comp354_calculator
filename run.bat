@echo off

set PYTHONPATH=%PYTHONPATH%;%~dp0\src\InterpreterModule;%~dp0\src
start "" "pythonw.exe" "%~dp0\src\main.py"