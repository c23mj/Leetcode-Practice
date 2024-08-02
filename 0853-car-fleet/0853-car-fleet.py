class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:    
        paired = [(p, s) for p, s in zip(position, speed)]
        paired.sort(reverse = True) 
        # merge when you're dealing with a car that starts at an earlier position AND earlier arrival time
        fleets = []
        times = [float(target - p)/s for p, s in paired]
        for time in times:
            if not fleets or time > fleets[-1]:
                fleets.append(time)
        
        return len(fleets)