@echo off
cd /d "C:\Users\Mandy\CLAUDE_OBSIDIAN\ObsidianLab\CLAUDE_NEWS\src"

REM Install missing dependencies silently on first run
pip show feedparser >nul 2>&1 || pip install -r requirements_news.txt -q
pip show anthropic >nul 2>&1 || pip install -r requirements_news.txt -q

REM Run the aggregator (python.exe captures stdout for Task Scheduler log)
"C:\Users\Mandy\AppData\Local\Programs\Python\Python313\python.exe" -m news_aggregator.main >> "C:\Users\Mandy\CLAUDE_OBSIDIAN\ObsidianLab\CLAUDE_NEWS\src\logs\task_scheduler.log" 2>&1
