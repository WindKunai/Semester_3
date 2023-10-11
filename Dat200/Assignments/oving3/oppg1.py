def is_palindrome_iterative(word):
    left, right = 0, len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1

    return True


print("\nThe word hello being a palindrome is:", is_palindrome_iterative("hello"))  
print("The word racecar being a palindrome is:", is_palindrome_iterative("racecar"), "\n")


def is_palindrome_recursive(word):
    if len(word) <= 1:
        return True

    # sammenligner first og last bokstav
    if word[0] == word[-1]:
        # Hopper over first og last bokstav
        return is_palindrome_recursive(word[1:-1])

    return False

print("The word hello being a palindrome is:", is_palindrome_recursive("hello"))  # Output: False
print("The word racecar being a palindrome is:", is_palindrome_recursive("racecar"), "\n")  # Output: True
