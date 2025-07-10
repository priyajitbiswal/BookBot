import sys
from stats import count_words, count_characters, sort_characters_by_count


def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)

    if book_text:
        # Word count
        num_words = count_words(book_text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")

        # Character count
        char_count = count_characters(book_text)

        # Sort the character counts
        sorted_char_counts = sort_characters_by_count(char_count)
        print("--------- Character Count -------")

        # Print the sorted character counts
        for char_info in sorted_char_counts:
            print(f"{char_info['char']}: {char_info['num']}")

        print("============= END ===============")


if __name__ == "__main__":
    main()
