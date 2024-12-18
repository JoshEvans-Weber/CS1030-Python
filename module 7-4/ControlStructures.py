# Welcome Message
# Ask which party package
# Receive input
# Ask for membership
# Output Cost


cost = 0
pack_choice = 0
membership = 0
accepted_values = ['1', '2']
while pack_choice not in accepted_values:
    pack_choice = input('''Welcome to the Treehouse museum
What type of party Package would you like?:
1. Playtime Party
2. Deluxe Storybook Party
Enter Choice: ''')
    if pack_choice not in accepted_values:
        print('\nPlease enter "1" or "2" to make choice selection')

while membership not in accepted_values:
    membership = input('''Are you a member of the Treehouse Museum?
1. Yes
2. No
Enter Choice: ''')
    if membership not in accepted_values:
            print('\nPlease enter "1" for Yes and "2" for No.')
if pack_choice == '1':
    if membership == '1':
          cost = 125
    elif membership == '2':
         cost = 160
elif pack_choice == '2':
    if membership == '1':
          cost = 350
    elif membership == '2':
         cost = 275

print(f'Your cost would be ${cost}\n')