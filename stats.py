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
#        word = word.lower
#        print(word)
        for character in word:
            character = character.lower()
            #print(character)
            if character in characters:
                characters[character] += 1
            else:
                characters[character] = 1
    return characters
    #for i in words:
        #print(i)
