@echo off
setlocal

set REPO_ROOT=C:\Users\Mandy\CLAUDE_OBSIDIAN\ObsidianLab\CLAUDE_NEWS
set LOG_FILE=%REPO_ROOT%\src\logs\task_scheduler.log
set PYTHON=C:\Users\Mandy\AppData\Local\Programs\Python\Python313\python.exe

echo. >> "%LOG_FILE%"
echo [%DATE% %TIME%] ======== Daily pipeline start ======== >> "%LOG_FILE%"

REM ── Step 1: News aggregator ───────────────────────────────────────────────────
cd /d "%REPO_ROOT%\src"
pip show feedparser >nul 2>&1 || pip install -r requirements_news.txt -q
pip show anthropic >nul 2>&1 || pip install -r requirements_news.txt -q

"%PYTHON%" -m news_aggregator.main >> "%LOG_FILE%" 2>&1
if ERRORLEVEL 1 (
    echo [%DATE% %TIME%] Aggregator FAILED - stopping pipeline >> "%LOG_FILE%"
    exit /b 1
)
echo [%DATE% %TIME%] Aggregator OK >> "%LOG_FILE%"

REM ── Step 2: Wiki ingest ───────────────────────────────────────────────────────
echo [%DATE% %TIME%] Starting wiki ingest... >> "%LOG_FILE%"
cd /d "%REPO_ROOT%"
REM --dangerously-skip-permissions: no user present in scheduled mode; scope is
REM limited to this project's Read/Edit/Write on wiki/ and news/ files only.
claude -p "/wiki-ingest" --dangerously-skip-permissions >> "%LOG_FILE%" 2>&1
if ERRORLEVEL 1 (
    echo [%DATE% %TIME%] Wiki ingest FAILED - skipping wiki push >> "%LOG_FILE%"
    exit /b 0
)
echo [%DATE% %TIME%] Wiki ingest OK >> "%LOG_FILE%"

REM ── Step 3: Commit and push wiki changes ─────────────────────────────────────
for /f %%d in ('%PYTHON% -c "from datetime import date; print(date.today())"') do set TODAY=%%d
git -C "%REPO_ROOT%" add wiki/ >> "%LOG_FILE%" 2>&1
git -C "%REPO_ROOT%" commit -m "wiki: auto-ingest %TODAY%" >> "%LOG_FILE%" 2>&1
git -C "%REPO_ROOT%" push >> "%LOG_FILE%" 2>&1
echo [%DATE% %TIME%] Wiki push done >> "%LOG_FILE%"

echo [%DATE% %TIME%] ======== Daily pipeline complete ======== >> "%LOG_FILE%"
