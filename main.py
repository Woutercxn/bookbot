def get_book_text(path_to_file: str):
    with open(path_to_file, "r") as f:
        content = f.read()
        print(content)
# This code reads the content of the file "frankenstein.txt" located in the "books" directory 
# and prints it to the console.

def main():
    path_to_file = "books/frankenstein.txt"
    get_book_text(path_to_file)

main()