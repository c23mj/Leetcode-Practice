from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Brute Force Simulation
        # lastCompleted = defaultdict(lambda: float('-inf'))
        # taskCounter = Counter(tasks)
        # time = 0
        # while taskCounter:
        #     time += 1
        #     canDo = [key for key in taskCounter.keys() if lastCompleted[key] < time - n]
        #     if not canDo:
        #         continue
        #     nextTask = max(canDo, key = lambda x: taskCounter[x])
        #     taskCounter[nextTask] -= 1
        #     if taskCounter[nextTask] == 0:
        #         del taskCounter[nextTask]
        #     lastCompleted[nextTask] = time
        # return time
        
        # With a heap and a queue 
        counts = [-val for val in Counter(tasks).values()]
        heapq.heapify(counts) # max heap of cooldowns
        cooldownQueue = deque()
        time = 0
        while counts or cooldownQueue:
            if counts:
                nextCount = heapq.heappop(counts)
                if nextCount < -1:
                    cooldownQueue.append((nextCount + 1, time + n + 1)) 
            time += 1
            while cooldownQueue and cooldownQueue[0][1] <= time:
                heapq.heappush(counts, cooldownQueue.popleft()[0])
        return time
            
            
            
        
        
        
        
        
        
        