

# problem 3.3
class FindNum:
    def __init__(self):
        pass

    def findNum(self, nums: list):
        left = 0
        right = len(nums) - 1
        return self.findNum_internal(nums, left, right)

    def findNum_internal(self, nums: list, left: int, right: int):
        if right == left:
            return nums[right] == right
        assert(left < right)
        mid = left + int((right - left) / 2)
        if nums[mid] == mid:
            return True
        if nums[mid] > mid:
            return self.findNum_internal(nums, left, mid - 1)
        else:
            return self.findNum_internal(nums, mid + 1, right)
