from stats import count_words, count_characters, sort_count
import sys

# Fetch the full text of the chosen book
def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()
        return book_text

def main():
    print("======== WELCOME TO BOOKBOT ========")
    
    #Check if book path arg has been provided, otherwise exit
    if(len(sys.argv) < 2):
        print("Sorry, it looks like you didn't provide the path to the book")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print(f"Analyzing the book found at {sys.argv[1]}.....")
    full_text = get_book_text(sys.argv[1])

    #getting word count
    word_count = count_words(full_text)
    print("-------- Word Count --------")

    print(f"Found {word_count} total words")

    print("-------- Character Count --------")
    #counting characters
    total_characters = count_characters(full_text)

    #sort the character counts into new list of dicts
    sorted_counts = sort_count(total_characters)
    for item in sorted_counts:
        #check to make sure we're only printing alphanumeric chars
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("======== END ========")
main()

