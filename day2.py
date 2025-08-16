class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums) + 1
        new_list = [i for i in range(length)]
        element = [i for i in new_list if i not in nums]
        return (element[0])
