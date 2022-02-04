from version1.Elevator import Elevator
from version1.Floor import Floor


class Building:

    def __init__(self):
        self.floors = [Floor(), Floor(), Floor(), Floor()]
        self.elevator = Elevator()

    def next(self):
        for floor in self.floors:
            floor.next()
        self.elevator.next()

    def get_elevator_position(self):
        return self.elevator.get_position()

    def get_floors_count(self):
        return len(self.floors)

    def get_count_humans_in_floor(self, number):
        return self.floors[number].get_humans_count()