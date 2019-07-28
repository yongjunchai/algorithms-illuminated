
class Job:
    def __init__(self, length, weight):
        self.length = length
        self.weight = weight


class Greedy:
    def __init__(self):
        self.jobs = list()
        self.jobs.append(Job(5, 3))
        self.jobs.append(Job(2, 1))

    def greedyDiff(self):
        scores = list()
        for job in self.jobs:
            score = job.weight - job.length
            scores.append((score, job))
        scores.sort(key=lambda x: x[0], reverse=True)
        curLen = 0
        weightedCt = 0
        for score in scores:
            curLen += score[1].length
            weightedCt += curLen * score[1].weight
        print("greedyDiff, weighted completion time: %s" % weightedCt)

    def greedyRatio(self):
        scores = list()
        for job in self.jobs:
            score = job.weight * 1.0 / job.length
            scores.append((score, job))
        scores.sort(key=lambda x: x[0], reverse=True)
        curLen = 0
        weightedCt = 0
        for score in scores:
            curLen += score[1].length
            weightedCt += curLen * score[1].weight
        print("greedyRatio, weighted completion time: %s" % weightedCt)


greedy = Greedy()
greedy.greedyDiff()
greedy.greedyRatio()
