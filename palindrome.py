def isPalindrome(s):
    s = s.replace(" ","").lower()
    print(f'Converted String: {s}')
    return s == s[::-1]


string = input("Enter String: ")



if isPalindrome(string):
    print("Palindrome")
else:
    print("Not Palindrome")    