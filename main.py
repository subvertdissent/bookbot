import sys
from sys import argv
from stats import report, get_num_words, generated_dict, get_char_count, get_book_text 

if len(argv) < 2:
    sys.exit("Usage: python3 main.py <path_to_book>")

book_path = argv[1]

def main(a):
    if len(book_path) < 1: 
        sys.exit("huh")    
    else:
        report(book_path)

main(book_path)

