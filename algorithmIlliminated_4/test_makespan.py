import unittest
from makespan import *


class MyTestCase(unittest.TestCase):
    def findMakespan(self, schedule):
        makeSpan = -1
        for i in range(0, len(schedule)):
            if schedule[i][0] > makeSpan:
                makeSpan = schedule[i][0]
        return makeSpan

    def test_graham(self):
        makeSpan = Makespan()
        machineCount = 5
        jobs = [1, 1, 1, 1, 1, 2, 2, 5, 2, 3, 7, 3, 4, 3, 2, 1, 12, 5, 1, 6, 7, 4, 20]
        schedule = makeSpan.graham(machineCount, jobs)
        print(schedule)
        print("graham: {}".format(self.findMakespan(schedule)))
        schedule = makeSpan.ltp(machineCount, jobs)
        print(schedule)
        print("LTP: {}".format(self.findMakespan(schedule)))


if __name__ == '__main__':
    unittest.main()
