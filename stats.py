#Functions for analyzing the text

def count_words(book_text):
    num_words = len(book_text.split())
    return num_words

def count_characters(book_text):
    char_count = {}
    for char in book_text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return (char_count)

#helper function to sort by number of characters
def sort_on(item):
    return item["num"]

def sort_count(char_count):
    list_of_dicts = []
    #split the dictionary into list of new dicts
    for char, count in char_count.items():
        sorted_count = {"char": char, "num": count}
        list_of_dicts.append(sorted_count)
    
    #sort the list by count
    list_of_dicts.sort(reverse=True, key=sort_on)
    
    return list_of_dicts 
