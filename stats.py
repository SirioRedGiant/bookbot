def word_counter(book_text):
    text_split_in_words = book_text.split()
    numb_of_words = len(text_split_in_words)
    return numb_of_words

def alphabet_counter(book_text):
    dictionary_counter = {}
    for character in book_text:
        minuscolo_character = character.lower()
        if minuscolo_character not in dictionary_counter:
            dictionary_counter[minuscolo_character] = 1
        else:
            dictionary_counter[minuscolo_character] += 1
    return dictionary_counter

def sort_on(dictionary_counter):
    return dictionary_counter["num"]

def report_list(dictionary_counter):
    list_of_character = []
    for key, value in dictionary_counter.items():
        if key.isalpha() == True:
            list_of_character.append({"char" : key, "num" : value})
    list_of_character.sort(reverse=True, key=sort_on)
    return list_of_character