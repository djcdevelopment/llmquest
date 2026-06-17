@echo off
REM === Old Goat, New Tricks - one-time setup for your Kid ===
title Kid Setup

where py >nul 2>nul
if errorlevel 1 (
  echo Python isn't installed yet. Installing it now...
  echo.
  winget install Python.Python.3.12 -e --accept-source-agreements --accept-package-agreements
  echo.
  echo -------------------------------------------------------
  echo  Python is installed. Windows needs a fresh window to
  echo  see it -- so CLOSE this window and double-click
  echo  setup.bat ONE more time.
  echo -------------------------------------------------------
  echo.
  pause
  exit /b
)

echo Installing the Kid's libraries (discord.py, ollama, python-dotenv)...
echo.
py -m pip install --upgrade discord.py ollama python-dotenv

if not exist .env copy .env.example .env >nul

echo.
echo =======================================================
echo  Setup complete.
echo.
echo  Next:
echo    1. Open  .env  (in this folder) with Notepad
echo    2. Paste your bot token after  DISCORD_TOKEN=
echo    3. Save it, then double-click  start-kid.bat
echo =======================================================
echo.
pause
