from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        counted = defaultdict(int)
        for num in nums:
            counted[num] += 1

        arr = []
        for num, cnt in counted.items():
            arr.append([cnt, num])
        arr.sort()

        for i in range(k):
            ans.append(arr[len(arr)-i-1][1])
        
        return ans