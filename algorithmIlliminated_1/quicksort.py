import random


class Quicksort:
    def __init__(self):
        pass

    def choosePivot(self, left: int, right: int):
        return random.randint(left, right)

    def partition(self, arr: list, left: int, right: int):
        pivot = self.choosePivot(left, right)
        arr[left], arr[pivot] = arr[pivot], arr[left]
        valPivot = arr[left]
        i = left + 1
        for j in range(left + 1, right + 1):
            if arr[j] < valPivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[left], arr[i - 1] = arr[i - 1], arr[left]
        return i - 1

    def sort(self, arr: list, left: int, right: int):
        if right <= left:
            return
        pivot = self.partition(arr, left, right)
        self.sort(arr, left, pivot - 1)
        self.sort(arr, pivot + 1, right)



