def longestPalindrome(s: str) -> str:
    n = len(s)
    longest_palindrome = ""

    for center in range(n):
        left = right = center

        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1

        current_palindrome = s[left + 1:right]

        if len(current_palindrome) > len(longest_palindrome):
            longest_palindrome = current_palindrome
            
        left, right = center, center + 1

        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1

        current_palindrome = s[left + 1:right]

        if len(current_palindrome) > len(longest_palindrome):
            longest_palindrome = current_palindrome

    return longest_palindrome

print(longestPalindrome("babad"))