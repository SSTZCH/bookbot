from stats import get_num_words, get_character_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")
    counts = get_character_count(book_text)
    print(counts)

main()