def buddyStrings(s:str,goal:str)-> bool:
    if len(s)!=len(goal):
        return False
    if s == goal:
        seen = set()
        for ch in s:
            if ch in seen:
                return True
            seen.add(ch)
        return False
    mismatches = []
    for i in range(len(s)):
        if s[i]!=goal[i]:
            mismatches.append(i)
    return (
        len(mismatches)==2
        and s[mismatches[0]]==goal[mismatches[1]]
        and s[mismatches[1]]==goal[mismatches[0]]
    )

print(buddyStrings("ab", "ba"))
