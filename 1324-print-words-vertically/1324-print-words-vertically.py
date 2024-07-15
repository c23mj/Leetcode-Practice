class Solution:
    def printVertically(self, s: str) -> List[str]:
        s_arr = s.split(" ")
        maxLen = len(max(s_arr, key=len))
        out_arr = []
        for i in range(maxLen):
            out_arr.append('')
        for i in range(maxLen):
            for j in range(len(s_arr)):
                if len(s_arr[j]) > i:
                    out_arr[i] += s_arr[j][i]
                else:
                    out_arr[i] += ' '
        

        
        return [s.rstrip() for s in out_arr]
        