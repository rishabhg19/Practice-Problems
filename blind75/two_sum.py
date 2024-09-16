class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        pair = []
        for i, num in enumerate(nums):
            difference = target - num
            if difference in dic:
                return [dic[difference], i]
            else:
                dic[num] = i