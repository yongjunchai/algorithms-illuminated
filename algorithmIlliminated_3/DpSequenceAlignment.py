from algorithmIlliminated_3.utils import *

class Result:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.score = 0


class SequenceAlignment:
    def __init__(self):
        pass

    def getScore(self, char1, char2):
        assert(len(char1) == 1)
        assert (len(char2) == 1)
        if char1 == "-" or char2 == "-":
            return SequenceAlignment.getScoreGap()
        if char1 == char2:
            return 0
        return 2

    @staticmethod
    def getScoreGap():
        return 1

    def getMinNwScoreRecursive(self, str1, str2):
        result = Result(str1, str2)
        if len(str1) == 0 or len(str2) == 0:
            if len(str1) != 0:
                result.score = len(str1) * SequenceAlignment.getScoreGap()
                result.str2 = "-" * len(str1)
            if len(str2) != 0:
                result.score = len(str2) * SequenceAlignment.getScoreGap()
                result.str1 = "-" * len(str2)
            return result

        if len(str1) == len(str2) == 1:
            result.score = self.getScore(str1, str2)
            return result

        r1 = self.getMinNwScoreRecursive(str1[0:len(str1) - 1], str2[0:len(str2) - 1])
        r2 = self.getMinNwScoreRecursive(str1[0:len(str1) - 1], str2)
        r3 = self.getMinNwScoreRecursive(str1, str2[0:len(str2) - 1])
        r1Score = r1.score + self.getScore(str1[len(str1) - 1], str2[len(str2) - 1])
        r2Score = r2.score + SequenceAlignment.getScoreGap()
        r3Score = r3.score + SequenceAlignment.getScoreGap()
        if  r3Score <= r1Score and r3Score <= r2Score:
            result.str1 = r3.str1 + "-"
            result.str2 = r3.str2 + str2[len(str2) - 1]
            result.score = r3Score
            return result

        if r2Score <= r3Score and r2Score <= r1Score:
            result.str1 = r2.str1 + str1[len(str1) - 1]
            result.str2 = r2.str2 + "-"
            result.score = r2Score
            return result
        result.score = r1Score
        result.str1 = r1.str1 + str1[len(str1) - 1]
        result.str2 = r1.str2 + str2[len(str2) - 1]
        return result

    def getMinNwScoreDp(self, str1, str2):
        subProblemsSolution = Utils.createArray([len(str1) + 1, len(str2) + 1])
        for j in range(0, len(str2) + 1):
            subProblemsSolution[0][j] = j
        for i in range(0, len(str1) + 1):
            subProblemsSolution[i][0] = i
        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                score1 = subProblemsSolution[i - 1][j - 1] + self.getScore(str1[i - 1], str2[j - 1])
                score2 = subProblemsSolution[i - 1][j] + self.getScoreGap()
                score3 = subProblemsSolution[i][j - 1] + self.getScoreGap()
                if score1 <= score2 and score1 <= score3:
                    subProblemsSolution[i][j] = score1
                elif score2 <= score3 and score2 <= score1:
                    subProblemsSolution[i][j] = score2
                else:
                    subProblemsSolution[i][j] = score3
        return subProblemsSolution

    def constructMinNwSolution(self, str1, str2, subProblemsSolution):
        i = len(str1)
        j = len(str2)
        result = Result("", "")
        result.score = subProblemsSolution[i][j]
        while i > 0 or j > 0:
            if i == 0:
                result.str1 = "-" * j + result.str1
                result.str2 = str2[0:j] + result.str2
                break
            if j == 0:
                result.str2 = "-" * i + result.str2
                result.str1 = str1[0:i] + result.str1
                break
            score1 = subProblemsSolution[i - 1][j - 1] + self.getScore(str1[i - 1], str2[j - 1])
            score2 = subProblemsSolution[i - 1][j] + self.getScoreGap()
            score3 = subProblemsSolution[i][j - 1] + self.getScoreGap()
            if score1 <= subProblemsSolution[i][j]:
                result.str1 = str1[i - 1] + result.str1
                result.str2 = str2[j - 1] + result.str2
                i = i - 1
                j = j - 1
            elif score2 <= subProblemsSolution[i][j]:
                result.str1 = str1[i - 1] + result.str1
                result.str2 = "-" + result.str2
                i = i - 1
            elif score3 <= subProblemsSolution[i][j]:
                result.str1 = "-" + result.str1
                result.str2 = str2[j - 1] + result.str2
                j = j - 1
            else:
                assert(False)

        return result


