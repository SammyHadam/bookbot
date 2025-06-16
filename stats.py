def num_words(text):
    num = 0
    for word in text.split():
        num += 1
    print(f"{num} words found in the document")