@echo off

IF "%1"=="" GOTO :Continue

set file=%~n1
set mPath=%~dp1
set mPathScript=%~dp0

for %%i in (%1\*.bin) do (
    echo "%%i"
    call python %mPathScript%\main.py --gts2mini --file "%%i"
)

pause

:Continue
IF "%1"=="" echo No folder given. Usage: %~nx0 path\to\binfiles\

