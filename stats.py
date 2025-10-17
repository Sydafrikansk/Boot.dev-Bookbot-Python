def get_word_count(text):	
	return len(text.split())

def char(book):
    numChar = {}
    for c in book:
        lowered = c.lower()
        if lowered in numChar:
            numChar[lowered] += 1
        else:
            numChar[lowered] = 1
    return numChar

def sort_on(list):
    return list['num']

def sortCharList(list):
    sortedList =[]
    for char in list:
        sortedList.append({"ch": char, "num": list[char]})
        sortedList.sort(key=sort_on, reverse=True)
    return sortedList