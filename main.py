import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_count_chars(text)
    print(f"{num_words} words found in this document")
    print(chars_dict)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_count_chars(text):
    chars_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in string.ascii_lowercase:
            chars_dict[lowered] = chars_dict.get(lowered, 0) + 1
    return chars_dict

main()