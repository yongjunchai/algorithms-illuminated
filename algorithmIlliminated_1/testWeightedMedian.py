from algorithmIlliminated_1.weightedMedian import *
import unittest


class MyTestCase(unittest.TestCase):
    def test_rndData_equal_weight(self):
        dataLen = 1025
        arr = []
        for i in range(dataLen):
            arr.append((i, 1))
        random.shuffle(arr)
        weightedMedian = WeightedMedian()
        getValueFun = lambda x: x[0]
        getWeightFun = lambda x: x[1]
        median, index = weightedMedian.getWeightedMedian(arr, getValueFun, getWeightFun)
        self.assertTrue(getValueFun(median) == 512)

    def test_preparedData_varied_weight(self):
        data1 = [[(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1),
            (13, 1), (14, 1), (15, 1)], (8, 1)]
        data2 = [[(1, 1), (2, 1), (3, 1), (4, 100), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1),
            (13, 1), (14, 1), (15, 1)], (4, 100)]
        data3 = [[(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1),
            (13, 5), (14, 6), (15, 1)], (12, 1)]
        dataSet = [data1, data2, data3]
        for data in dataSet:
            random.shuffle(data[0])
            weightedMedian = WeightedMedian()
            getValueFun = lambda x: x[0]
            getWeightFun = lambda x: x[1]
            median, index = weightedMedian.getWeightedMedian(data[0], getValueFun, getWeightFun)
            self.assertTrue(getValueFun(median) == getValueFun(data[1]))

    def test_complete_rnd_weight(self):
        for dataLen in range(1, 256):
            arr = []
            for i in range(dataLen):
                arr.append((i, random.randint(1, 100)))
            random.shuffle(arr)
            weightedMedian = WeightedMedian()
            getValueFun = lambda x: x[0]
            getWeightFun = lambda x: x[1]
            median, index = weightedMedian.getWeightedMedian(arr, getValueFun, getWeightFun)
            self.assertTrue(getValueFun(median) == getValueFun(arr[index]))
            self.assertTrue(getWeightFun(median) == getWeightFun(arr[index]))
            leftSubArrayMedianSum = 0
            rightSubArrayMedianSum = 0
            totalMedianSum = 0
            for i in range(0, index):
                leftSubArrayMedianSum += getWeightFun(arr[i])
            for i in range(index + 1, len(arr)):
                rightSubArrayMedianSum += getWeightFun(arr[i])
            totalMedianSum = leftSubArrayMedianSum + rightSubArrayMedianSum + getWeightFun(arr[index])
            self.assertTrue(leftSubArrayMedianSum / totalMedianSum <= 0.5)
            self.assertTrue(rightSubArrayMedianSum / totalMedianSum <= 0.5)

if __name__ == '__main__':
    unittest.main()
