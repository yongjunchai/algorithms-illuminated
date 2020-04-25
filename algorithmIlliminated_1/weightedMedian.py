from algorithmIlliminated_1.dSelect import *


class WeightedMedian:
    """
    Problem 6.3 of Algorithm Illuminated
    """
    def __init__(self):
        self.dSelect = DSelect()

    def getWeightedMedian(self, arr: list, getVal=lambda x: x.val, getWeight=lambda x: x.weight):
        self.getWeightedMedian_internal(arr, 0, len(arr - 1), 0.5, 0.5, getVal, getWeight)

    def getWeightedMedian_internal(self, arr: list, left: int, right: int,
                                   leftArrayMedianSumMaxPercent: float, rightArrayMedianSumMaxPercent: float,
                                   getVal=lambda x: x.val, getWeight=lambda x: x.weight):
        assert(1 == (leftArrayMedianSumMaxPercent + rightArrayMedianSumMaxPercent))
        # selct median of array, return the index of the median element
        item, index = self.dSelect.select(arr, left, right, left + int((right - left) / 2), getVal)

        # calculate the sum of the median of the left and right sum array
        leftSubArrayWeightSum = 0
        rightSubArrayWeightSum = 0
        totalWeightSum = 0
        for i in range(left, index):
            leftSubArrayWeightSum += getWeight(arr[i])
        for i in range(index + 1, right):
            rightSubArrayWeightSum += getWeight(arr[i])
        totalWeightSum = leftSubArrayWeightSum + rightSubArrayWeightSum + getWeight(arr[index])

        #case 1, weighted median found, done
        if leftSubArrayWeightSum / totalWeightSum <= leftArrayMedianSumMaxPercent and rightSubArrayWeightSum / totalWeightSum <= rightArrayMedianSumMaxPercent:
            return arr[index]

        #case 2, weighted median is in the left sub array


        #case 3, weighted median is in the right sub array