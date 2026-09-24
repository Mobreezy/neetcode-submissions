class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(filter(str.isalnum, s))
        cleaned = cleaned.lower()

        for l in range(len(cleaned)):
            r = len(cleaned) - 1 - l
            if cleaned[l] != cleaned[r]:
                return False
        
        return True