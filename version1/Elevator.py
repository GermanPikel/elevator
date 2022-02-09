class Elevator:

    def __init__(self):
        self.floors_count = 4
        self.capacityKG = 800
        self.workload = 0
        self.calls = []
        self.buttons = set()
        self.position = 0
        self.goto_position = []
        self._is_open = False

    #  совершает одно действие для лифта
    def next(self):
        self._action()

    def get_position(self):
        return self.position

    def is_open(self):
        return self._is_open

    def call(self, floor_number):
        if 0 <= floor_number < self.floors_count:
            if floor_number not in self.calls:
                self.calls.append(floor_number)

    def goto(self, floor_number):
        if 0 <= floor_number < self.floors_count:
            self.buttons.add(floor_number)

    def check_workload(self, weight, capacity):
        if (self.workload + weight) <= capacity:
            return True
        return False

    def add_workload(self, weight):
        self.workload += weight

    def close(self):
        self._is_open = False
        self.calls.remove(self.position)

    def __str__(self):
        return self.workload

    #  совершает только одно действие с лифтом
    def _action(self):
        if self.is_open() == False:
            if len(self.calls) >= 1:
                first_call = self.calls[0]
                if first_call > self.position:
                    self.position += 1
                elif first_call < self.position:
                    self.position -= 1
                else:
                    self._is_open = True
