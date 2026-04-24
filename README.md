# Smart Review Analyzer - NLP System

A web-based NLP application that analyzes user reviews and provides sentiment analysis, keyword extraction, text summarization, and data visualization.

## 🌟 Features

- **Sentiment Analysis**: Classify reviews as Positive, Negative, or Neutral using TextBlob
- **Keyword Extraction**: Extract top 5 important keywords using TF-IDF (scikit-learn)
- **Text Summarization**: Generate concise summaries using LSA Summarizer (sumy)
- **Data Visualization**: Interactive pie chart showing sentiment distribution
- **Review Filtering**: Filter reviews by sentiment type
- **Real-time Statistics**: View sentiment percentages and counts

## 📋 Project Structure

```
NLP/
├── backend/
│   ├── app.py              # Main Flask application
│   ├── sentiment.py        # Sentiment analysis module
│   ├── keywords.py         # Keyword extraction module
│   ├── summary.py          # Text summarization module
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── index.html          # Main HTML file
│   ├── style.css           # Styling
│   └── script.js           # Frontend logic
└── README.md               # This file
```

## 🔧 Technical Stack

### Backend
- **Python 3.8+**
- **Flask** - Web framework
- **TextBlob** - Sentiment analysis
- **scikit-learn** - Keyword extraction (TF-IDF)
- **sumy** - Text summarization (LSA)
- **Flask-CORS** - Cross-Origin Resource Sharing

### Frontend
- **HTML5** - Markup
- **CSS3** - Styling
- **JavaScript (Vanilla)** - Interactivity
- **Chart.js** - Data visualization

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Modern web browser

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd NLP/backend
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK data (required for summarization):**
   ```bash
   python -m textblob.download_corpora
   python -c "import nltk; nltk.download('punkt'); nltk.download('averaged_perceptron_tagger')"
   ```

5. **Run the Flask server:**
   ```bash
   python app.py
   ```
   
   The API will be available at `http://localhost:5000`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd NLP/frontend
   ```

2. **Serve the frontend using Python's built-in server:**
   ```bash
   # Python 3
   python -m http.server 8000
   
   # Or use any other local server like Live Server extension in VS Code
   ```

3. **Open in browser:**
   - Navigate to `http://localhost:8000`

## 🚀 Usage

### Basic Workflow

1. Enter one or more reviews in the text area (one per line)
2. Click "Analyze Reviews" button
3. View results:
   - Sentiment statistics with pie chart
   - Top 5 keywords with importance scores
   - Combined summary of all reviews
   - Individual review details with sentiment labels

### Input Format

Enter reviews with one review per line:
```
This product is amazing! I love it.
Terrible quality, very disappointed.
It's okay, nothing special.
```

### Filtering

Click the filter buttons to view reviews by sentiment:
- **All Reviews** - Show all reviews
- **✅ Positive** - Show only positive reviews
- **❌ Negative** - Show only negative reviews
- **➖ Neutral** - Show only neutral reviews

## 🔌 API Endpoints

### POST /analyze

**Description:** Analyze multiple reviews

**Request:**
```json
{
    "texts": ["review1", "review2"],
    "summary_sentences": 2
}
```

**Response:**
```json
{
    "success": true,
    "analysis": {
        "sentiments": [
            {
                "sentiment": "Positive",
                "polarity": 0.857,
                "text": "This product is amazing!"
            }
        ],
        "statistics": {
            "total": 1,
            "positive": 1,
            "negative": 0,
            "neutral": 0,
            "positive_percent": 100,
            "negative_percent": 0,
            "neutral_percent": 0
        },
        "keywords": [
            {"word": "product", "score": 0.452},
            {"word": "amazing", "score": 0.398}
        ],
        "summary": "Summary text here",
        "total_reviews": 1
    }
}
```

### POST /analyze-single

**Description:** Analyze a single review with keyword highlighting

**Request:**
```json
{
    "text": "This product is amazing!"
}
```

### POST /keywords

**Description:** Extract keywords from texts

**Request:**
```json
{
    "texts": ["text1", "text2"],
    "top_n": 5
}
```

## 📊 NLP Pipeline

```
User Input (Reviews)
        ↓
    [Text Cleaning]
        ↓
    [Sentiment Analysis] → Classification (Pos/Neg/Neutral)
        ↓
    [Keyword Extraction] → Top 5 Keywords (TF-IDF)
        ↓
    [Text Summarization] → Summary (2-3 sentences)
        ↓
    [Visualization] → Pie Chart + Statistics
        ↓
    Display Results to User
```

