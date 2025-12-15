def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def count_text_words(text):
    return len(text.split())

def count_text_characters(text):
    char_count = {}

    text = text.lower()

    for char in text:
        if not char.isalpha():
            continue
        char_count[char] = char_count.get(char,0) + 1        

    dict_char_list = []

    for char in char_count:
        item = {"char":char, "num":char_count[char]}
        dict_char_list.append(item)

    return dict_char_list

def sort_on(dict_item):
    return dict_item["num"]

