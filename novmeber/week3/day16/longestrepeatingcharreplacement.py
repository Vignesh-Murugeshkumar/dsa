def characterReplacement(s: str, k: int) -> int:
    freq = {}
    left = 0
    max_freq = 0
    max_len = 0
    for right, ch in enumerate(s):
        freq[ch] = freq.get(ch, 0) + 1
        max_freq = max(max_freq, freq[ch])
        if (right - left + 1) - max_freq > k:
            left_ch = s[left]
            freq[left_ch] -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
s = "AABABBA"
k = 1
print(characterReplacement(s, k))