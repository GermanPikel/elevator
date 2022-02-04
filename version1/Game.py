from version1.Building import Building
from time import sleep


class Game:

    def __init__(self):
        self.building = Building()

    def start(self):
        while True:
            self.building.next()
            self._show()
            sleep(1)

    def _show(self):
        elevator_position = self.building.get_elevator_position()
        print('позиция лифта:', elevator_position)
        count_floors = self.building.get_floors_count()
        for floor in range(count_floors - 1, -1, -1):
            count_people = self.building.get_count_humans_in_floor(floor)
            print('на', floor, 'этаже', count_people, 'людей')
