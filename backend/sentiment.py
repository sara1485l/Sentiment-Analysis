"""
Sentiment Analysis Module
Uses TextBlob to classify text sentiment as Positive, Negative, or Neutral
"""

from textblob import TextBlob


def analyze_sentiment(text):
    """
    Analyze sentiment of a given text
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        dict: Contains polarity score and sentiment label
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # Range: -1 (negative) to 1 (positive)
    
    # Classify based on polarity
    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return {
        "sentiment": sentiment,
        "polarity": round(polarity, 3),
        "text": text
    }


def analyze_multiple_sentiments(texts):
    """
    Analyze sentiment for multiple texts
    
    Args:
        texts (list): List of text strings
        
    Returns:
        list: List of sentiment analysis results
    """
    results = [analyze_sentiment(text) for text in texts]
    return results


def get_sentiment_statistics(sentiments):
    """
    Calculate sentiment statistics
    
    Args:
        sentiments (list): List of sentiment results
        
    Returns:
        dict: Statistics with counts and percentages
    """
    total = len(sentiments)
    positive = sum(1 for s in sentiments if s["sentiment"] == "Positive")
    negative = sum(1 for s in sentiments if s["sentiment"] == "Negative")
    neutral = sum(1 for s in sentiments if s["sentiment"] == "Neutral")
    
    return {
        "total": total,
        "positive": positive,
        "negative": negative,
        "neutral": neutral,
        "positive_percent": round((positive / total * 100), 2) if total > 0 else 0,
        "negative_percent": round((negative / total * 100), 2) if total > 0 else 0,
        "neutral_percent": round((neutral / total * 100), 2) if total > 0 else 0
    }
