try:
    age = (int(input('Please enter your age.\n')))
except TypeError:
    print('invalid input')
    exit()
if age >= 18:
    print("You can get a drivers license!")
elif age >= 15 and age < 18:
    print('You can get a learners permit')
elif age < 15:
    print('You are not able to drive yet.')
