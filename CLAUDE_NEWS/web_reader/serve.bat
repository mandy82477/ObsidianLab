@echo off
set PORT=8765
echo Starting CLAUDE NEWS web reader at http://localhost:%PORT%
start "" "http://localhost:%PORT%"
python -m http.server %PORT%
