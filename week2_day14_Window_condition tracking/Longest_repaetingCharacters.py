class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count={}
        maxfreq=0
        maxlenght=0
        start=0
        for end in range(len(s)):
            count[s[end]]=count.get(s[end],0)+1
            maxfreq=max(maxfreq,count.get(s[end]))
            while (end-start+1)-maxfreq>k:
                count[s[start]]-=1
                start+=1
            maxlenght=max(maxlenght,end-start+1)
        return maxlenght

arr="ABAB"
k=2
print(Solution().characterReplacement(arr,k))   
