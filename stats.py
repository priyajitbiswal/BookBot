def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    char_count = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count


def sort_characters_by_count(char_count):
    sorted_chars = [{"char": char, "num": count} for char, count in char_count.items()]
    sorted_chars.sort(reverse=True, key=lambda item: item["num"])
    return sorted_chars
