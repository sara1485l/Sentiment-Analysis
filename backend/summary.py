"""
Text Summarization Module
Uses sumy library with LSA Summarizer for text summarization
"""

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer


def summarize_text(text, sentences_count=2):
    """
    Summarize a text document
    
    Args:
        text (str): Input text to summarize
        sentences_count (int): Number of sentences in summary
        
    Returns:
        str: Summarized text
    """
    if not text or len(text.strip()) < 50:
        return text
    
    try:
        # Create parser and tokenizer
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        
        # Create summarizer
        stemmer = Stemmer("english")
        summarizer = LsaSummarizer(stemmer)
        
        # Generate summary
        summary_sentences = summarizer(parser.document, sentences_count)
        summary = " ".join(str(sentence) for sentence in summary_sentences)
        
        return summary if summary else text[:200] + "..."
    except:
        # Fallback: return first 200 characters if summarization fails
        return text[:200] + "..."


def summarize_multiple(texts, sentences_count=2):
    """
    Summarize multiple texts
    
    Args:
        texts (list): List of texts to summarize
        sentences_count (int): Number of sentences per summary
        
    Returns:
        list: List of summaries
    """
    summaries = [summarize_text(text, sentences_count) for text in texts]
    return summaries


def create_combined_summary(texts, sentences_count=3):
    """
    Create a single summary from multiple texts combined
    
    Args:
        texts (list): List of review texts
        sentences_count (int): Number of sentences in final summary
        
    Returns:
        str: Combined summary
    """
    if not texts or len(texts) == 0:
        return ""
    
    # Combine all texts
    combined_text = " ".join(texts)
    return summarize_text(combined_text, sentences_count)
