
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
                result.str1 = "-" * len(str1)
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
        if  r1Score <= r2Score <= r3Score:
            result.str1 = result.str1 + "-"
            result.score = r3Score
            return result

        if r1Score <= r3Score <= r2Score:
            result.str2 = result.str2 + "-"
            result.score = r2Score
            return result
        result.score = r1Score
        return result



