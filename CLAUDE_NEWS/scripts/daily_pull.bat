@echo off
setlocal
rem Daily git pull for ObsidianLab (run by Windows Task Scheduler).
rem Register once (adjust /ST to change the time):
rem   schtasks /Create /TN "ObsidianLab Daily Pull" /TR "\"C:\Users\Mandy\CLAUDE_OBSIDIAN\ObsidianLab\CLAUDE_NEWS\scripts\daily_pull.bat\"" /SC DAILY /ST 09:00 /F
rem Remove:
rem   schtasks /Delete /TN "ObsidianLab Daily Pull" /F

set "REPO=%~dp0..\.."
set "LOG=%USERPROFILE%\ObsidianLab-daily-pull.log"

echo [%date% %time%] daily pull start >> "%LOG%"

set "BRANCH="
for /f "delims=" %%b in ('git -C "%REPO%" rev-parse --abbrev-ref HEAD 2^>nul') do set "BRANCH=%%b"

if not defined BRANCH (
  echo [%date% %time%] FAILED: git unavailable or not a repo: %REPO% >> "%LOG%"
  exit /b 1
)

if /i not "%BRANCH%"=="master" (
  echo [%date% %time%] SKIP: on branch %BRANCH%, not master - no pull >> "%LOG%"
  exit /b 0
)

git -C "%REPO%" pull --ff-only origin master >> "%LOG%" 2>&1
if errorlevel 1 (
  echo [%date% %time%] FAILED: ff-only pull did not complete. Local master has diverged or a merge/rebase is in progress - resolve manually with: git pull --rebase origin master >> "%LOG%"
  exit /b 1
)

echo [%date% %time%] OK >> "%LOG%"
exit /b 0
