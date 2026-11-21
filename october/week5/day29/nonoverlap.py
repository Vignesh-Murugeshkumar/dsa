class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        intervals = self.merge_sort(intervals)

        removals = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if start < prev_end:
                removals += 1
            else:
                prev_end = end

        return removals

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i][1] <= right[j][1]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result
arr = [[1,2],[2,3],[3,4],[1,3]]
print(Solution().eraseOverlapIntervals(arr))