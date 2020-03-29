s=str(input('Enter the string:'))
for i in range(len(s)):
    print(s[i],s[-i-1])
    if s[i]==s[-i-1]:
        if i==len(s)-1:
            print('The string is palindrome')
    else:
        print('The string is not palindrome')
        break
