def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""
    first = strs[0]
    for i in range(len(first)):
        char = first[i]
        for s in strs[1:]:
            if i == len(s) or s[i] != char:
                return first[:i]

    return first
print(longest_common_prefix(["flower", "flow", "flight"])) 