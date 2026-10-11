def solution(nums,target):
    map = {}
    for i in range(len(nums)):
        complement=target-nums[i] #finding the complement number to che ck if it exists in the map ex: (target=9, nums[i]=2, complement=7)
        if(complement in map): #if the complement number exists in the map, return the index of the complement and the current index
            return[map[complement],i]
        map[nums[i]]=i
    return[]  
array=[2,7,11,15]
target=9
print(solution(array,target))  