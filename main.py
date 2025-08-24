import sys
from stats import word_count, char_count, sort_char_count
def get_book_text(filepath):
    with open(filepath) as f:
        cont = f.read()
    return cont

def main ():
    if len(sys.argv) == 1:
        print (f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    # path = "books/frankenstein.txt"
    book = get_book_text(path)
    sorted = sort_char_count(char_count(book))
    print (f"""============ BOOKBOT ============
    Analyzing book found at {path}...
    ----------- Word Count ----------
    Found {len(word_count(book))} total words
    --------- Character Count -------""")
    for entry in sorted:
        print (f"{entry["char"]}: {entry["num"]}")
    
main()