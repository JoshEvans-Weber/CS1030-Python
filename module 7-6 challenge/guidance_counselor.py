counselors = {'Marci Thomas':['A','B','C','D'], 
              'Robert Hancock':['E','F','G','H','I','J','K'],
              'John Caine':['L','M','N','O','P','Q','R'],
              'Lacy Peterson':['S','T','U','V','W','X','Y','Z']}
print('Boneville High School Counselor')
name = input('Enter your last name: ')
while name.isalpha() is False:
    name = input('[Invalid Input] Please enter your last name: ')
for key in counselors:
    if name[0].title() in counselors[key]:
        print(f'Your counselor is {key}')