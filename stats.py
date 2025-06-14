def get_num_words(book_text):
    list_of_words = book_text.split()
    num_words = len(list_of_words)
    return num_words

def get_character_count(book_text):
    book_text = book_text.lower()
    counts = {}
    for char in book_text:
        if char in counts:
            counts[char] = counts[char] + 1
        else:
            counts[char] = 1
    return counts

def sort_character(dict):
    listing = []
    for key, value in dict.items():
        listing.append({"char" : key, "num" : value})
    listing.sort(reverse=True, key=lambda item: item["num"])
    return listing