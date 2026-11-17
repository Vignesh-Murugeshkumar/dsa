def vowel_ranges(s: str, queries: list[list[int]]) -> list[int]:
    vowels = set("aeiouAEIOU")
    n = len(s)
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + (1 if s[i] in vowels else 0)
    ans = []
    for l, r in queries:
        ans.append(pref[r + 1] - pref[l])
    return ans
s="leetcode"
queries=[[0, 1], [0, 2], [0, 3]]
print(vowel_ranges(s, queries))