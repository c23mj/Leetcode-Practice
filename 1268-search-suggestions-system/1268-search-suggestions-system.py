class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        n = len(products)
        l, r = 0, n - 1 
        out = [[] for _ in range(len(searchWord))]
        for i in range(len(searchWord)):
            c = searchWord[i]
            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1
            validCount = r - l + 1
            out[i].extend(products[l:l + min(3, validCount)])
        return out
            
                

        