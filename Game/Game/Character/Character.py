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

    def get_json(self):
        return {
            "movement": self.movement, "attack": self.attack, "defence": self.defence, "damage": self.damage
        }

class CharacterInfo:

    def __init__(self, name, affiliations, stats):
        self.stats = stats
        self.name = name
        self.affiliations = affiliations

    def get_json(self):
        return {
            "name": self.name, "dials": [x.get_json() for x in self.stats]
        }
