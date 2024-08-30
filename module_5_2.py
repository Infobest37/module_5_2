class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        print(f"ЖК называется '{self.name}', этажей в доме '{self.number_of_floors}', этаж номер '{self.new_floor}' ")

        if self.number_of_floors < 1 or self.new_floor > self.number_of_floors:
            print(f"В ЖК '{self.name}' Такого этажа не существует")
            return
        else:
            for i in range(1,self.new_floor + 1):
                print(i)

            print(f"Добро пожаловать на '{self.new_floor}' этаж")
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f"ЖК '{self.name}' колличество этажей '{self.number_of_floors}' ")


hous = House('ЖК Горский', 28)
hous1 = House('Домик в деревне', 7)
hous.go_to(8)
hous1.go_to(8)

print(len(hous))
print(len(hous1))
print(str(hous))
print(str(hous1))


