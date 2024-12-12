from pprint import pprint as pp
class Information:
    def __init__(self, name, pronoun, pronoun2,
                place, object, sport, hobby):
        self.name = name.title()
        self.pronoun = pronoun.title()
        self.pronoun2 = pronoun2.title()
        self.place = place.title()
        self.object = object
        self.sport = sport
        self.hobby = hobby
        self.pronoun3 = pronoun2.title()
        if self.pronoun2.lower() == 'him':
            self.pronoun3 = 'his'.title()
        if self.pronoun2.lower() == 'her':
            self.pronoun3 = 'her'.title()
        if self.pronoun2.lower() == 'them':
            self.pronoun3 == 'their'.title()
    
    def story(self):
        message = []
        message.append(f'''This is {self.name},''')
        message.append(f'''{self.pronoun} likes to play {self.sport},''')
        message.append(f'''{self.pronoun} also likes to do {self.hobby} in {self.pronoun3} spare time,''')
        message.append(f'''{self.pronoun2} favorite place to be is {self.place},''')
        message.append(f'''and {self.pronoun3} most prized posession is {self.object} ''')
        print(' '.join(message))
        
    def answers(self):
        self.answers = {}
        self.answers['name'] = self.name
        self.answers['pronoun'] = self.pronoun
        self.answers['pronoun2'] = self.pronoun2
        self.answers['place'] = self.place
        self.answers['object'] = self.object
        self.answers['sport'] = self.sport
        self.answers['hobby'] = self.hobby
        pp(self.answers)
 

def main():
    name = input('Enter your name.\n')
    while (''.join(name.split(' '))).isalpha() == False:
        name = input('Enter your name.\n')
    pronoun = input('Enter your first pronoun. ie: He / She\n')
    while pronoun.isalpha() != True:
        pronoun = input('Enter your first pronoun. ie: He / She\n')
    pronoun2 = input('Enter your second pronouns. ie: Him / Her\n')
    while pronoun2.isalpha() != True:
        pronoun2 = input('Enter your first pronoun. ie: He / She\n')
    place = input('What is your favorite place?\n')
    while place.isalpha() != True:
        place = input('What is your favorite place?\n')
    object = input('What is your most prized possession?\n')
    sport = input('What is your favorite sport?\n')
    while (''.join(sport.split(' '))).isalpha() == False:
        sport = input('What is your favorite sport?\n')
    hobby = input('What do you do for a hobby?\n')

    globals()[name] = Information(name, pronoun, pronoun2,
                                   place, object, sport, hobby)
    globals()[name].story()
    


if __name__ == '__main__':
    main()
    pass