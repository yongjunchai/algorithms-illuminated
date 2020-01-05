
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

