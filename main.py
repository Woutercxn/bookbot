from stats import count_words

def get_book_text(path_to_file: str) -> str:
    with open(path_to_file, "r") as f:
        content = f.read()
        return content

def main():
    path_to_file = "books/frankenstein.txt"

    text = get_book_text(path_to_file)
    wordcount = count_words(text)
    print(f"Found {wordcount} total words")

main()