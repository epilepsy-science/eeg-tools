@echo off
docker run --rm -v "C:\Users\ddefreitas.exe\Documents\input:/app/input" -v "C:\Users\ddefreitas.exe\Documents\output:/app/output" eeg-processor
pause
