from stats import get_word_count, char

def main():
	path_to_file = "books/frankenstein.txt"
	text = get_book_text(path_to_file)
	sortedList = sortCharList()
	printReport(path_to_file, text)

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		return f.read()

def printReport(path, text):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}")
	print("----------- Word Count ----------")
	print(f"Found {get_word_count(text)} total words")
	print("-------- Character Count --------")
	for char in sortedList:
		if not char.isalpha():
			continue
		else
			print(f"{char}: {sortedList[ch["num"]]}")

	
if __name__ == "__main__":
	main()