@echo off
setlocal

set REPO_ROOT=C:\Users\Mandy\CLAUDE_OBSIDIAN\ObsidianLab\CLAUDE_NEWS
set LOG_FILE=%REPO_ROOT%\src\logs\task_scheduler.log
set PYTHON=C:\Users\Mandy\AppData\Local\Programs\Python\Python313\python.exe

REM ---- Optional date argument (%1) for backfill mode --------------------------
if "%~1"=="" (
    set TARGET_DATE=
    set DATE_ARG=
    set WIKI_PROMPT=/wiki-ingest
) else (
    set TARGET_DATE=%~1
    set DATE_ARG=--date %~1
    set WIKI_PROMPT=Please ingest news/^%~1^%.md and update the wiki.
)

echo. >> "%LOG_FILE%"
if "%TARGET_DATE%"=="" (
    echo === Daily pipeline start [%DATE% %TIME%] ===
    echo [%DATE% %TIME%] === Daily pipeline start === >> "%LOG_FILE%"
) else (
    echo === Backfill pipeline start: %TARGET_DATE% [%DATE% %TIME%] ===
    echo [%DATE% %TIME%] === Backfill pipeline start: %TARGET_DATE% === >> "%LOG_FILE%"
)

REM ---- Step 1: News aggregator ------------------------------------------------
echo [Step 1/4] News aggregator...
cd /d "%REPO_ROOT%\src"
pip show feedparser >nul 2>&1 || pip install -r requirements_news.txt -q
pip show anthropic >nul 2>&1 || pip install -r requirements_news.txt -q

"%PYTHON%" -m news_aggregator.main %DATE_ARG% >> "%LOG_FILE%" 2>&1
if ERRORLEVEL 1 (
    echo [Step 1/4] FAILED - stopping
    echo [%DATE% %TIME%] Aggregator FAILED - stopping >> "%LOG_FILE%"
    exit /b 1
)
echo [Step 1/4] OK
echo [%DATE% %TIME%] Aggregator OK >> "%LOG_FILE%"

REM ---- Step 2: Wiki ingest (claude -p, non-interactive) -----------------------
echo [Step 2/4] Wiki ingest...
echo [%DATE% %TIME%] Starting wiki ingest... >> "%LOG_FILE%"
cd /d "%REPO_ROOT%"
call claude -p "%WIKI_PROMPT%" --dangerously-skip-permissions >> "%LOG_FILE%" 2>&1
if ERRORLEVEL 1 (
    echo [Step 2/4] FAILED - skipping wiki push
    echo [%DATE% %TIME%] Wiki ingest FAILED - skipping wiki push >> "%LOG_FILE%"
    exit /b 0
)
echo [Step 2/4] OK
echo [%DATE% %TIME%] Wiki ingest OK >> "%LOG_FILE%"

REM ---- Step 3: Commit and push wiki changes -----------------------------------
echo [Step 3/4] Pushing wiki...
if "%TARGET_DATE%"=="" (
    for /f %%d in ('%PYTHON% -c "from datetime import date; print(date.today())"') do set COMMIT_DATE=%%d
) else (
    set COMMIT_DATE=%TARGET_DATE%
)
git -C "%REPO_ROOT%" add wiki/ >> "%LOG_FILE%" 2>&1
git -C "%REPO_ROOT%" commit -m "wiki: auto-ingest %COMMIT_DATE%" >> "%LOG_FILE%" 2>&1
git -C "%REPO_ROOT%" push >> "%LOG_FILE%" 2>&1
echo [Step 3/4] OK
echo [%DATE% %TIME%] Wiki push done >> "%LOG_FILE%"

REM ---- Step 4: Build web reader and push --------------------------------------
echo [Step 4/4] Building web reader...
echo [%DATE% %TIME%] Building web reader... >> "%LOG_FILE%"
"%PYTHON%" "%REPO_ROOT%\scripts\build_web.py" >> "%LOG_FILE%" 2>&1
if ERRORLEVEL 1 (
    echo [Step 4/4] FAILED - skipping web push
    echo [%DATE% %TIME%] build_web FAILED - skipping web push >> "%LOG_FILE%"
    exit /b 0
)
git -C "%REPO_ROOT%" add web_reader/ >> "%LOG_FILE%" 2>&1
git -C "%REPO_ROOT%" commit -m "web: rebuild %COMMIT_DATE%" >> "%LOG_FILE%" 2>&1
git -C "%REPO_ROOT%" push >> "%LOG_FILE%" 2>&1
echo [Step 4/4] OK
echo [%DATE% %TIME%] Web push done >> "%LOG_FILE%"

echo.
echo === Pipeline complete ===
echo [%DATE% %TIME%] === Pipeline complete === >> "%LOG_FILE%"
