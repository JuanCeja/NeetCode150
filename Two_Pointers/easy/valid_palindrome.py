# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

# Example 1:
# Input: s = "Was it a car or a cat I saw?"
# Output: true
# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

# Example 2:
# Input: s = "tab a cat"
# Output: false
# Explanation: "tabacat" is not a palindrome.

def valid_palindrome(s: str) -> bool:
    clean_string = ''.join(c for c in s if c.isalpha()).lower()
    
    left = 0
    right = len(clean_string) - 1

    while (left <= right):
        if clean_string[left] != clean_string[right]:
            return False
        else:
            left += 1
            right -= 1

    return True

print(valid_palindrome("Was it a car or a cat I saw?")) # true
print(valid_palindrome("tab a cat")) # false