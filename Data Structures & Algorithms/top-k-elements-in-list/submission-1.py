from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []

        counted = Counter(nums).most_common(k)

        for i in range(k):
            ans.append(counted[i][0])
        
        return ans