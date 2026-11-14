def is_prefix_string(s: str, words: list[str]) -> bool:
    idx = 0
    n = len(s)
    for word in words:
        # If the current word extends past the end of s, it cannot be an exact prefix concatenation
        if idx + len(word) > n:
            return False
        for i in range(len(word)):
            if s[idx + i] != word[i]:
                return False
        idx += len(word)
        if idx == n:
            return True
    return False
print(is_prefix_string("iloveleetcode", ["i", "love", "leetcode", "apples"]))  