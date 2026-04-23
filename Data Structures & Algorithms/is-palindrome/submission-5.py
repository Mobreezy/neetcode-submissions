class Solution:
    def isPalindrome(self, s: str) -> bool:
        #call sanitzeInput
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        if len(cleaned) == 0:
            return True
        l, r = 0, len(cleaned) - 1
        while True:
            if cleaned[l] == cleaned[r] and l != r and r != l+1:
                print(cleaned[l], l, cleaned[r], r)
                l+= 1
                r-= 1
            elif cleaned[l] != cleaned[r]:
                return False
            else:
                return True
