# problem 3.2
class UnimodalMax:
    def __init__(self):
        pass

    def findMax(self, nums: list):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        return self.findMax_internal(nums, left, right)

    def findMax_internal(self, nums: list, left: int, right: int):
        if left == right:
            return nums[left]
        assert(left < right)
        mid = left + int((right - left) / 2)
        if nums[mid] < nums[mid + 1]:
            return self.findMax_internal(nums, mid + 1, right)
        else:
            if mid == left:
                return nums[mid]
            if nums[mid - 1] < nums[mid]:
                return nums[mid]
            return self.findMax_internal(nums, left, mid - 1)


