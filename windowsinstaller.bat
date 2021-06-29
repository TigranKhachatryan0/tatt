@echo off
echo [information] -- Checking if Python is installed...
py --version 2>NUL
if errorlevel 1 goto errorNoPython

echo [information] -- Python was found
echo [information] -- [mkdir] -- [C:] -- [Program Files] -- [TATT]
md "C:\Program Files\TATT"
echo [information] -- [xcopy] -- [source] -- "*"    [destination] -- [C:] -- [Program Files] -- [TATT]
xcopy /y /s ".\*" "C:\Program Files\TATT"
echo [information] -- Creating temporary VBS script in %TEMP%
set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"
echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%
echo sLinkFile = "%USERPROFILE%\Desktop\TATT.lnk" >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%
echo oLink.WorkingDirectory = "C:\Program Files\TATT" >> %SCRIPT%
echo oLink.TargetPath = "C:\Program Files\TATT\tatt.windows.cmd" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%
echo [information] -- Executing temporary VBS script
cscript /nologo %SCRIPT%
echo [information] -- Deleting temporary VBS script
del %SCRIPT%
echo [information] -- Done...
pause>nul

goto:eof

:errorNoPython
echo.
echo [error] -- Python is required
pause>nul
