import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return stripped == stripped[::-1]