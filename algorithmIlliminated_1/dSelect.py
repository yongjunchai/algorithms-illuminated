from algorithmIlliminated_1.quicksort import *


class DSelect:
    def __init__(self):
        pass

    def partition(self, arr: list, left: int, right: int, p: int):
        i = left
        pivot = left
        while i <= right:
            if arr[i] == p:
                pivot = i
                break
            i += 1
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
        """
        if i > right - left + 1:
            return None
        if right - left + 1 == 1:
            return arr[left]
        quickSort = Quicksort()
        if right - left + 1 < 10:
            quickSort.sort(arr, left, right)
            return arr[left + i - 1]
        medians = []
        for h in range(int((right - left) / 5)):
            quickSort.sort(arr, left + 5 * h, left + 5 * h + 4)
            medians.append(arr[left + 5 * h + 2])
        p = self.select(medians, 0, len(medians) - 1, int((right - left) / 10))
        pivot: int = self.partition(arr, left, right, p)
        j = pivot - left + 1
        if j == i:
            return arr[pivot]
        elif j < i:
            return self.select(arr, pivot + 1, right, i - j)
        else:
            return self.select(arr, left, pivot - 1, i)


