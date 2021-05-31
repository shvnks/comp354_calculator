rem Add the third part Qt library directory to the path for python to find
set PYTHONPATH=%~dp0third_party
start "" pythonw.exe "%~dp0\src\test.py"
