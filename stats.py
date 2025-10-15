def count_words(text: str) -> int:
    """
    Count the number of words in the given text string.
    
    Args:
        text (str): The text string to count words in
        
    Returns:
        int: The number of words in the text
    """
    words = text.split()
    return len(words)