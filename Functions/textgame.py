def is_palindrome(word: str, case: bool = False) -> bool:
    if not case:
        word = word.casefold()
    return word[::-1] == word

