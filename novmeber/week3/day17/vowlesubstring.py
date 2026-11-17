def count_vowel_substrings(word: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    last_seen = {v: -1 for v in vowels}
    last_consonant = -1
    total = 0
    for i, ch in enumerate(word):
        if ch in vowels:
            last_seen[ch] = i
            earliest_vowel = min(last_seen.values())
            if earliest_vowel > last_consonant:
                total += earliest_vowel - last_consonant
        else:
            last_consonant = i
    return total

s="aeiouu"
print(count_vowel_substrings(s))