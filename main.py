def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = word_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document\n")
    character_count(text)
    print("--- End report ---")

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
        if char.isalpha():
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1

    list_of_letters = [{"char": char, "num": count} for char, count in letters.items()]
    def sort_on(letter):
        return letter["num"]
    
    list_of_letters.sort(reverse=True, key=sort_on)
    for alphs in list_of_letters:
        char = alphs["char"]
        count = alphs["num"]
        print(f"The '{char}' character was found {count} times")
    

main()

