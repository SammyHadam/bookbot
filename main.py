from stats import num_words, num_characters

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    chars_dict = num_characters(text)
    print(f"{num_words(text)} words found in the document")
    print(chars_dict)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    

main()