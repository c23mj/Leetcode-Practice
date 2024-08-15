from collections import defaultdict
class DetectSquares:
    def __init__(self):
        self.x_coords = defaultdict(set) # k: y-axes, v: y-values
        self.pt_counts = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.x_coords[x].add(y)
        self.pt_counts[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        count = 0
        x, y = point
        for y2 in self.x_coords[x]:
            if y2 == y: continue
            dy = y2 - y
            count += self.pt_counts[(x, y2)] * self.pt_counts[(x + dy, y)] * self.pt_counts[(x + dy, y2)]
            count += self.pt_counts[(x, y2)] * self.pt_counts[(x - dy, y)] * self.pt_counts[(x - dy, y2)]
        return count
            


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)