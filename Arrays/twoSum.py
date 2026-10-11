def solution(nums,target):
    map = {}
    for i in range(len(nums)):
        complement=target-nums[i]
        if(complement in map):
            return[map[complement],i]
        map[nums[i]]=i
    return[]  
array=[2,7,11,15]
target=9
print(solution(array,target))  