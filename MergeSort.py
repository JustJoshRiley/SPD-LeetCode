class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = len(nums) - 1
        
        i = 0
        count = 0
        while count < len(nums):
            if nums[i] == 0:
                nums[i], nums[red] = nums[red], nums[i]
                red += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[white] = nums[white], nums[i]
                white -= 1
            count += 1
            