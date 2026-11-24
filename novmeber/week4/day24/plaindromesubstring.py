def count_substrings(s: str) -> int:
    total = 0
    def expand_count(left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    for i in range(len(s)):
        total += expand_count(i, i)       
        total += expand_count(i, i + 1)   
    return total

s = "ababaccc"
print(count_substrings(s))