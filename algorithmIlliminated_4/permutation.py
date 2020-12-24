from collections import deque


class Entry:
    def __init__(self, value):
        self.value = value
        self.used = False


class Item:
    def __init__(self):
        self.index = None
        self.offset = None


class Permutation:
    def __init__(self):
        self.count = 0

    def getNextAvailableEntry(self, entries: list, ith: int):
        cnt = 0
        for i in range(len(entries)):
            entry: Entry = entries[i]
            if entry.used is False:
                cnt = cnt + 1
                if cnt == ith:
                    return entry
        return None

    def factorial_iterative(self, sources: list, index: int, output: list):
        size = len(sources)
        if index >= size:
            self.count = self.count + 1
            print("{}: {}".format(self.count, output))
            return
        if index == 0:
            for i in range(0, size):
                entry: Entry = sources[i]
                entry.used = True
                output[0] = entry.value
                self.factorial_iterative(sources, 1, output)
                entry.used = False
        else:
            for i in range(index, size):
                entry: Entry = self.getNextAvailableEntry(sources, (i - index + 1))
                entry.used = True
                output[index] = entry.value
                self.factorial_iterative(sources, index + 1, output)
                entry.used = False

    def factorial_stack(self, sources: list, output: list):
        stack = deque()
        item = Item()
        item.index = 0
        item.offset = 0
        size = len(sources)
        stack.append(item)
        while len(stack) > 0:
            item: Item = stack.pop()
            if item.index == 0:
                if item.offset > 0:
                    entry: Entry = sources[item.offset - 1]
                    entry.used = False
                entry: Entry = sources[item.offset]
                entry.used = True
                output[0] = entry.value
                item.offset = item.offset + 1
                if item.offset < size:
                    stack.append(item)
                nextItem: Item = Item()
                nextItem.index = 1
                nextItem.offset = 0
                stack.append(nextItem)
            else:
                if item.offset > 0:
                    # free the entry used by this index
                    sources[output[item.index] - 1].used = False
                if item.offset <= (size - item.index - 1):
                    entry: Entry = self.getNextAvailableEntry(sources, (item.offset + 1))
                    entry.used = True
                    output[item.index] = entry.value
                    nextItem = Item()
                    nextItem.index = item.index
                    nextItem.offset = item.offset + 1
                    stack.append(nextItem)
                    if item.index != size - 1:
                        nextItem = Item()
                        nextItem.index = item.index + 1
                        nextItem.offset = 0
                        stack.append(nextItem)
                if item.index == size - 1 and item.offset == 0:
                    self.count = self.count + 1
                    print("{}: {}".format(self.count, output))

    def factorial(self, n: int):
        nums = [Entry(x) for x in range(1, n + 1)]
        output = [None for x in range(0, n)]
        self.factorial_stack(nums, output)


if __name__ == "__main__":
    permutation = Permutation()
    permutation.factorial(5)


