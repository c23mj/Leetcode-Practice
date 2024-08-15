from collections import defaultdict, Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        lastCompleted = defaultdict(lambda: float('-inf'))
        taskCounter = Counter(tasks)
        time = 0
        while taskCounter:
            time += 1
            canDo = [key for key in taskCounter.keys() if lastCompleted[key] < time - n]
            if not canDo:
                continue
            nextTask = max(canDo, key = lambda x: taskCounter[x])
            taskCounter[nextTask] -= 1
            if taskCounter[nextTask] == 0:
                del taskCounter[nextTask]
            lastCompleted[nextTask] = time
        return time
        