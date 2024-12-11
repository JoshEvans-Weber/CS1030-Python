
debug_value = 1

def debug():
    global first, last, w_num
    first = 'Jake'
    last = 'Mishin'
    w_num = 'w0012345'
    

def username_f(first, last, w_num):
    username_build = []
    username_build.append(first[0].lower())
    username_build.append(last[0].lower())
    username_build.append(w_num[4:9])
    return ''.join(username_build)

def password_f(first):
    password_build = []
    password_build.append(first.title())
    password_build.append('cs!')
    return ''.join(password_build)

if debug_value == True:
    debug()
else:
    first = input('Please enter your first name\n')
    tries = 0
    while len(first) == 0:
        first = input('Please enter your first name\n')
        tries += 1
        if tries == 3:
            exit()
    while first.isalpha() == False:
        print('Invalid first name.')
        first = input('Please enter your first name\n')
        tries += 1
        if tries == 3:
            exit()
    last = input('Please input your last name\n')
    while len(last) == 0:
        last = input('Please input your last name\n')
        tries += 1
        if tries == 3:
            exit()
    while last.isalpha() == False:
        print('Invalid last name.')
        last = input('Please input your last name\n')
        tries += 1
        if tries == 3:
            exit()
    w_num = str(input('Please input your W#\n'))
    while len(w_num) != 8:
        print('W# must be 8 characters')
        w_num = str(input('Please input your W#\n'))
        tries += 1
        if tries == 3:
            exit()
    while w_num[1:].isdigit() == False and w_num[0].lower() != 'w':
        print('W# must be "W" followed by 7 numbers')
        w_num = str(input('Please input your W#\n'))
        tries += 1
        if tries == 3:
            exit()

username = username_f(first, last, w_num)
password = password_f(first)

print(username)
print(password)