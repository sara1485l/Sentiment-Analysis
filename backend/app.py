"""
Smart Review Analyzer - Flask Backend
Main application file that integrates all NLP modules
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from sentiment import analyze_multiple_sentiments, get_sentiment_statistics
from keywords import extract_keywords, highlight_keywords_in_text, clean_text
from summary import create_combined_summary

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication


@app.route('/', methods=['GET'])
def home():
    """Welcome endpoint"""
    return jsonify({
        "message": "Smart Review Analyzer API",
        "version": "1.0",
        "endpoints": {
            "POST /analyze": "Analyze reviews",
            "GET /health": "Health check"
        }
    })


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy"}), 200


@app.route('/analyze', methods=['POST'])
def analyze():
    """
    Main analysis endpoint
    
    Expected JSON request:
    {
        "texts": ["review1", "review2", ...],
        "summary_sentences": 2 (optional)
    }
    
    Returns:
    {
        "sentiments": [...],
        "statistics": {...},
        "keywords": [...],
        "summary": "...",
        "success": true
    }
    """
    try:
        # Get JSON data
        data = request.get_json()
        
        if not data or 'texts' not in data:
            return jsonify({
                "error": "Missing 'texts' field in request",
                "success": False
            }), 400
        
        texts = data.get('texts', [])
        summary_sentences = data.get('summary_sentences', 2)
        
        # Validate texts
        if not texts or len(texts) == 0:
            return jsonify({
                "error": "Texts list is empty",
                "success": False
            }), 400
        
        # Filter out empty strings
        texts = [t.strip() for t in texts if t.strip()]
        
        if len(texts) == 0:
            return jsonify({
                "error": "No valid texts provided",
                "success": False
            }), 400
        
        # 1. Sentiment Analysis
        sentiments = analyze_multiple_sentiments(texts)
        statistics = get_sentiment_statistics(sentiments)
        
        # 2. Keyword Extraction
        keywords = extract_keywords(texts, top_n=5)
        
        # 3. Text Summarization
        summary = create_combined_summary(texts, sentences_count=summary_sentences)
        
        # Prepare response
        response = {
            "success": True,
            "analysis": {
                "sentiments": sentiments,
                "statistics": statistics,
                "keywords": [{"word": kw[0], "score": kw[1]} for kw in keywords],
                "summary": summary,
                "total_reviews": len(texts)
            }
        }
        
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({
            "error": str(e),
            "success": False
        }), 500


@app.route('/analyze-single', methods=['POST'])
def analyze_single():
    """
    Analyze a single review with keyword highlighting
    
    Expected JSON request:
    {
        "text": "review text"
    }
    """
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({
                "error": "Text is empty",
                "success": False
            }), 400
        
        # Analyze
        sentiments = analyze_multiple_sentiments([text])
        keywords = extract_keywords([text], top_n=5)
        
        # Highlight keywords
        highlighted_text = highlight_keywords_in_text(text, keywords)
        
        response = {
            "success": True,
            "text": text,
            "highlighted_text": highlighted_text,
            "sentiment": sentiments[0],
            "keywords": [{"word": kw[0], "score": kw[1]} for kw in keywords]
        }
        
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({
            "error": str(e),
            "success": False
        }), 500


@app.route('/keywords', methods=['POST'])
def get_keywords():
    """
    Extract keywords from provided texts
    
    Expected JSON request:
    {
        "texts": ["text1", "text2"],
        "top_n": 5
    }
    """
    try:
        data = request.get_json()
        texts = data.get('texts', [])
        top_n = data.get('top_n', 5)
        
        if not texts:
            return jsonify({
                "error": "Texts list is empty",
                "success": False
            }), 400
        
        keywords = extract_keywords(texts, top_n=top_n)
        
        response = {
            "success": True,
            "keywords": [{"word": kw[0], "score": kw[1]} for kw in keywords]
        }
        
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({
            "error": str(e),
            "success": False
        }), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )
