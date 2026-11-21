class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        left=0
        smap={}
        pmap={}
        result=[]
        for char in p:
            pmap[char]=pmap.get(char,0)+1 #creating a map of the characters in p and their count
        for right in range(len(s)):
            smap[s[right]]=smap.get(s[right],0)+1 #incrementing the count of the character in the smap
            if right-left+1==len(p): #if the lenght of the window is equzl to the lengh of the p then we check whether the smap and pmap is equal or not
                if smap==pmap:
                    result+=[left] #adding the left index to the result list
                smap[s[left]]-=1 #decrementing the count of the character at the left index in the smap
                if smap[s[left]]==0: 
                    del smap[s[left]]
                left+=1
        return result
array="cbaebabacd"
p="abc"
print(Solution().findAnagrams(array,p))