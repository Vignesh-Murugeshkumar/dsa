def countWords(words1: list[str], words2: list[str]) -> int:
    counts1 = {}
    counts2 = {}

    for word in words1:
        counts1[word] = counts1.get(word, 0) + 1

    for word in words2:
        counts2[word] = counts2.get(word, 0) + 1

    count = 0
    for word in counts1:
        if counts1[word] == 1 and counts2.get(word, 0) == 1:
            count += 1

    return count


words1 = ["leetcode", "is", "amazing", "as", "is"]
words2 = ["amazing", "leetcode", "is"]
print(countWords(words1, words2))
