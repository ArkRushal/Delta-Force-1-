
def isAlphabeticPalindrome(code):
    New = ""
    for i in code:
        if str.isalpha(i):
            New = str((i).lower) + New
    Reverse = ""
    for i in New:
        Reverse = Reverse + i
    if Reverse == New:
        return (True)
    else:
        return (False)
        

if __name__ == '__main__':
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))
