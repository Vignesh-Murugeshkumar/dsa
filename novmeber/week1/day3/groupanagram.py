def groupAnagrams(strs: list[str]) -> list[list[str]]:
    groups = {}

    for word in strs:
        # 26 slots for 'a' through 'z'
        count = [0] * 26
        for ch in word:
            count[ord(ch) - ord('a')] += 1

        # Tuples are immutable and hashable, making them valid dict keys
        signature = tuple(count)
        
        if signature not in groups:
            groups[signature] = []
        groups[signature].append(word)

    return list(groups.values())