## 🎯 How It Works

### Sentiment Analysis
- Uses **TextBlob** library which leverages VADER sentiment analyzer
- Polarity score ranges from -1 (most negative) to 1 (most positive)
- Classification:
  - Positive: polarity > 0.1
  - Negative: polarity < -0.1
  - Neutral: -0.1 ≤ polarity ≤ 0.1

### Keyword Extraction
- Uses **TF-IDF (Term Frequency-Inverse Document Frequency)**
- Identifies terms that are important in the review collection
- Stops common English words using stopwords
- Returns top 5 keywords with importance scores

### Text Summarization
- Uses **LSA (Latent Semantic Analysis)** from sumy library
- Generates summary with 2-3 sentences by default
- Identifies most important sentences based on semantic content

### Data Visualization
- **Chart.js** library for interactive charts
- Pie/Doughnut chart showing sentiment distribution
- Real-time updates based on analysis results

## 🔐 Error Handling

The application includes comprehensive error handling for:
- Empty or invalid input
- API connection failures
- Missing dependencies
- Invalid JSON responses

All errors are displayed in user-friendly messages.

## 🚦 Running the Complete Application

### Terminal 1 - Start Backend
```bash
cd NLP/backend
python app.py
```

### Terminal 2 - Start Frontend
```bash
cd NLP/frontend
python -m http.server 8000
```

Then open `http://localhost:8000` in your browser.

## 📈 Example Output

**Input:**
```
I absolutely love this product! Highly recommend!
Worst purchase ever, total waste of money.
The product is fine, does what it says.
```

**Output:**
```
Sentiment Distribution:
- Positive: 1 (33.33%)
- Negative: 1 (33.33%)
- Neutral: 1 (33.33%)

Top Keywords:
- product (0.452)
- love (0.398)
- waste (0.345)
- recommend (0.298)
- money (0.276)

Summary:
"I absolutely love this product and highly recommend it. 
The product is fine and does what it says. 
Worst purchase ever, total waste of money."
```

## 🎨 UI Features

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Interactive Charts**: Hover for detailed statistics
- **Sentiment Color Coding**: Green (positive), Red (negative), Gray (neutral)
- **Smooth Animations**: Professional transitions and effects
- **Keyboard Shortcuts**: Ctrl+Enter to analyze (when in textarea)

## 📚 Dependencies

### Python Packages
- Flask==2.3.0
- Flask-CORS==4.0.0
- TextBlob==0.17.1
- scikit-learn==1.3.0
- sumy==0.12.0
- numpy==1.24.0
- nltk==3.8.1

### JavaScript Libraries
- Chart.js (via CDN)

## 🐛 Troubleshooting

### CORS Error
- Ensure Flask-CORS is installed: `pip install Flask-CORS`
- Check that backend is running on port 5000

### TextBlob Error
- Run: `python -m textblob.download_corpora`

### NLTK Data Error
- Run: `python -m nltk.downloader punkt averaged_perceptron_tagger`

### Port Already in Use
- Change port in `app.py` (default: 5000)
- Or stop the process using the port

## 🚀 Future Enhancements

- [ ] Aspect-based sentiment analysis
- [ ] Multi-language support
- [ ] Entity recognition
- [ ] File upload support (CSV, TXT)
- [ ] Export results to PDF
- [ ] Real-time analysis while typing
- [ ] User authentication & history
- [ ] Advanced NLP models (BERT, GPT)
- [ ] Mobile app version
- [ ] Database integration

## 📝 License

This project is created for educational purposes as part of an NLP team project.

## 👥 Team Roles

1. **Backend Developer** - Build Flask API & integrate NLP functions
2. **NLP Engineer** - Implement sentiment, keywords, summarization
3. **Frontend Developer** - Build UI & connect API
4. **Data/Visualization** - Create charts & handle statistics

## 📞 Support

For issues or questions, please check:
1. README.md file
2. Code comments and documentation
3. Error messages in browser console
4. Terminal output for backend errors

## 🎓 Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [TextBlob Guide](https://textblob.readthedocs.io/)
- [scikit-learn TF-IDF](https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting)
- [Sumy Documentation](https://github.com/asavinov/sumy)
- [Chart.js Guide](https://www.chartjs.org/)

---

**Created:** 2026 | **Version:** 1.0
