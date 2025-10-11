class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while (left < right):
            #('A' <= ch <= 'Z') or ('a' <= ch <= 'z')
            if (not s[left].isalnum() and not s[right].isalnum()):
                left += 1
                right -= 1
            elif (not s[left].isalnum() and s[right].isalnum()):
                left += 1
            elif (s[left].isalnum() and not s[right].isalnum()):
                right -= 1
            elif (s[left].lower() == s[right].lower()):
                left += 1
                right -= 1
            else:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        ("0P", False),
        ("No lemon, no melon", True),
        ("Was it a car or a cat I saw?", True),
        ("12321", True),
        ("123a321", True),
        ("ab@a", True),
    ]

    for s, expected in tests:
        result = sol.isPalindrome(s)
        print(f"Input: {s!r}\nOutput: {result} | Expected: {expected}\n{'-'*40}")
