
class MergeSort:
    def __init__(self):
        pass

    def mergeSort(self, data: list, lessThan = lambda x, y: x < y):
        if data is None or len(data) < 2:
            return data
        mid = int(len(data) / 2)
        left = self.mergeSort_internal(data, 0, mid - 1, lessThan)
        right = self.mergeSort_internal(data, mid, len(data) - 1, lessThan)
        return self.merge(left, right, lessThan)

    def mergeSort_internal(self, data: list, l: int, r: int, lessThan = lambda x, y: x < y):
        if r - l + 1 <= 0:
            return []
        if r - l + 1 == 1:
            return data[l:l + 1]
        mid = l + int((r - l + 1) / 2)
        left = self.mergeSort_internal(data, l, mid - 1, lessThan)
        right = self.mergeSort_internal(data, mid, r, lessThan)
        return self.merge(left, right, lessThan)

    def merge(self, left: list, right: list, lessThan = lambda x, y: x < y):
        l = 0
        r = 0
        merged = []
        for k in range(len(left) + len(right)):
            if l == len(left):
                merged.extend(right[r:len(right)])
                break
            if r == len(right):
                merged.extend(left[l:len(left)])
                break
            if lessThan(left[l], right[r]):
                merged.append(left[l])
                l = l + 1
            else:
                merged.append(right[r])
                r = r + 1
        return merged


