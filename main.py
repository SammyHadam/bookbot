from stats import num_words, num_characters, sorted_num_of_chars
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    chars_dict = num_characters(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words(text)} total words")

    sorted_list_of_dict = sorted_num_of_chars(chars_dict)

    for item in sorted_list_of_dict:
        letter = item['char']
        count = item['num']
        if letter.isalpha():
            print(f"{letter}: {count}")
    
    print("============= END ===============")



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    

main()