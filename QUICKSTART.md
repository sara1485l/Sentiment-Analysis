# Quick Start Guide - Smart Review Analyzer

## 🚀 5-Minute Setup

### Option 1: Automated Setup (Recommended)

#### On macOS/Linux:
```bash
cd NLP
bash setup.sh
```

#### On Windows:
```bash
cd NLP
setup.bat
```

### Option 2: Manual Setup

#### Step 1: Install Backend Dependencies
```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
python -m textblob.download_corpora
```

#### Step 2: Run Backend
```bash
python app.py
```
✅ Backend running on: `http://localhost:5000`

#### Step 3: Run Frontend (in another terminal)
```bash
cd frontend
python -m http.server 8000
```
✅ Frontend running on: `http://localhost:8000`

#### Step 4: Open in Browser
Open: **http://localhost:8000**

---

## 📝 Example Usage

### Input:
```
I absolutely love this product! Highly recommend!
Worst purchase ever, total waste of money.
The product is fine, does what it says.
```

### Output:
```
Sentiments:
✅ Positive: 1 review
❌ Negative: 1 review
➖ Neutral: 1 review

Top Keywords:
- product (85%)
- love (72%)
- waste (65%)

Summary:
"I absolutely love this product and highly recommend it. 
Worst purchase ever, total waste of money."
```

---

## 🧪 Test the System

Before running the full application, test the NLP modules:

```bash
cd backend
python test_nlp.py
```

This will test:
- ✅ Sentiment Analysis
- ✅ Keyword Extraction
- ✅ Text Summarization
- ✅ Text Cleaning
- ✅ API Request Format

---

## 🔌 API Testing

### Using curl:
```bash
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "texts": [
      "This product is amazing!",
      "Not good at all."
    ],
    "summary_sentences": 2
  }'
```

### Using Python:
```python
import requests

response = requests.post('http://localhost:5000/analyze', json={
    'texts': ['This is great!', 'This is terrible.'],
    'summary_sentences': 2
})

print(response.json())
```

### Using JavaScript (in frontend):
```javascript
fetch('http://localhost:5000/analyze', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
        texts: ['Great product!', 'Bad quality.'],
        summary_sentences: 2
    })
})
.then(res => res.json())
.then(data => console.log(data))
```

---

## ❓ Troubleshooting

### Port Already in Use
- **Error**: `Address already in use`
- **Solution**: Kill the process or use a different port
```bash
# Change port in app.py: app.run(port=5001)
# Or kill process:
lsof -ti:5000 | xargs kill -9  # macOS/Linux
netstat -ano | findstr :5000   # Windows
```

### CORS Error
- **Error**: `CORS policy: No 'Access-Control-Allow-Origin'`
- **Solution**: Ensure Flask-CORS is installed
```bash
pip install Flask-CORS
```

### TextBlob Error
- **Error**: `Cannot find corpora...`
- **Solution**: Download corpora
```bash
python -m textblob.download_corpora
```

### Module Not Found
- **Error**: `ModuleNotFoundError: No module named 'flask'`
- **Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

---

## 📚 Project Structure

```
NLP/
├── backend/
│   ├── app.py              # Main Flask app
│   ├── sentiment.py        # Sentiment analysis
│   ├── keywords.py         # Keyword extraction
│   ├── summary.py          # Text summarization
│   ├── config.py           # Configuration
│   ├── test_nlp.py         # Test suite
│   └── requirements.txt    # Dependencies
├── frontend/
│   ├── index.html          # Main page
│   ├── style.css           # Styling
│   └── script.js           # Frontend logic
├── setup.sh                # Auto setup (macOS/Linux)
├── setup.bat               # Auto setup (Windows)
├── QUICKSTART.md           # This file
└── README.md               # Full documentation
```

---

## 🎯 Core Features

| Feature | Status | Module |
|---------|--------|--------|
| Sentiment Analysis | ✅ | `sentiment.py` |
| Keyword Extraction | ✅ | `keywords.py` |
| Text Summarization | ✅ | `summary.py` |
| Data Visualization | ✅ | `script.js` + Chart.js |
| Review Filtering | ✅ | `script.js` |
| Real-time Stats | ✅ | `script.js` |

---

## 🚀 Next Steps

1. ✅ Run the application
2. ✅ Enter sample reviews
3. ✅ Click "Analyze Reviews"
4. ✅ View results and chart
5. ✅ Filter by sentiment
6. ✅ Review the summary

---

## 📞 Need Help?

- Check [README.md](README.md) for detailed documentation
- See [api.md](#api-endpoints) for API reference
- Review code comments in Python files
- Check browser console for JavaScript errors
- Check terminal for Python errors

---

## 🎓 Learning Goals

After using this project, you'll understand:
- ✅ How sentiment analysis works
- ✅ How to extract keywords using TF-IDF
- ✅ How to summarize text with LSA
- ✅ How to build NLP pipelines
- ✅ How to create Flask APIs
- ✅ How to visualize data with Chart.js
- ✅ How to integrate frontend and backend

---

**Happy Analyzing! 🎉**
