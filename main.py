def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = word_count(text)
    char_count = character_count(text)
    print(text)
    print(f"{count} words found in the document")
    print(f"{char_count}")

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
    letters = {}
    characters = text.lower()
    for char in characters:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters

main()

