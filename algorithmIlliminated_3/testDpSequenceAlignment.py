from algorithmIlliminated_3.dpSequenceAlignment import *

import unittest


class SequenceAlignmentTestCase(unittest.TestCase):
    def test_getMinNwScoreRecursive(self):
        dataSet = [(("abc", "defabcd"), (4, "---abc-", "defabcd"))]

        for data in dataSet:
            inputData = data[0]
            expectdResult = data[1]
            sequenceAlignment = SequenceAlignment()
            result = sequenceAlignment.getMinNwScoreRecursive(inputData[0], inputData[1])
            print("input strings -----------------------")
            print(inputData[0])
            print(inputData[1])
            print("result strings -----------------------")
            print(result.score)
            print(result.str1)
            print(result.str2)
            self.assertTrue(result.score == expectdResult[0])
            self.assertTrue(result.str1 == expectdResult[1])
            self.assertTrue(result.str2 == expectdResult[2])

    def test_getMinNwScoreDp(self):
        dataSet = [(("abc", "defabcd"), (4, "---abc-", "defabcd")),
                   (("abc", "abcdefghijkllmml"), (13, "abc-------------", "abcdefghijkllmml")),
                   (("kdewfwlfsljdfsjdfabcdef", "sfsfdsfsdfsdfsdfsdfabcdefghijkllmmhjgjhghl"), (35, "---kdewfwlfsljdfs--jdfabcdef-----------------", "sfsfd-sfsdfs--dfsdfsdfabcdefghijkllmmhjgjhghl")),
                   ]

        for data in dataSet:
            inputData = data[0]
            expectdResult = data[1]
            sequenceAlignment = SequenceAlignment()
            subProblemsSolution = sequenceAlignment.getMinNwScoreDp(inputData[0], inputData[1])
            result = sequenceAlignment.constructMinNwSolution(inputData[0], inputData[1], subProblemsSolution)
            print("input strings -----------------------")
            print(inputData[0])
            print(inputData[1])
            print("result strings -----------------------")
            print(result.score)
            print(result.str1)
            print(result.str2)
            self.assertTrue(result.score == expectdResult[0])
            self.assertTrue(result.str1 == expectdResult[1])
            self.assertTrue(result.str2 == expectdResult[2])

    def test_getMinNwScoreDp_play(self):
        inputData = ("aadflkja;slkfj;asaljf;asskjf;lkdjkdewf", "asdjjf;alsjf;laskjf;lasjf;laskjf;alssj;lskjj;;slkj;lkjkkdewf")
        sequenceAlignment = SequenceAlignment()
        subProblemsSolution = sequenceAlignment.getMinNwScoreDp(inputData[0], inputData[1])
        result = sequenceAlignment.constructMinNwSolution(inputData[0], inputData[1], subProblemsSolution)
        print("input strings -----------------------")
        print(inputData[0])
        print(inputData[1])
        print("result strings -----------------------")
        print(result.score)
        print(result.str1)
        print(result.str2)


if __name__ == '__main__':
    unittest.main()
