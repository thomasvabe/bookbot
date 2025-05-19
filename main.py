import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    print(sys.argv)
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = count_words(text)
    dictionary = get_characters(text)
    print(f"{num_words} words found in the document")
    print(dictionary)
    char_counts = get_characters(text)
    sorted_chars = report(char_counts)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        # Only print alphabetical characters
        if char.isalpha():
            count = char_dict["num"]
            print(f"{char}: {count}")
    
    print("============= END ===============")

from stats import count_words

from stats import get_characters

from stats import report

main()