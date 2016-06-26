class Stats:

    def __init__(self, movement, attack, defence, damage):
        """
        Holds information about the characters current statistics
        Movement, Attack, Defence and Damage
        TODO - link to powers
        """
        self.movement = movement
        self.attack = attack
        self.defence = defence
        self.damage = damage

class CharacterInfo:

    def __init__(self, name, affiliations, stats):
        self.stats = stats
        self.name = name
        self.affiliations = affiliations
