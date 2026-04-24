# Windows Setup Script
# Smart Review Analyzer - Setup for Windows

@echo off
echo ================================
echo Smart Review Analyzer - Setup
echo ================================
echo.

REM Check Python version
echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from https://www.python.org
    pause
    exit /b 1
)

python --version
echo Python found!
echo.

REM Navigate to backend directory
cd backend

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv
echo Virtual environment created!
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate
echo Virtual environment activated!
echo.

REM Install dependencies
echo Installing Python dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt
echo Dependencies installed!
echo.

REM Download required NLTK data
echo Downloading NLP data (this may take a minute)...
python -m textblob.download_corpora
python -c "import nltk; nltk.download('punkt'); nltk.download('averaged_perceptron_tagger')"
echo NLP data downloaded!
echo.

echo ================================
echo Setup Complete!
echo ================================
echo.
echo To run the application:
echo.
echo Terminal 1 (Backend):
echo   cd backend
echo   venv\Scripts\activate
echo   python app.py
echo.
echo Terminal 2 (Frontend):
echo   cd frontend
echo   python -m http.server 8000
echo.
echo Then open: http://localhost:8000
echo.
pause
