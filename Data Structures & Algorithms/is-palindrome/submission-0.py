class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(char for char in s if char.isalnum())
        cleaned = cleaned.lower()
        i = 0
        j = len(cleaned) - 1
        while i < j:
            if cleaned[i] == cleaned[j]:
                i = i + 1
                j = j - 1
            else: 
                return False
        return True
          
                
