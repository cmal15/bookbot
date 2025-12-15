import sys
from stats import get_book_text, count_text_words, count_text_characters, sort_on

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    text_book = get_book_text(path)
    num_words = count_text_words(text_book)
    char_list = count_text_characters(text_book)

    char_list.sort(reverse=True, key=sort_on)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")

    for item in char_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()