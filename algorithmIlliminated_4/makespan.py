import heapq


class Makespan:
    def __init__(self):
        pass

    def graham(self, machineCount: int, jobs: list):
        """
        problem 20.6
        :param machines:
        :param jobs:
        :return:
        """
        # [load, machine id, job list]
        machines = [[0, x, list()] for x in range(0, machineCount)]
        for i in range(0, len(jobs)):
            machine = heapq.heappop(machines)
            machine[0] = machine[0] + jobs[i]
            machine[2].append(jobs[i])
            heapq.heappush(machines, machine)
        return machines

    def ltp(self, machineCount: int, jobs: list):
        sortedJobs = sorted(jobs, reverse=True)
        return self.graham(machineCount, sortedJobs)