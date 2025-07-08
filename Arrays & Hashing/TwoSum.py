class Solution:
    def twoSum_(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    #brute force solution
    # Time O(n^2), Space O(1)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                 return [prevMap[diff],i]
            prevMap[n] = i
        return
    
    # adding to hashmap while checking for index
    # Time O(n), Space O(n)
        