def wordCount(text):
    count = 0
    words = text.split()
    for i in words:
        count += 1
    return count
