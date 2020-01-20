

class CountInv:
    def __init__(self):
        pass

    def countInv(self, data: list):
        if data is None or len(data) < 2:
            return data
        mid = int(len(data) / 2)
        left, leftInv = self.countInv_internal(data, 0, mid - 1)
        right, rightInv = self.countInv_internal(data, mid, len(data) - 1)
        combined, splitInv = self.merge_count_split_inv(left, right)
        return leftInv + rightInv + splitInv

    def countInv_internal(self, data: list, l: int, r: int):
        if r - l + 1 <= 0:
            return [], 0
        if r - l + 1 == 1:
            return data[l:l + 1], 0
        mid = l + int((r - l + 1) / 2)
        left, leftInv = self.countInv_internal(data, l, mid - 1)
        right, rightInv = self.countInv_internal(data, mid, r)
        combined, splitInv = self.merge_count_split_inv(left, right)
        return combined, (leftInv + rightInv + splitInv)

    def merge_count_split_inv(self, left: list, right: list):
        l = 0
        r = 0
        merged = []
        leftLen = len(left)
        splitInv = 0
        for k in range(len(left) + len(right)):
            if l == len(left):
                merged.extend(right[r:len(right)])
                break
            if r == len(right):
                merged.extend(left[l:len(left)])
                break
            if left[l] < right[r]:
                merged.append(left[l])
                l = l + 1
            else:
                merged.append(right[r])
                r = r + 1
                splitInv = splitInv + (leftLen - l)
        return merged, splitInv


