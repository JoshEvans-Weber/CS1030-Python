

def calculate(player_count, players_on_field):
    teams = int(player_count/players_on_field)
    players_per_team = player_count/teams
    print(f'{teams} teams are able to be made.\neach team will have about {players_per_team:.1f} players')
    pass

def initiate():
    try:
        globals()['player_count'] = int(input('How many players are present today?\n'))
        globals()['players_on_field'] = int(input('How many players willplay on the field at one time?\n'))
    except TypeError:
        print('Please try again, please provide number inputs')

def main():
    initiate()
    calculate(player_count, players_on_field)

if __name__ == '__main__':
    main()
    pass