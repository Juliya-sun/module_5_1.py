class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.go_to()

    def go_to(self, new_floor):
        for new_floor in range (1, self.number_of_floors):
            print(new_floor)
            break
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

