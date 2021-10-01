@echo off

IF "%1"=="" GOTO :Continue

set file=%~n1
set mPath=%~dp1
set mPathScript=%~dp0

python %mPathScript%\main.py --gts2mini --file "%mPath%%file%"

echo.
echo Resources and JSON in "%mPath%%file%"
echo.
pause

:Continue
IF "%1"=="" echo No bin file given. Usage: %~nx0 path\to\file.bin

