import math
"""
quiz 12.3
"""


class BirthdayProblem:
    def __init__(self):
        pass

    def calPossibility(self, n: int):
        """
        assume each year has 366 days
        :param n: number of people
        :return: possibility of at least two people have the same birthday
        """
        p = 1
        for i in range(1, n):
            p = p * (366.0 - i) / 366.0
        return 1 - p

    def run(self):
        for i in range(1, 50):
            p = self.calPossibility(i)
            print("%-5d people, the possibility of at least two people have the same birthday: %f" % (i, p))


birthdayProblem = BirthdayProblem()
birthdayProblem.run()


"""
problem 12.3
"""


def calculateBloomFilterFalsePositiveRate(bits: int):
    return math.pow(0.5, math.log(2) * bits)


bits = 16
print("bloom filter: false positive rate of  %d bits: %f" % (bits, calculateBloomFilterFalsePositiveRate(bits)))

