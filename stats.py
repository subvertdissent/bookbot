from sys import argv

# get_book_text takes a file argument and parses the text.

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

# get_num_words counts total words in book

def get_num_words(a):
    num_words = 0 
    book_path = a
    read_book = get_book_text(a)
    book_text = read_book.split()
    for i in range(0, len(book_text)):
        num_words += 1
    return num_words   

# generated_dict generates a dictionary

def generated_dict(a):
    chars = {}
    read_book = get_book_text(a)
    book_path = read_book.lower().split()
    for char in book_path:
        for letter in char:
            if letter != chars:
                chars[letter] = 0
    return chars 

def get_char_count(a):
    chars = generated_dict(a)
    book_path = get_book_text(a).lower().split()
    for char in book_path:
        for letter in char:
            if letter in chars:
                chars[letter] += 1
    return chars

def sort_on(dict):
    return dict["num"]

def report(a):
    book = a
    char_report = get_char_count(a)
    sorted_chars = sorted(char_report.items(), key=lambda x:x[1], reverse=True)
    char_dict = dict(sorted_chars)
    word_count = get_num_words(a)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {a}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in char_dict:
        if i.isalpha():
            print(f"{i}: {char_dict[i]}")
    print("============= END ===============")
