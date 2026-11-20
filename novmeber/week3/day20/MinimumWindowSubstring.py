def minWindow(s: str, t: str) -> str:
    if not s or not t or len(s) < len(t):
        return ""
    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1
    required = len(need)
    formed = 0
    window = {}
    left = 0
    min_len = float("inf")
    min_start = 0
    for right, ch in enumerate(s):
        window[ch] = window.get(ch, 0) + 1
        if ch in need and window[ch] == need[ch]:
            formed += 1
        while left <= right and formed == required:
            curr_len = right - left + 1
            if curr_len < min_len:
                min_len = curr_len
                min_start = left
            left_ch = s[left]
            window[left_ch] -= 1
            if left_ch in need and window[left_ch] < need[left_ch]:
                formed -= 1
            left += 1
    if min_len == float("inf"):
        return ""
    return s[min_start : min_start + min_len]
s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))  