def get_word_count(bookText):
    return len(bookText.split())

def getCharsDict(booktext):
    chars = {}
    for c in booktext:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def getSortedList(charDict):
    sortedList = []
    for ch in charDict:
        sortedList.append({"char": ch, "num": charDict[ch]})
    sortedList.sort(key=sort_on, reverse=True)
    return sortedList