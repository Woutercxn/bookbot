def get_book_text(path_to_file: str) -> str:
    with open(path_to_file, "r") as f:
        content = f.read()
        return content

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

def main():
    path_to_file = "books/frankenstein.txt"

    text = get_book_text(path_to_file)
    wordcount = count_words(text)
    print(f"Word count: {wordcount}")

main()