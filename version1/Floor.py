from version1.Human import Human
from random import randint


class Floor():

    def __init__(self):
        self.humans = []
        self.elevator_button = False

    def next(self):
        for human in self.humans:
            human.next()
        self._action()

    def _generate_human(self):
        human = Human()
        human.weightKG = randint(40, 100)
        human.going_to = randint(0, 3)
        return human

    def get_humans_count(self):
        return len(self.humans)

    def let_in(self):
        return self.humans.pop(0)

    def exist_human(self):
        if len(self.humans) > 0:
            return True
        return False

    #  совершает только одно действие с этажом
    #  движение человека до двери (стр12)
    def _action(self):
        if randint(1, 100) <= 5:
            self.humans.append(self._generate_human())
            self.elevator_button = True
        if not self.exist_human():
            self.elevator_button = False