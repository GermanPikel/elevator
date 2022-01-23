from __future__ import annotations
from time import sleep
from random import randint

# начальные данные находятся в одном словаре
# люди создаются случайным образом
# симуляция работы лифта

information = {
    'floors': 8,
    'capacity': 800,
    'position': 5
}

class Human:
    def __init__(self, weight_kg=0, current_floor=0, going_to=0, difference=0, inside=False):
        self.weight = weight_kg
        self.current_floor = current_floor
        self.going_to = going_to
        self.difference = difference
        self.inside = inside  # В лифте или на этаже

    def set_difference(self, difference):
        self.difference = difference

    def __str__(self):
        return 'вес: ' + str(self.weight) + '  этаж нахождения: ' + str(self.current_floor) + '  хочет добраться: ' + str(self.going_to)

    def __lt__(self, other):
        return self.difference < other.difference



class Elevator:
    def __init__(self, floors=information['floors'], capacity=information['capacity'], position=information['position'], waiters=[], inside=[], workload=0):
        self.floors = floors
        self.capacity = capacity
        self.position = position
        self.waiters = waiters      # Список тех кто снаружи
        self.inside = inside        # Список тех кто внутри 
        self.workload = workload     

    def __lt__(self, other):
        for i in range(1, self.waiters):
            return self.waiters[i - 1].difference < self.waiters[i].difference

    # 1 действие программы
    def moving(self):
        for human in self.waiters:  # TODO: Сделать пересортировку ( update_waiters() )
            if human.current_floor == elevator.position:
                elevator.operation(elevator.position, human)
            elif human.current_floor > elevator.position:
                for floor in range(elevator.position, human.current_floor + 1):
                    print('лифт на %s этаже' % floor)
                    sleep(1)
                elevator.position = floor
                elevator.operation(elevator.position, human)
            else:
                for floor in range(elevator.position, human.current_floor - 1, -1):
                    print('лифт на %s этаже' % floor)
                    sleep(1.5)
                elevator.position = floor
                elevator.operation(elevator.position, human)
            self.waiters.remove(human)
            self.waiters = update_waiters(self.waiters)


    def check_capacity(self, human: Human, elevator):
        if elevator.workload + human.weight <= elevator.capacity:
            return True
        else:
            print('лифт пропускает человека, возможна перегрузка')

    def operation(self, floor, waiter: Human):  # Описывает, что происходит на этаже во время нахождения на нем лифта
        door = 'close'
        elevator.open_close(door, floor)
        door = 'open'
        capacity_ok = elevator.check_capacity(waiter, self)
        if capacity_ok:
            waiter.inside = not waiter.inside
            self.inside.append(waiter)
            sleep(3)
            print('лифт забрал/высадил человека')
            sleep(1)
            elevator.open_close(door, floor)
        else:
            skip_waiter()

    def stop(self):
        pass

    def open_close(self, door, floor):
        if door == 'close':
            print('лифт прибыл на', floor, 'этаж')
            sleep(1)
            print('двери открылись')
        else:
            print('двери закрылись и поехал дальше')
            sleep(1)

    def print(self):
        pass

    def __str__(self):
        waiters_list = []
        for waiter in self.waiters:
            waiters_list.append(waiter.__str__())
        return str(waiters_list)


def validate_elevator_parameters(floors: int, capacity: int, current_elevator_floor: int):
    if not (type(floors) == int and floors > 0):
        print('некорректное количество этажей, попробуйте снова')
        return False
    if type(capacity) != int or capacity < 0:
        print('некорреткная грузоподъемность лифта, попробуйте снова')
        return False
    if type(current_elevator_floor) == int and current_elevator_floor > 0:
        if current_elevator_floor > floors or current_elevator_floor < 1:
            print('некорректно введен текущий этаж лифта')
            return False
    else:
        print('некорректно введен текущий этаж лифта')
        return False

    return True


def validate_human_parameters(weight: int, current_person_floor: int, floors: int, going_to: int):
    if type(weight) == int and weight > 0 and type(current_person_floor) == int and 0 < current_person_floor <= floors and type(going_to) == int and 0 < going_to <= floors:
        return True
    else:
        print('некорректно введены данные')
        return False


def human_wish(current_floor, going_to):  # Проверяет, чтобы current_floor != going_to
    if current_floor == going_to:
        return False
    return True


def generate_human():
    while True:
        human = Human()
        human.weight = randint(40, 90)
        human.current_floor = randint(1, elevator.floors)
        human.going_to = randint(1, elevator.floors)
        if human_wish(human.current_floor, human.going_to):
            return human

# Оптимизировать работу лифта
def update_waiters(waiters: Elevator):
    waiters2 = []
    for waiter in waiters:
        difference = abs(waiter.current_floor - elevator.position)
        waiter.set_difference(difference)
        waiters2.append(waiter)
    waiters2.sort()

    return waiters2


def skip_waiter():
    pass


# Начало программы
while True:  # Проверяем валидатность лифта
    try:
        elevator = Elevator()
        floors = elevator.floors
        capacity = elevator.capacity
        current_elevator_floor = elevator.position
    except ValueError:
        print('некорректный ввод данных')
        continue

    if validate_elevator_parameters(floors, capacity, current_elevator_floor):
        elevator = Elevator(floors, capacity, current_elevator_floor, None)
        break
    else:
        exit()

started = False
waiters = []

while True:
    if not started:  # Начинаем работу лифта
        try:
            amount_people = randint(1, 5)
            started = True
            while amount_people > 0:
                try:
                    waiter = generate_human()
                    if validate_human_parameters(waiter.weight, waiter.current_floor, floors, waiter.going_to):
                        amount_people -= 1
                        waiter = Human(waiter.weight, waiter.current_floor, waiter.going_to)
                        difference = abs(waiter.current_floor - elevator.position)
                        waiter.set_difference(difference)
                        waiters.append(waiter)

                except ValueError:
                    print('некорректный ввод данных')
                    continue

        except ValueError:
            print('введите верное количество людей')
            continue

        elevator = Elevator(floors, capacity, current_elevator_floor, waiters)
        elevator.waiters.sort()
        for human in elevator.waiters:
            print(human)

    else:  # Начинаем бесконечный цикл работы лифта
        elevator.moving()
        break

