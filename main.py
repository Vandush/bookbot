def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

from stats import wordCount
from stats import characterCount

def main():
    path = "books/frankenstein.txt"
    #print(get_book_text(path))
    text = (get_book_text(path))
    word_count = wordCount(text)
    character_count = characterCount(text)
    print(f"{word_count} words found in the document")
    print(character_count)
main()
