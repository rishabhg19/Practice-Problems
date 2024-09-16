class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1]
        prod = 1
        for i in range(1, len(nums)):
            prod = prod*nums[i-1]
            prefixes.append(prod)
        postfixes = [1] * len(nums)
        prod = 1
        for i in reversed(range(len(nums)-1)):
            prod = prod*nums[i+1]
            postfixes[i] = prod 
        return [prefix * postfix for prefix, postfix in zip(prefixes, postfixes)]
