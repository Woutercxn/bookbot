import sys
from stats import count_words, count_letters, sort_letter_counts

def get_book_text(path_to_file: str) -> str:
    with open(path_to_file, "r", encoding="utf-8") as f:
        content = f.read()
        return content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_file = sys.argv[1]

    text = get_book_text(path_to_file)
    wordcount = count_words(text)
    lettercount = count_letters(text)
    print(f"Found {wordcount} total words")
    # print("Found the following letter counts:")
    # for letter, count in lettercount.items():
    #    print(f" '{letter}': {count}")
        
    sorted_letters = sort_letter_counts(lettercount)
    print("Letters sorted by frequency:")
    for letter, count in sorted_letters:
        print(f" {letter}: {count}")

main()