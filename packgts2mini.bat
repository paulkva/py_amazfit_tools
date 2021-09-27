@echo off

IF "%1"=="" GOTO :Continue

set file=%~n1
set mPath=%~dp1
set mPathScript=%~dp0
echo %file%

python %mPathScript%\main.py --gts2mini --file %1
ren "%mPath%%file%_packed.bin.cmp" "%file%_packed_cmp.bin"

echo.
echo Install "%mPath%%file%_packed_cmp.bin" to Watch
echo.
pause

:Continue
IF "%1"=="" echo No json given. Usage: %~nx0 path\to\file.json

