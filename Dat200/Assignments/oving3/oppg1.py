def is_palindrome_iterative(word):
    left, right = 0, len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1

    return True

def is_palindrome_recursive(word):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    word = word.replace(" ", "").lower()

    # Base case: if the word is empty or has only one character, it's a palindrome
    if len(word) <= 1:
        return True
    
    if word[0] == word[-1]:
        
        return is_palindrome_recursive(word[1:-1])

    return False


while True:
    word = input("\nInput word: ")
    if word == "exit":
        sure = input("you sure? y/n: ").lower()
        if sure == "y":
            break
        else:
            word = input("Input word")
    if is_palindrome_iterative(word):
        print(f"\nthe word {word} is a palindrome (using interative method)")
    else:
        print(f"\nthe word {word} is not a palidrome (using interative method)")
    if is_palindrome_recursive(word):
        print(f"the word: {word}, is apalindrome (using recursive method)")
    else:
        print(f"the word: {word}, is not a palindrome (using recursive method)")