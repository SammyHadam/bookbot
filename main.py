def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = word_count(text)
    print(text)
    print(f"{count} words found in the document")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    counter = 0
    words = text.split()
    for word in words:
        counter += 1
    return counter

def character_count(text):
    words = text.split.lower()
    characters = words.split()


main()
