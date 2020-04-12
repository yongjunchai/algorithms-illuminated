import random


class RSelect:
    def __init__(self):
        pass

    def partition(self, arr: list, left: int, right: int):
        pivot = random.randint(left, right)
        arr[left], arr[pivot] = arr[pivot], arr[left]
        valPivot = arr[left]
        i = left + 1
        for j in range(left + 1, right + 1):
            if arr[j] < valPivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[left], arr[i - 1] = arr[i - 1], arr[left]
        return i - 1

    def select(self, arr: list, left: int, right: int, i: int):
        """
        select ith order statistic of arr
        :param arr:
        :param i:
        :return:
        """
        if i > right - left + 1:
            return None
        if right - left + 1 == 1:
            return arr[left]
        pivot: int = self.partition(arr, left, right)
        j = pivot - left + 1
        if j == i:
            return arr[pivot]
        elif j < i:
            return self.select(arr, pivot + 1, right, i - j)
        else:
            return self.select(arr, left, pivot - 1, i)
