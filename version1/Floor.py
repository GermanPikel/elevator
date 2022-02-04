from version1.Human import Human


class Floor():

    def __init__(self):
        self.humans = [Human(), Human(), Human()]
        self.elevator_button = False

    def next(self):
        for human in self.humans:
            human.next()
        self._generate_human()

    def _generate_human(self):
        pass

    def get_humans_count(self):
        return len(self.humans)
