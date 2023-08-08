def palindrome(line):
    rev_line = ''.join(reversed(line))
    if rev_line == line:
        return True
    else:
        return False
stroka = 'радар' 
ans = palindrome(stroka)
print(ans)