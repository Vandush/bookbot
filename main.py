import sys

try:
    x, y = sys.argv
    path = y
except Exception as e:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

from stats import wordCount
from stats import characterCount
from stats import characterSort

def main():
    text = (get_book_text(path))
    word_count = wordCount(text)
    character_count = characterCount(text)
    print(f"Found {word_count} total words")
    print(characterSort(character_count))
main()
