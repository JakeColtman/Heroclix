
class Unit:

    def __init__(self, name, affiliations, stats):
        self.stats = stats
        self.name = name
        self.dial = 0
        self.affiliations = affiliations
        self.alive = True
        self.actions_remaining = 1
        self.position = None

    def get_stats(self):
        return self.stats[self.dial]

    def inflict_damage(self, damage):
        self.dial += damage
        if self.dial == len(self.stats):
            self.alive = False

    def can_act(self):
        return self.actions_remaining > 0

    def reset_actions(self):
        self.actions_remaining = 1