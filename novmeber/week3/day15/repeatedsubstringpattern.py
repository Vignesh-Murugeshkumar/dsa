def repeatedSubstringPattern(s: str) -> bool:
    n = len(s)
    if n <= 1:
        return False

    # Construct (s + s) without the first and last character
    doubled = (s + s)[1:-1]
    
    # Use our nested-loop strStr to check if s exists inside doubled
    return strStr(doubled, s) != -1
def strStr(haystack: str, needle: str) -> int:
    n, m = len(haystack), len(needle)
    if m == 0:
        return 0
    for i in range(n - m + 1):
        j = 0
        while j < m and haystack[i + j] == needle[j]:
            j += 1
        if j == m:
            return i
    return -1


s = "abab"
print(repeatedSubstringPattern(s))