import sys

from stats import get_num_words, get_chars_dict, sort_on, sort_letters

def main():
    try:
        sys.argv[1] != ""
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_dict = sort_letters(chars_dict)
    sorted_dict.sort(key=sort_on, reverse=True)
    for item in sorted_dict:
        if item["letter"].isalpha() is False:
            continue
        letter = item["letter"]
        num = item["num"]
        print(f"{letter}: {num}")
    print("============= END ===============")
    


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
