class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count={}
        maxCount=0
        start=0
        for end in range(len(s)):
            currentChar=s[end]
            if currentChar in count and count.get(currentChar)>=start: #checks whether the char is already there and the index of the char is gt start
                start=count[currentChar]+1 #update the start index to the next index of the current char
            count[currentChar]=end #the current char always gets updated to the latest index
            maxCount=max(maxCount,end-start+1)
        return maxCount
arr="abcabcbb"
print(Solution().lengthOfLongestSubstring(arr)) 