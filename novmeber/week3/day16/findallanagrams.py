def findAnagrams(s: str, p: str) -> list[int]:
    if len(p) > len(s):
        return []
    need = {}
    for ch in p:
        need[ch] = need.get(ch, 0) + 1
    window = {}
    required = len(need)
    matched = 0
    result = []
    k = len(p)
    for right, ch in enumerate(s):
        window[ch] = window.get(ch, 0) + 1
        if ch in need and window[ch] == need[ch]:
            matched += 1
        if right >= k:
            left_ch = s[right - k]
            if left_ch in need and window[left_ch] == need[left_ch]:
                matched -= 1
            window[left_ch] -= 1
        if matched == required:
            result.append(right - k + 1)
    return result

s="cbaebabacd"
p="abc"
print(findAnagrams(s, p))