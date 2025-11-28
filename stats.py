from collections import Counter
def get_num_words(text):
    """Count the number of words in a given text."""
    words = text.split()
    return len(words)
def count_characters(text):
    """Count the number of characters in a given text."""
    text = text.lower()
    return Counter(text)
def sort_on(items):
    return items["count"]
