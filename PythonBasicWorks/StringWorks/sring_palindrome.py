
# write a program to creater a function is_palindrome(word).
# return true if palindrome
# else return false


def is_palindrome(word):

    reverse_word=word[::-1]

    return True if word==reverse_word else False

print(is_palindrome("amma"))