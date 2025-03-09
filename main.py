def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

from stats import wordCount

def main():
    path = "books/frankenstein.txt"
    #print(get_book_text(path))
    text = (get_book_text(path))
    print(f"{wordCount(text)} words found in the document")
main()
