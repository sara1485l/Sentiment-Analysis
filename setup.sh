#!/bin/bash
# Smart Review Analyzer - Setup Script
# Automates the installation and setup process

echo "================================"
echo "Smart Review Analyzer - Setup"
echo "================================"
echo ""

# Check Python version
echo "Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

python_version=$(python3 --version | cut -d' ' -f2)
echo "✅ Python $python_version found"
echo ""

# Navigate to backend directory
cd backend

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
echo "✅ Virtual environment created"
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo "✅ Virtual environment activated"
echo ""

# Install dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip > /dev/null
pip install -r requirements.txt
echo "✅ Dependencies installed"
echo ""

# Download required NLTK data
echo "Downloading NLP data (this may take a minute)..."
python -m textblob.download_corpora > /dev/null 2>&1
python -c "import nltk; nltk.download('punkt', quiet=True); nltk.download('averaged_perceptron_tagger', quiet=True)"
echo "✅ NLP data downloaded"
echo ""

echo "================================"
echo "Setup Complete! ✅"
echo "================================"
echo ""
echo "To run the application:"
echo ""
echo "Terminal 1 (Backend):"
echo "  cd backend"
echo "  source venv/bin/activate  # or: . venv/Scripts/activate (on Windows)"
echo "  python app.py"
echo ""
echo "Terminal 2 (Frontend):"
echo "  cd frontend"
echo "  python -m http.server 8000"
echo ""
echo "Then open: http://localhost:8000"
echo ""
