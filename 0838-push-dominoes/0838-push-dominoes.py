class Solution(object):
    def pushDominoes(self, dominoes):
        dom = [dominoes[i] for i in range(len(dominoes))]
        while True:
            changed = False
            next_dom = [dom[i] for i in range(len(dom))]
            for i in range(len(dom)):
                if dom[i] != ".":
                    continue
                if i > 0 and dom[i-1] == "R":
                    if i == len(dom) - 1 or dom[i+1] != "L":
                        changed = True
                        next_dom[i] = "R"
                if i < len(dom) - 1 and dom[i + 1] == "L" :
                    if i == 0 or dom[i-1] != "R":
                        changed = True
                        next_dom[i] = "L"
            if not changed:
                break
            dom = next_dom
 
        return ''.join(dom)

        