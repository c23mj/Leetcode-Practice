class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglies = [1]
        indices = [0] * len(primes)
        for i in range(n-1):
            t = [primes[i] * uglies[indices[i]] for i in range(len(primes))]
            m = min(t)
            for j in range(len(t)):
                if t[j] == m:
                    indices[j]+=1
            
            uglies.append(m)

        return uglies[-1]