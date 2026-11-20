def countGoodSubstrings(s: str) -> int:
    if len(s) < 3:
        return 0
    window = {}
    distinct_count = 0
    good_substrings = 0
    left = 0
    for right, ch in enumerate(s):
        window[ch] = window.get(ch, 0) + 1
        if window[ch] == 1:
            distinct_count += 1
        if right - left + 1 == 3:
            if distinct_count == 3:
                good_substrings += 1
            left_ch = s[left]
            window[left_ch] -= 1
            if window[left_ch] == 0:
                distinct_count -= 1
            left += 1
    return good_substrings
s="xyzzaz"
print(countGoodSubstrings(s))