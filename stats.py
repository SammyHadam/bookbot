def num_words(text):
    return len(text.split())

def num_characters(text):
    characters_dict = {}
    for char in text.lower():
        if char not in characters_dict:
            characters_dict[char] = 1
        else:
            characters_dict[char] += 1
    return characters_dict

def sorted_num_of_chars(dict):
    sorted_dict = {}
    