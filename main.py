from stats import get_num_words
from stats import get_num_letters
from stats import sort_letters
import sys
def main():

    if len(sys.argv) == 2:
        book = sys.argv[1]  
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}...")
        get_num_words(book)
        sort_letters(get_num_letters(book))
        return
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
        return





main()
