from stats import get_num_words
from stats import get_total_characters
from stats import sorted_characters
import sys 

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]
temp_dict = sorted_characters(path)

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found",get_num_words(path),"total words")
    print("--------- Character Count -------")
    for a,b in temp_dict.items():
        print(f"{a}: {b}")
    print("============= END ===============")

main()

