def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

from stats import wordCount
from stats import characterCount
from stats import characterSort

def main():
    path = "books/frankenstein.txt"
    #print(get_book_text(path))
    text = (get_book_text(path))
    word_count = wordCount(text)
    character_count = characterCount(text)
    print(f"Found {word_count} total words")
    #print(character_count)
    #characterSort(character_count)
    print(characterSort(character_count))
main()
