from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []

        for i in range(k):
            ans.append(Counter(nums).most_common(k)[i][0])
        
        return ans