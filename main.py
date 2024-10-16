import string

def main():
    book_path = input("Enter path here: ")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = get_count_chars(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} found in this document")

    for letter, count in chars.items():
        print(f"We found the letter '{letter}' {count} times")
    
    print("--- End of report ---")

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
    
    sorted_chars = sorted(chars_dict.items())
    return dict(sorted_chars)

main()