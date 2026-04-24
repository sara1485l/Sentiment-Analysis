"""
Configuration file for Smart Review Analyzer
Customize settings here
"""

# ==================== Flask Configuration ====================

DEBUG = True
HOST = '0.0.0.0'
PORT = 5000

# ==================== NLP Configuration ====================

# Sentiment Analysis
SENTIMENT_POSITIVE_THRESHOLD = 0.1      # Polarity score above this is positive
SENTIMENT_NEGATIVE_THRESHOLD = -0.1     # Polarity score below this is negative

# Keyword Extraction
KEYWORDS_COUNT = 5                       # Number of keywords to extract
TFIDF_MAX_FEATURES = 100                # Maximum features for TF-IDF
MIN_DOCUMENT_FREQUENCY = 1              # Minimum document frequency
MAX_DOCUMENT_FREQUENCY = 1.0            # Maximum document frequency

# Text Summarization
SUMMARY_SENTENCES = 2                   # Number of sentences in summary
SUMMARY_MIN_LENGTH = 50                 # Minimum text length to summarize

# ==================== Frontend Configuration ====================

API_TIMEOUT = 30000                     # API request timeout in milliseconds
AUTO_ANALYZE_DELAY = 1000               # Delay for real-time analysis (ms)

# ==================== Logging ====================

LOG_LEVEL = 'INFO'                      # DEBUG, INFO, WARNING, ERROR
LOG_FILE = 'app.log'

# ==================== CORS Configuration ====================

CORS_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://localhost:3000',             # For React frontend if used
    '*'                                  # Allow all origins (development only)
]

# ==================== Feature Flags ====================

ENABLE_KEYWORD_HIGHLIGHTING = True
ENABLE_REAL_TIME_ANALYSIS = False
ENABLE_FILE_UPLOAD = False
ENABLE_EXPORT_PDF = False
