def lengthOfLongestSubstring(s: str) -> int:
    freq = {}
    left = 0
    max_len = 0
    for right, ch in enumerate(s):
        freq[ch] = freq.get(ch, 0) + 1
        while freq[ch] > 1:
            left_ch = s[left]
            freq[left_ch] -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

s = "abcabcbb"
print(lengthOfLongestSubstring(s))
