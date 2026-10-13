class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        left=0
        s1map={}
        s2map={}
        for char in s1:
            s1map[char]=s1map.get(char,0)+1
        for right in range(len(s2)):
            s2map[s2[right]] = s2map.get(s2[right], 0) + 1
            if right-left+1==len(s1):
                if s1map==s2map:
                    return True
                s2map[s2[left]]-=1
                if s2map[s2[left]]==0:
                    del s2map[s2[left]]
                left+=1
        return False
arr1="ab"
arr2="eidbaooo" 
print(Solution().checkInclusion(arr1,arr2))