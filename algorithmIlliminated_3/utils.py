
class Utils:
    @staticmethod
    def createArray_internal(dimensions: list, index: int, root):
        if index >= len(dimensions):
            return
        if root is None:
            assert(False)
        items = dimensions[index]
        isLastDimension = (len(dimensions) - 1) == index
        for i in range(items):
            value = None
            if not isLastDimension:
                value = []
            root.append(value)
            Utils.createArray_internal(dimensions, index + 1, value)
        return root

    @staticmethod
    def  createArray(dimensions: list):
        return Utils.createArray_internal(dimensions, 0, [])

    @staticmethod
    def getValue(arr: list, indices: list):
        cur = arr
        for i in indices:
            cur = cur[i]
        return cur

    @staticmethod
    def updateValue(arr: list, indices: list, value):
        cur = arr
        i = len(indices) - 1
        for j in range(indices):
            if j == i:
                cur[indices[j]] = value
                break
            cur = cur[indices[j]]

    @staticmethod
    def updateValue(slot: list, value):
        for i in range(len(slot)):
           if type(slot(i)) is list:
               Utils.updateValue(slot(i), value)
           else:
               slot[i] = value

    @staticmethod
    def updateArr(arr: list, indices: list, value):
        """
        apply the value to all the remaining dimensions
        for example indices = [3, 2]
        if arr[3][2] is a not list, then set value as it values
        if arr[3][2] is list, and have more remaining dimensions, set value as the values of all the remaining dimensions
        :param arr:
        :param indices:
        :param value:
        :return:
        """
        slot = Utils.getValue(arr, indices)
        if type(slot) is list:
            Utils.updateValue(slot, value)
        else:
            Utils.updateValue(arr, indices,  value)