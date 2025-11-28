import sys
from stats import get_num_words, count_characters, sort_on
def get_book_text(book_path):
    with open(book_path) as file:
        file_contents = file.read()
    return file_contents


def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    book_path = sys.argv[1]
    print("----------- Word Count ----------")
    text = get_book_text(book_path)
    msg = f"Found {get_num_words(text)} total words"
    print(msg)
    print("--------- Character Count -------")
    # print(count_characters(text))
    char_counts = count_characters(text)
    sorted_char_counts = sorted(
        [{"char": char, "count": count} for char, count in char_counts.items()],
        key=sort_on,
        reverse=True,
    )
    for item in sorted_char_counts:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        main()
        sys.exit(0)