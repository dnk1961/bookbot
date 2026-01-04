from stats import get_count_of_words, get_count_of_characters, sort_character_count
import sys

def get_book_text(filepath):
    with open(filepath) as book:
        book_contents = book.read()
        return book_contents

def main():
    print("Usage: python3 main.py <path_to_book>")
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...)")
    text = get_book_text(book_path)
    num_words = get_count_of_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_dict = get_count_of_characters(text)
    sorted_list = sort_character_count(char_dict)
    for i in sorted_list:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")

if __name__ == "__main__":
    main()
