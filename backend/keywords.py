"""
Keyword Extraction Module
Uses TF-IDF (scikit-learn) to extract important keywords from reviews
"""




def clean_text(text):
    """
    Clean text by removing special characters and converting to lowercase
    
    Args:
        text (str): Input text
        
    Returns:
        str: Cleaned text
    """
    # Convert to lowercase
    text = text.lower()
    # Remove special characters and digits
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text


from collections import Counter
import re

def extract_keywords(texts, top_n=5):
    if not texts:
        return []

    # دمج كل النصوص
    text = " ".join(texts).lower()

    # تنظيف
    words = re.findall(r'\w+', text)

    # stopwords بسيطة
    stopwords = {
        "the","is","and","a","to","in","of","it","this","that",
        "with","for","on","was","are","as","but","be","have"
    }

    words = [w for w in words if w not in stopwords and len(w) > 2]

    counts = Counter(words)

    top = counts.most_common(top_n)

    # نفس شكل output القديم
    return [(word, round(count / len(words), 3)) for word, count in top]


def highlight_keywords_in_text(text, keywords):
    """
    Highlight keywords in text for frontend display
    
    Args:
        text (str): Original text
        keywords (list): List of keywords to highlight
        
    Returns:
        str: Text with keywords wrapped in HTML tags
    """
    highlighted_text = text
    keyword_list = [kw[0] for kw in keywords]
    
    for keyword in keyword_list:
        # Case-insensitive replacement with highlight
        pattern = re.compile(re.escape(keyword), re.IGNORECASE)
        highlighted_text = pattern.sub(f'<mark>{keyword}</mark>', highlighted_text)
    
    return highlighted_text
