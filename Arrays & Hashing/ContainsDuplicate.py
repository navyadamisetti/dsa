class Solution:

    def hasDuplicate_(self, nums: List[int]) -> bool:
        for i_index, i in enumerate(nums): 
            for j_index, j in enumerate(nums):      #O(n^2)
                if(i==j) & (i_index != j_index):
                    return True
        return False
        
    #brute force solution
    #comparing each element with rest of the array

    def hasDuplicate(self, nums: List[int]) -> bool:

        hashset = set()
        for num in nums:         #O(n)
            if num in hashset:   #O(1)
                return True
            hashset.add(num)     #O(1)
        return False

    #above solution has Time complexity of O(n)

        