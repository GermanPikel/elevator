from version1.Elevator import Elevator
from version1.Floor import Floor


class Building:

    def __init__(self):
        self.floors = [Floor(), Floor(), Floor(), Floor()]
        self.elevator = Elevator()

    #  одно действие для здания
    def next(self):
        for floor in self.floors:
            floor.next()
        self.elevator.next()
        self._action()

    def get_elevator_position(self):
        return self.elevator.get_position()

    def get_floors_count(self):
        return len(self.floors)

    def get_count_humans_in_floor(self, number):
        return self.floors[number].get_humans_count()

    def _action(self):
        for i in range(len(self.floors)):
            if self.floors[i].elevator_button == True:
                self.elevator.call(i)
        if self.elevator.is_open() == True:
            elevator_position = self.elevator.position
            if self.floors[elevator_position].exist_human():
                human = self.floors[elevator_position].get_human()
                if self.elevator.check_workload(human.weightKG, self.elevator.capacityKG):
                    human = self.floors[elevator_position].let_in()
                    self.elevator.add_workload(human.weightKG)
                    self.elevator.goto_position.append(human)
                else:
                    self.elevator.close()
            else:
                self.elevator.close()
        # if len(self.elevator.calls) == 0 and self.elevator.position == 0:
        #     self.elevator.call(3)
        # elif len(self.elevator.calls) == 0 and self.elevator.position == 3:
        #     self.elevator.call(0)