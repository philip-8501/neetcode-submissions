class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # nums = [1,2,2,3,3,3], k = 2

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # count = {1: 1, 2: 2, 3: 3}

        freq = [[] for i in range(len(nums) + 1)]

        # freq = [[] [] [] [] [] [] []]

        for num, cnt in count.items():
            freq[cnt].append(num)

        # freq = [[] [1] [2] [3] [] [] []]

        ans = []

        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return ans