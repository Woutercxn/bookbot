def get_book_text(path_to_file: str):
    with open(path_to_file, "r") as f:
        content = f.read()
        print(content)
# This code reads the content of the file "frankenstein.txt" located in the "books" directory 
# and prints it to the console.

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

    get_book_text(path_to_file)
    wordcount = count_words(path_to_file)
    print(f"Word count: {wordcount}")

main()