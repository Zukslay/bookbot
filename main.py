from stats import get_num_words
from stats import get_total_characters

path = "/home/fabrizio/workflow/github.com/bootdotdev/bookbot/books/frankenstein.txt"

def main():
    print("Found",get_num_words(path),"total words")
    print(get_total_characters(path))

main()

