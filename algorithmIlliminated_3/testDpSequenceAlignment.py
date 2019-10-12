from algorithmIlliminated_3.DpSequenceAlignment import *

import unittest


class SequenceAlignmentTestCase(unittest.TestCase):
        def test_getMinNwScoreRecursive(self):
        str1 = "adbc"
        str2 = "aebfc"
        sequenceAlignment = SequenceAlignment()
        result = sequenceAlignment.getMinNwScoreRecursive(str1, str2)
        print(result.score)
        print(result.str1)
        print(result.str2)


if __name__ == '__main__':
    unittest.main()
