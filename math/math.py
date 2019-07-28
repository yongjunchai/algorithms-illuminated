
class Permu:
    def __init__(self):
        self.cnt = 0
        self.pcCnt = 0

    def listFactorial(self, n):
        """
        list all possible permutiation of n numbers
        :param n:
        :return:
        """
        input = list()
        for i in range(1, n + 1):
            input.append(i)
        self.permu(input, list())
        print("permutations for [%i] items are [%i]" % (n, self.cnt))

    def permu(self, inputList, curList):
        if len(inputList) == 0:
            print(curList)
            self.cnt += 1
        for i in inputList:
            inputCopy = inputList.copy()
            curCopy = curList.copy()
            inputCopy.remove(i)
            curCopy.append(i)
            self.permu(inputCopy, curCopy)

    def listPc(self):
        parts = [["cpu1", "cpu2", "cpu3"], ["disk1", "disk2"], ["gpu1", "gpu2", "gpu3", "gpu4"], ["sound1", "sound2",
                                                                                                  "sound3"]]
        self.pcPermu(parts, 0,  list())
        print("permutations for PC are [%i]" % self.pcCnt)

    def pcPermu(self, parts, index,  pc):
        if len(parts) <= index:
            self.pcCnt += 1
            print("%3i : %s" % (self.pcCnt, pc))
            return
        part = parts[index]
        for i in part:
            pcCopy = pc.copy()
            pcCopy.append(i)
            self.pcPermu(parts, index + 1, pcCopy)





perm = Permu()
#perm.listFactorial(4)
perm.listPc()
