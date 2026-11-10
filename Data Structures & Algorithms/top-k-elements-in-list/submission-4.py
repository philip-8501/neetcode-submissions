class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counted = defaultdict(int)

        for num in nums:
            counted[num] += 1

        freq = [[] for i in range(len(nums) + 1)]
        for num, cnt in counted.items():
            freq[cnt].append(num)

        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans