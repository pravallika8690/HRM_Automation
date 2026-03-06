@echo off
:: This command finds the folder where this batch file is located
cd /d "%~dp0"

echo Successfully moved to: %cd%

:: Check if the virtual environment exists here
if not exist .venv (
    echo [ERROR] Could not find .venv folder in %cd%
    pause
    exit
)

:: Run the tests
echo Starting Pytest...
call .venv\Scripts\pytest test_scripts/ --headed --html=test_reports/daily_status.html

echo.
echo Tests completed! Check your report in the test_reports folder.
pause