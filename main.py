def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def wordCount(text):
    count = 0
    words = text.split()
    for i in words:
        count += 1
    return count

#text = "Hello there world!"
#{num_words} words found in the document

def main():
    path = "books/frankenstein.txt"
    #print(get_book_text(path))
    text = (get_book_text(path))
    print(f"{wordCount(text)} words found in the document")
main()
