
class RodCutting:
    def __init__(self):
        self.prices = [0, 1, 5, 8, 9, 15, 17, 17, 20, 24, 25]
        self.pricesShortBig = [0, 3, 7, 10, 15, 18, 25, 30]

    def bottomUp_cutCost(self, prices):
        costPerCut = 1
        subProblem = [-1] * (len(prices))
        solution = [-1] * (len(prices))
        subProblem[0] = 0
        solution[0] = 0
        for i in range(1, len(prices)):
            maxVal = -1
            for j in range(1, i + 1):
                value = prices[j] + subProblem[i - j]
                if i - j > 0:
                    value = value - costPerCut
                if maxVal < value:
                    maxVal = value
                    solution[i] = j
            subProblem[i] = maxVal
        return subProblem, solution

    def bottomUp(self):
        subProblem = [-1] * (len(self.prices))
        solution = [-1] * (len(self.prices))
        subProblem[0] = 0
        solution[0] = 0
        for i in range(1, len(self.prices)):
            maxVal = -1
            for j in range(1, i + 1):
                value = self.prices[j] + subProblem[i - j]
                if maxVal < value:
                    maxVal = value
                    solution[i] = j
            subProblem[i] = maxVal
        return subProblem, solution

    def findCut_cutCost(self):
        print("begin findCut_cutCost --------------")
        subProblem, solution = self.bottomUp_cutCost(self.prices)
        print("prices: ")
        print(self.prices)
        print("sub problems: ")
        print(subProblem)
        print("solution: ")
        print(solution)
        self.printSolution(solution, 9)

    def findCut(self):
        print("begin findCut --------------")
        subProblem, solution = self.bottomUp()
        print("prices: ")
        print(self.prices)
        print("sub problems: ")
        print(subProblem)
        print("solution: ")
        print(solution)
        self.printSolution(solution, 9)

    def printSolution(self, solution, n):
        print("rod cutting for rod of size: " + str(n))
        cuts = list()
        while n > 0:
            cuts.append(solution[n])
            n = n - solution[n]
        print(cuts)

    def printDensity(self, prices):
        print(prices)
        densities = list()
        for i in range(1, len(prices) + 1):
            densities.append(prices[i - 1] / (1.0 * i))
        print(densities)

rodCutting = RodCutting()


rodCutting.printDensity(rodCutting.prices)

rodCutting.findCut()
rodCutting.findCut_cutCost()
