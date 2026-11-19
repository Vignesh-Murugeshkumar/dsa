class Solution(object):
    def findLongestWord(self, s, dictionary):
        char_indices = {}
        for i, ch in enumerate(s):
            if ch not in char_indices:
                char_indices[ch] = []
            char_indices[ch].append(i)

        def upper_bound(arr, target):
            low = 0
            high = len(arr)
            while low < high:
                mid = low + (high - low) // 2
                if arr[mid] <= target:
                    low = mid + 1
                else:
                    high = mid
            return low
        def is_subsequence(word):
            prev_idx = -1
            for ch in word:
                if ch not in char_indices:
                    return False
                indices = char_indices[ch]
                pos = upper_bound(indices, prev_idx)
                if pos == len(indices):
                    return False
                prev_idx = indices[pos]
            return True
        best_word = ""
        for word in dictionary:
            if len(word) < len(best_word):
                continue
            if len(word) == len(best_word) and word >= best_word:
                continue
            if is_subsequence(word):
                best_word = word
        return best_word

s="abpcplea"
dictionary=["ale","apple","monkey","plea"]
print(Solution().findLongestWord(s, dictionary))