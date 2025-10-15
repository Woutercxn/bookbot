path_to_file = "books/frankenstein.txt"

with open(path_to_file, "r") as f:
    content = f.read()
    print(content)
# This code reads the content of the file "frankenstein.txt" located in the "books" directory 
# and prints it to the console.