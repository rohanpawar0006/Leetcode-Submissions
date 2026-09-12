class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = list(filter(lambda letter : letter.isalnum(), s.lower()))
        rev = cleaned[::-1]

        if cleaned == rev:
            return True
        else:
            return False