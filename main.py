# python
from stats import get_num_words, get_char_count, sorted_dict
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_path)} total words")
    print("--------- Character Count -------")
    sorted_list_of_char_and_count = sorted_dict(get_char_count(book_path))
    for item in sorted_list_of_char_and_count:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()

