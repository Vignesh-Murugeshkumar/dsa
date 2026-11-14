def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""

    prefix_chars = []
    first = strs[0]

    for i in range(len(first)):
        char = first[i]
        for s in strs[1:]:
            # Stop if string is shorter or characters diverge
            if i == len(s) or s[i] != char:
                return "".join(prefix_chars)
        prefix_chars.append(char)

    return "".join(prefix_chars)
s=["flower","flow","flight"]
print(longestCommonPrefix(s))