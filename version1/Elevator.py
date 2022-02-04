class Elevator:

    def __init__(self):
        self.capacityKG = 800
        self.workload = 0
        self.calls = []
        self.buttons = []
        self.position = 1
        self._is_open = False

    def next(self):
        pass

    def get_position(self):
        return self.position

    def is_open(self):
        return self._is_open

    def call(self, floor_number):
        self.calls.append(floor_number)