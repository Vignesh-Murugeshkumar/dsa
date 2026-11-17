class TrieNode:
    __slots__ = ("children", "count")
    def __init__(self):
        self.children = {}
        self.count = 0

def sum_prefix_scores(words: list[str]) -> list[int]:
    root = TrieNode()
    for w in words:
        curr = root
        for ch in w:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
            curr.count += 1

    ans = []
    for w in words:
        curr = root
        score = 0
        for ch in w:
            curr = curr.children[ch]
            score += curr.count
        ans.append(score)
    return ans

words = ["abciiiiidef", "abciii", "abc"]
print(sum_prefix_scores(words))  