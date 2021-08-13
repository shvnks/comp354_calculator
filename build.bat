@echo off

pyinstaller -F ^
--paths="%~dp0\src" ^
--paths="%~dp0\src\InterpreterModule" ^
--specpath tmp ^
--name ETERNITYCalculator ^
--distpath "%~dp0\ETERNITYCalculator" ^
--icon "%~dp0\src\icon.ico" ^
-y --clean --noconsole src\main.py

xcopy /Y "%~dp0\src\darkstyle.qss" "%~dp0\ETERNITYCalculator\"
xcopy /Y "%~dp0\src\icon.ico" "%~dp0\ETERNITYCalculator\"

rmdir /S /Q "%~dp0\tmp"
rmdir /S /Q "%~dp0\build"
