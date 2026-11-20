def longestNiceSubstring(s: str) -> str:
    n = len(s)
    if n < 2:
        return ""
    all_letters = {}
    for ch in s:
        all_letters[ch.lower()] = True
    max_unique = len(all_letters)
    best_start = 0
    best_len = 0
    for target_unique in range(1, max_unique + 1):
        lower_freq = {}
        upper_freq = {}
        unique_letters = 0
        nice_letters = 0
        left = 0
        for right, ch in enumerate(s):
            low = ch.lower()
            is_lower = "a" <= ch <= "z"
            prev_low = lower_freq.get(low, 0)
            prev_up = upper_freq.get(low, 0)
            if prev_low == 0 and prev_up == 0:
                unique_letters += 1
            if is_lower:
                lower_freq[low] = prev_low + 1
                if prev_low == 0 and prev_up > 0:
                    nice_letters += 1
            else:
                upper_freq[low] = prev_up + 1
                if prev_up == 0 and prev_low > 0:
                    nice_letters += 1
            while unique_letters > target_unique:
                l_ch = s[left]
                l_low = l_ch.lower()
                l_is_lower = "a" <= l_ch <= "z"
                cur_low = lower_freq.get(l_low, 0)
                cur_up = upper_freq.get(l_low, 0)
                if cur_low > 0 and cur_up > 0:
                    if (l_is_lower and cur_low == 1) or (not l_is_lower and cur_up == 1):
                        nice_letters -= 1
                if l_is_lower:
                    lower_freq[l_low] -= 1
                else:
                    upper_freq[l_low] -= 1
                if lower_freq.get(l_low, 0) == 0 and upper_freq.get(l_low, 0) == 0:
                    unique_letters -= 1
                left += 1
            if unique_letters == target_unique and nice_letters == target_unique:
                curr_len = right - left + 1
                if curr_len > best_len:
                    best_len = curr_len
                    best_start = left

    return s[best_start : best_start + best_len]

s="YazaAay"
print(longestNiceSubstring(s))