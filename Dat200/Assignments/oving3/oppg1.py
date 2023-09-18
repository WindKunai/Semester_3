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
    # Remove spaces and convert to lowercase for case-insensitive comparison
    word = word.replace(" ", "").lower()

    # Base case: if the word is empty or has only one character, it's a palindrome
    if len(word) <= 1:
        return True
    
    if word[0] == word[-1]:
        
        return is_palindrome_recursive(word[1:-1])

    return False


print("The word hello being a palindrome is:", is_palindrome_recursive("hello"))  
print("The word racecar being a palindrome is:", is_palindrome_recursive("racecar"), "\n") 
