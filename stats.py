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

def count_letters(text: str) -> dict:
    """
    Count the occurrences of each letter in the given text string.

    Args:
        text (str): The text string to count letters in

    Returns:
        dict: A dictionary with letters as keys and their counts as values
    """
    letter_counts = {}
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            letter_counts[char_lower] = letter_counts.get(char_lower, 0) + 1
    return letter_counts