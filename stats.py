def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def get_num_words():
    num_words = 0 
    book_string = get_book_text("/home/dennisb/Projects/gopherus/subvertdissent/bookbot/books/frankenstein.txt")
    book_text = book_string.split()
    for i in range(0, len(book_text)):
        num_words += 1
    print(f"{num_words} words found in the document")

def get_char_count():
    chars  = {
            "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0,
            "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0,
            "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
            }
