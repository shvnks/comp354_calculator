@echo off

set PYTHONPATH=%PYTHONPATH%;%~dp0\src\InterpreterModule;%~dp0\src

pushd "%~dp0\src"
"python.exe" "main.py"
popd
