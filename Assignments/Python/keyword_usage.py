
def keyword_usage(words, list):
    words = words.split()
    result = []
    for word in list:
        result.append(word in words)
    return tuple (result)

