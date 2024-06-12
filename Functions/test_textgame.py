from textgame import is_palindrome


def test_is_palindrome_ci_ok():
    assert is_palindrome("Kayak")


def test_is_palindrome_ci_ko():
    assert not is_palindrome("python")


def test_is_palindrome_cs_ok():
    assert is_palindrome("kayak", case=True)


def test_is_palindrome_cs_ko():
    assert not is_palindrome("Kayak", case=True)