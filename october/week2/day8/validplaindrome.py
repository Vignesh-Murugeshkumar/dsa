class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)-1
        left=0
        right=n
        while left<right:
            while left < right and not s[left].isalnum():
                left += 1
            while  left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1
        return True
s="A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))