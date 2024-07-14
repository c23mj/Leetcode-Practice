class Solution:
    def addToDict(self, base, addend):
        for key in addend:
            base[key] += addend[key]
    def multDict(self, d, count):
        for key in d:
            d[key] *= count     

    def getCount(self, formula, i, n):
        if i == n or not formula[i].isdigit():
            count = 1
        else:
            count = [formula[i]]
            i += 1
            while i < n and formula[i].isdigit():
                count.append(formula[i])
                i += 1
            count = int(''.join(count))
        return count, i

    def countOfAtomsRec(self, formula, matches, startAt):
        # print(f"running countofAtomsRec at {formula}")
        full_dict = defaultdict(int)
        n = len(formula)
        i = startAt
        while i < n:
            if formula[i].isupper():
                # print(f"i: {i}")
                word = [formula[i]]
                i += 1
                while i < n and formula[i].islower():
                    word.append(formula[i])
                    i += 1
                word = ''.join(word)
                count, i = self.getCount(formula, i, n)
                full_dict[word] += count
            else:
                tmp = i
                i = matches[i]
                to_add = self.countOfAtomsRec(formula[tmp+1:i].zfill(i), matches, tmp+1)
                i += 1
                count, i = self.getCount(formula, i, n)
                self.multDict(to_add, count)
                self.addToDict(full_dict, to_add)

        return full_dict
                
                    

    def countOfAtoms(self, formula: str) -> str:
        if not formula:
            return dict()
        matches = dict()
        # print(f"string: {formula}")
        stack = []
        for i in range(len(formula)):
            if formula[i] == '(':
                stack.append(i)
                # print(f"append at {i}")
            elif formula[i] == ')':
                matches[stack.pop()] = i
                # print(f'pop at {i}')
        # print(f"matches: {matches}")
        countDict = self.countOfAtomsRec(formula, matches, 0)
        # print(f"countDict: {countDict}")
        out = []
        for key in sorted(countDict.keys()):
            if countDict[key] > 1:
                out.append(f'{key}{countDict[key]}')
            else:
                out.append(key)
    
        return ''.join(out)
      
                
                