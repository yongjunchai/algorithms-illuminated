
class Heap:
    def __init__(self):
        self.keys = []
        self.values = []
        self.valKeyIndex = dict()

    def size(self):
        return len(self.keys)

    def getKey(self, value):
        index = self.valKeyIndex.get(value)
        if index is None:
            return None
        assert(self.values[index][0] == value)
        return self.keys[index]

    def getValue(self, value):
        index = self.valKeyIndex.get(value)
        if index is None:
            return None
        assert(self.values[index][0] == value)
        return self.values[index]

    def insert(self, key, value):
        """
        :param key:
        :param value: value should be a tuple, the value[0] will be used to uniquely identify each value
        :return:
        """
        self.keys.append(key)
        self.values.append(value)
        self.valKeyIndex[value[0]] = len(self.keys) - 1
        self.bubbleUp(len(self.keys) - 1)

    def extractMin(self):
        key = self.keys[0]
        value = self.values[0]
        self.swap(0, len(self.keys) - 1)
        self.keys.pop()
        self.values.pop()
        self.valKeyIndex.pop(value[0])
        self.bubbleDown(0)
        return key, value

    def swap(self, i, j):
        self.valKeyIndex[self.values[i][0]], self.valKeyIndex[self.values[j][0]] =  \
            self.valKeyIndex[self.values[j][0]], self.valKeyIndex[self.values[i][0]]
        self.keys[i], self.keys[j] = self.keys[j], self.keys[i]
        self.values[i], self.values[j] = self.values[j], self.values[i]

    def update(self, value, newKey):
        index = self.valKeyIndex.get(value[0])
        if index is None:
            return
        oldKey = self.keys[index]
        if oldKey == newKey:
            return
        self.keys[index] = newKey
        if newKey < oldKey:
            self.bubbleUp(index)
        else:
            self.bubbleDown(index)

    def bubbleUp(self, index):
        while index > 0:
            parentIndex = int((index - 1) / 2)
            if parentIndex < 0:
                break
            if self.keys[parentIndex] <= self.keys[index]:
                break
            self.swap(index, parentIndex)
            index = parentIndex

    def bubbleDown(self, index):
        lastParent = len(self.keys) / 2 - 1
        while index <= lastParent:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index
            if left < len(self.keys) and self.keys[left] < self.keys[smallest]:
                smallest = left
            if right < len(self.keys) and self.keys[right] < self.keys[smallest]:
                smallest = right
            if smallest == index:
                break
            self.swap(index, smallest)
            index = smallest


