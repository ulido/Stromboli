class Species(object):
    def __init__(self, initial_number=0, name="S"):
        self.number = initial_number
        self._reactions = []
        self.name = name

    def _change(self, value):
        if self.number<-value:
            raise ValueError("Species number would become negative!")
        self.number += value

    def _register_reaction(self, reaction):
        self._reactions.append(reaction)

    def _get_dependent_reactions(self):
        return self._reactions

    def __repr__(self):
        return self.name + "[" + str(self.number) + "]"
