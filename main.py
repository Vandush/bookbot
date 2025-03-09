def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents



def main():
    path = "books/frankenstein.txt"
    print(get_book_text(path))
main()
