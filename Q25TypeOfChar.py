char = input('Enter a character = ')
special_char = '[@_!#$%^&*().<>?/\|}{~:]'  
if char.islower(): 
    print('Lowercase')
elif char.isupper(): 
    print('Uppercase')
elif char in special_char: 
    print('Special Character')
