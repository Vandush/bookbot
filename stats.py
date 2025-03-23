def wordCount(text):
    count = 0
    words = text.split()
    for i in words:
        count += 1
    return count

def characterCount(text):
    words = text.split()
    characters = {}
    for word in words:
        for character in word:
            if character.isalpha() == True:
                character = character.lower()
                if character in characters:
                    characters[character] += 1
                else:
                    characters[character] = 1
    return characters

def sort_on(dict):
    return dict["num"]

def characterSort(characters):
    newList = []
    result = []
    for i in characters:
        newPairs = {}
        newPairs["character"] = i
        newPairs["num"] = characters[i]
        newList.append(newPairs)
    newList.sort(reverse=True, key=sort_on)
    for d in newList:
        #print(d["character"])
        c = f"{d["character"]}: {d["num"]}"
        result.append(c)
    return result
