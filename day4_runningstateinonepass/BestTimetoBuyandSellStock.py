class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice=prices[0]
        max_profit=0
        for i in range(1,len(prices)):
            if prices[i]<minprice:
                minprice=prices[i]
            else:
                current_profit=prices[i]-minprice
                max_profit=max(max_profit,current_profit)
        return max_profit

arr=[7,1,5,3,6,4]
print(Solution().maxProfit(arr))