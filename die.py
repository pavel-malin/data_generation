from random import randint

class Die():
    """A class that represents one cube."""
    
    def __init__(self, num_sudes=6):
        """The default hex key is used."""
        self.num_sudes = num_sudes

    def roll(self):
        """Returns a random number from 1 to the number of faces."""
        return randint(1, self.num_sudes)