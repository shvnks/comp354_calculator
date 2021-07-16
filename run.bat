@echo off
rem Add the third part Qt library directory to the path for python to find
start "" "%~dp0\Python\pythonw.exe" "%~dp0\src\main.py"