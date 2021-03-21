@echo off
set arg1=%1
python scrapeYT.py %arg1%
timeout /t 5
python processing.py
timeout /t 5
python youtubeSentiment.py
timeout /t 5
python processing_final.py
timeout /t 5
python plot.py
