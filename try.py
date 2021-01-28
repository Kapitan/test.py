import re
def is_all_upper(text: str) -> bool:
    # your code here
    test = r"[a-z]*"
    test2 = r"[A-Z]*"
    if text.isupper():
        return True
    elif re.match(test, text):
        return False
    else:
        return True

if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))
    print(is_all_upper(' '))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
 #   assert is_all_upper('') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")



test = r"[a-z]{6}"
test2 = r"[A-Z]*"

print(bool(re.findall(test, "text")))
