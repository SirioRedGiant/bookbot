import sys
from stats import word_counter, alphabet_counter, report_list

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        # se non vengono passati gli argomenti
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) #esce dal programma

    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    number_counter = word_counter(book_text)
    dictionary_alphabet_counter = alphabet_counter(book_text)
    book_report = report_list(dictionary_alphabet_counter)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count -----------")
    print(f"Found {number_counter} total words")
    print("--------- Character Count ---------")
    for dictonary in book_report:
        character = dictonary["char"]
        counter = dictonary["num"]
        print(f"{character}: {counter}")
    print("============= END =============")
main()
