from version1.Building import Building
from time import sleep


class Game:

    def __init__(self):
        self.building = Building()
        self.fps = 2

    def start(self):
        while True:
            self.building.next()
            self._show()
            sleep(1 / self.fps)

    # 0 | x | * * *
    def _show(self):
        print('---------------------')
        print(self.building.elevator.workload)
        # print(self.building.elevator.calls)
        elevator_position = self.building.get_elevator_position()
        count_floors = self.building.get_floors_count()
        for floor in range(count_floors - 1, -1, -1):
            x = ' '
            count_people = self.building.get_count_humans_in_floor(floor)
            if elevator_position == floor:
                x = 'x'
            print(floor, '|', x, '|', '*' * count_people)
