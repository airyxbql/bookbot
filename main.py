def main():
    text = get_text("books/frankenstein.txt")
    word_count = count_words(text)
    letter_count = sorted(
        filter(lambda el: el[0].isalpha(),
               list(char_count(text).items())))

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for letter, count in letter_count:
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")


def count_words(text):
    return len(text.split())

def get_text(filename):
    with open(filename) as f:
        text = f.read()
    return text

def char_count(text):
    counts = {}
    for char in text:
        char = char.lower()
        if char not in counts:
            counts[char] = 0
        counts[char] += 1
    return counts

main()