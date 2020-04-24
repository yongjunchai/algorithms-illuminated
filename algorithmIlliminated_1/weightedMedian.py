from algorithmIlliminated_1.dSelect import *


class WeightedMedian:
    """
    Problem 6.3 of Algorithm Illuminated
    """
    def __init__(self):
        pass

    def getWeightedMedian(self, arr: list, getVal=lambda x: x.val, getWeight=lambda x: x.weight):
        self.getWeightedMedian_internal(arr, 0, len(arr - 1), 50, 50, getVal, getWeight)

    def getWeightedMedian_internal(self, arr: list, left: int, right: int,
                                   leftArrayMedianSumMaxPercent: int, rightArrayMedianSumMaxPercent: int,
                                   getVal=lambda x: x.val, getWeight=lambda x: x.weight):
        assert(1 == (leftArrayMedianSumMaxPercent + rightArrayMedianSumMaxPercent))
        # selct median of array, return the index of the median element

        # calculate the sum of the median of the left and right sum array

        #case 1, weighted median found, done

        #case 2, weighted median is in the left sub array

        #case 3, weighted median is in the right sub array