import random as rnd

#  Constant lists
PREF = ['Captain', 'Sir', 'Madame', 'The', 'Sinister']
POWR = ['fire', 'water', 'earth', 'air']
DESC = ['summon', 'create', 'manipulate', 'throw']

#  Constant Dictionaries
NAME = {'fire': rnd.choice(['Blaze', 'Inferno']),
    'water': rnd.choice(['Tsunami', 'Tide']),
    'air': rnd.choice(['Storm', 'Jetstream']),
    'earth': rnd.choice(['Quake', 'Monolith'])
}
LEVL = {'summon': 10, 'create': 15, 'manipulate': 10, 'throw': 5,  # End descriptions #
    'fire': 10, 'water': 15, 'earth': 20, 'air': 30,  # End powers #
    'Captain': 5, 'Sir': 5, 'Madame': 7, 'The': 10, 'Sinister': 12  # End Prefixes #
}

#  For len of POWR and DESC lists
master_rand = rnd.randint(0, 3)

class HeroProfile:
    
    def __init__(self, prefix = rnd.choice(PREF), power = POWR[master_rand],
    name = NAME[POWR[master_rand]], pow_desc = rnd.choice(DESC)):
        """Create a new HeroProfile"""
        self.pref = prefix
        self.pow = power
        self.nm = name
        self.pd = pow_desc
        self.lv = LEVL[prefix] + LEVL[power] + LEVL[pow_desc]
        
    def __repr__(self):
        """Representation method"""
        return f'{self.pref} {self.nm}'
        
    def print_profile(self):
        """Print all info"""
        print(f'Hero Name: {self.pref} {self.nm}')
        print()
        print(f'Power Description: {self.pref} {self.nm} can {self.pd} {self.pow}')
        print(f'Power Level: {self.lv}')
