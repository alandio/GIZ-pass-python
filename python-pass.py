class Solution:
    @staticmethod
    def longest_palindromic(s: str) -> str:
        long_palindrome = ""
        for i in range(len(s)):
            for j in range(len(s),i,-1):
                if s[i:j] == s[i:j][::-1]:
                    if len(long_palindrome) < len(s[i:j]):
                        long_palindrome = s[i:j]
        return long_palindrome

ob = Solution ()
print(ob.longest_palindromic("babad"))
print(ob.longest_palindromic("cbbd"))
print(ob.longest_palindromic("a"))
print(ob.longest_palindromic("ac"))
