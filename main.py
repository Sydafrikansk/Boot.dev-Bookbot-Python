from stats import get_word_count, getCharsDict, getSortedList
import sys



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    try:
        bookText = get_book_text(path)
    except FileNotFoundError:
        print(f"Error! Not a valid path: {path}")
        sys.exit(2)
    numWords = get_word_count(bookText)
    charDict = getCharsDict(bookText)
    sortedList = getSortedList(charDict)
    printReport(path, numWords, sortedList)



def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()
    

def printReport(path, num_words, sortedList):
    print(
f"""============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    for char in sortedList:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
        else:
            pass
    print("============= END ===============")



if __name__ == "__main__":
    main()