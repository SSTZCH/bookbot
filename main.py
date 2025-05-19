from stats import get_num_words, get_character_count, sort_character

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(book_text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    counts = get_character_count(book_text)
    listing = sort_character(counts)
    for item in listing:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()