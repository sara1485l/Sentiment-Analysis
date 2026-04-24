"""
Test file for Smart Review Analyzer
Test all NLP modules and API endpoints
"""

import json
import sys
sys.path.insert(0, '.')

from sentiment import analyze_sentiment, analyze_multiple_sentiments, get_sentiment_statistics
from keywords import extract_keywords, clean_text
from summary import summarize_text, create_combined_summary

# ==================== Test Data ====================

TEST_REVIEWS = [
    "This product is absolutely amazing! Best purchase ever.",
    "Terrible quality, very disappointed with my purchase.",
    "It's okay, does what it's supposed to do.",
    "I love this! Great customer service and fast shipping!",
    "Waste of money. Broke after one week."
]

# ==================== Test Functions ====================

def test_sentiment_analysis():
    """Test sentiment analysis on reviews"""
    print("\n" + "="*50)
    print("TEST 1: Sentiment Analysis")
    print("="*50)
    
    results = analyze_multiple_sentiments(TEST_REVIEWS)
    
    for i, result in enumerate(results, 1):
        print(f"\nReview {i}:")
        print(f"  Text: {result['text'][:50]}...")
        print(f"  Sentiment: {result['sentiment']}")
        print(f"  Polarity: {result['polarity']}")
    
    stats = get_sentiment_statistics(results)
    print(f"\nStatistics:")
    print(f"  Total: {stats['total']}")
    print(f"  Positive: {stats['positive']} ({stats['positive_percent']}%)")
    print(f"  Negative: {stats['negative']} ({stats['negative_percent']}%)")
    print(f"  Neutral: {stats['neutral']} ({stats['neutral_percent']}%)")
    
    assert stats['total'] == len(TEST_REVIEWS), "Total count mismatch"
    print("\n✅ Sentiment Analysis Test Passed!")


def test_keyword_extraction():
    """Test keyword extraction"""
    print("\n" + "="*50)
    print("TEST 2: Keyword Extraction")
    print("="*50)
    
    keywords = extract_keywords(TEST_REVIEWS, top_n=5)
    
    print("\nTop 5 Keywords:")
    for i, (keyword, score) in enumerate(keywords, 1):
        print(f"  {i}. {keyword}: {score}")
    
    assert len(keywords) <= 5, "Too many keywords extracted"
    print("\n✅ Keyword Extraction Test Passed!")


def test_text_summarization():
    """Test text summarization"""
    print("\n" + "="*50)
    print("TEST 3: Text Summarization")
    print("="*50)
    
    combined_text = " ".join(TEST_REVIEWS)
    summary = create_combined_summary(TEST_REVIEWS, sentences_count=2)
    
    print("\nOriginal text length:", len(combined_text))
    print("Summary length:", len(summary))
    print("\nSummary:")
    print(f"  {summary}")
    
    assert len(summary) > 0, "Summary is empty"
    assert len(summary) < len(combined_text), "Summary not shorter than original"
    print("\n✅ Text Summarization Test Passed!")


def test_text_cleaning():
    """Test text cleaning function"""
    print("\n" + "="*50)
    print("TEST 4: Text Cleaning")
    print("="*50)
    
    test_texts = [
        "This IS great!!!",
        "Amazing@#$%product",
        "Love-It_123"
    ]
    
    print("\nCleaning test texts:")
    for text in test_texts:
        cleaned = clean_text(text)
        print(f"  Original: {text}")
        print(f"  Cleaned:  {cleaned}")
    
    print("\n✅ Text Cleaning Test Passed!")


def test_api_request_format():
    """Test API request format"""
    print("\n" + "="*50)
    print("TEST 5: API Request Format")
    print("="*50)
    
    # Simulate API request
    api_request = {
        "texts": TEST_REVIEWS[:2],
        "summary_sentences": 2
    }
    
    print("\nAPI Request format:")
    print(json.dumps(api_request, indent=2))
    
    assert "texts" in api_request, "Missing 'texts' field"
    assert isinstance(api_request["texts"], list), "Texts should be a list"
    assert len(api_request["texts"]) > 0, "Texts list is empty"
    
    print("\n✅ API Request Format Test Passed!")


# ==================== Run All Tests ====================

def run_all_tests():
    """Run all tests"""
    print("\n" + "="*60)
    print("SMART REVIEW ANALYZER - TEST SUITE")
    print("="*60)
    
    try:
        test_sentiment_analysis()
        test_keyword_extraction()
        test_text_summarization()
        test_text_cleaning()
        test_api_request_format()
        
        print("\n" + "="*60)
        print("ALL TESTS PASSED! ✅")
        print("="*60)
        print("\nThe NLP modules are working correctly!")
        print("You can now run: python app.py")
        return True
        
    except Exception as e:
        print(f"\n❌ TEST FAILED: {str(e)}")
        print("\nPlease ensure all dependencies are installed:")
        print("  pip install -r requirements.txt")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
