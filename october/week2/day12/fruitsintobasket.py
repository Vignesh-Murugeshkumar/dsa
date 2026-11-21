class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left=0
        maxx=0
        map={} #declaring map to store the fruits and their count
        for right in range (len(fruits)):
            map[fruits[right]]=map.get(fruits[right],0)+1 #used to increment the count of the fruit in the map
            while len(map)>2:
                map[fruits[left]]-=1 
                if map[fruits[left]]==0:
                    del map[fruits[left]] #used to delete if the count of the fruit becomes zero
                left+=1
            maxx=max(maxx,right-left+1) #used to update the maxx value with the maximum length 
        return maxx


arr = [1, 2, 2]
print(Solution().totalFruit(arr))