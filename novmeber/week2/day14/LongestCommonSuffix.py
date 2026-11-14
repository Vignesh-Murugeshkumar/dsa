def longest_common_suffix(strs: list[str]) -> str:
    if not strs:
        return ""
    first = strs[0]
    n = len(first)
    for offset in range(1, n + 1):
        char = first[-offset]
        for s in strs[1:]:
            if offset > len(s) or s[-offset] != char:
                # If offset == 1, no characters matched at all
                return "" if offset == 1 else first[-(offset - 1):]
    return first
print(longest_common_suffix(["running", "jogging", "walking"]))  # Output: "ing"
