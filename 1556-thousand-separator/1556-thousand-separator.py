class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0: return "0"
        n_string = ""
        i = 0
        while n > 0:
            if i % 3 == 0:
                n_string = '.' + n_string
            i += 1
            next_digit = str(n % 10)
            n_string = next_digit + n_string
            n //= 10
        return n_string[:-1]
         