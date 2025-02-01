def isPalindrome(word):
    for left in range(len(word)//2):
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False

    return True

print(isPalindrome("radar"))
