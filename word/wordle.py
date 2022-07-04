

class Wordle:
    def __init__(self):
        self.wordFIle = "./data/words_alpha.txt"

    def hasLetters(self, word: str, letters):
        for letter in letters:
            index = word.find(letter)
            if index == -1:
                return False
        return True

    def hasMultipleLetters(self, word: str, letter: str):
        cnt = 0
        for i in range(0, 5):
            l = word[i:i+1]
            if l == letter:
                cnt += 1
        return cnt > 1

    def hasMultiple(self, word: str, letters):
        for letter in letters:
            if self.hasMultipleLetters(word, letter):
                return True
        return False

    def findWords(self):
        f = open(self.wordFIle, "r")
        lines = f.readlines()
        overallGrayedLetters = {}
        firstGrayedLetters = {}
        sndGrayedLetters = {}
        thirdGrayedLetters = {}
        fourthGrayedLetters = {}
        fifthGrayedLetters = {}
        mustHaveLetters = {}
        firstLetter = None
        sndLetter = None
        thirdLetter = None
        fourthLetter = None
        fifthLetter = None
        noMultiplLetters = {}
        hits = []
        for line in lines:
            if len(line) != 6:
                continue
            hit = True
            for i in range(0, 5):
                letter = line[i: i+1]
                if letter in overallGrayedLetters:
                    hit = False
                    break
                if i == 0:
                    if letter in firstGrayedLetters:
                        hit = False
                        break
                    if firstLetter is not None and letter != firstLetter:
                        hit = False
                        break
                elif i == 1:
                    if letter in sndGrayedLetters:
                        hit = False
                        break
                    if sndLetter is not None and letter != sndLetter:
                        hit = False
                        break
                elif i == 2:
                    if letter in thirdGrayedLetters:
                        hit = False
                        break
                    if thirdLetter is not None and letter != thirdLetter:
                        hit = False
                        break
                elif i == 3:
                    if letter in fourthGrayedLetters:
                        hit = False
                        break
                    if fourthLetter is not None and letter != fourthLetter:
                        hit = False
                        break
                elif i == 4:
                    if letter in fifthGrayedLetters:
                        hit = False
                        break
                    if fifthLetter is not None and letter != fifthLetter:
                        hit = False
                        break
            if not self.hasLetters(line, mustHaveLetters):
                hit = False
            if self.hasMultiple(line, noMultiplLetters):
                hit = False
            if hit:
                line = line[0:5]
                hits.append(line)
        print(hits)


wordle = Wordle()
wordle.findWords()