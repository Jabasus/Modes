
from time import sleep
from dataclasses import dataclass
import keyboard
import random
from jojo_abil import Timestop, Erasing_time, Life, Barage

summon = 0
stamina = 120
opened_abilty = []

erasing_time = Erasing_time()
erasing_time.use(opened_abilty)
@dataclass
class Jojo_stand:
    name: str
    strength: int
    speed: int
    precision: int
    potential: int
    abilitys: list

    def charact(self, param):
        if param >= 11:
            return "A"
        elif param >= 7:
            return "B"
        elif param >= 4:
            return "C"
        elif param > 0:
            return "E"
        else:
            return "0"

    def open_ability(self, stand):
        global summon, stamina
        if summon % 2 == 0:
            if stand.abilitys:
                self.potential -= 3
                new_ability = stand.abilitys[0]
                opened_abilty.append(new_ability)
                stand.abilitys.pop(0)

    def summon_stand(self, stand):
        global summon, stamina
        if stamina <= 0:
            print("Ты устал. Неудалось вызвать стенд")
        else:
            summon += 1

    def __str__(self):
        return (f"Имя: {self.name}\nСила: {self.charact(self.strength)}\nСкорость: {self.charact(self.speed)}\n"
                f"точность: {self.charact(self.precision)}\nПотенциал: {self.charact(self.potential)}")


def log_abil(choice):
    global stand_abil, opened_abilty  # Добавляем opened_abilty в область видимости
    for ability in stand_abil:
        if ability.name == choice:
            print(f"Использование способности: {ability.name}")
            
            # Передаём opened_abilty, если это Erasing_time
            if isinstance(ability, Erasing_time):
                ability.use(opened_abilty)
            else:
                ability.use()
                
            return
    print("Способность не найдена!")()


stands = [
    Jojo_stand("Лох у тебя нету стенда", 0, 0, 0, 0, [""]),

    Jojo_stand("Star Platinum", 11, 11, 11, 15,
              ["Ora Ora", "Star finger", "Ora Ora kick", "Rage mode", "Star Platinum Time Stop"]),
    Jojo_stand("The World", 10, 10, 10, 15, ["Barage", "Knife", "Muda-Muda kick", "Range mode", "Time stop"]),
    Jojo_stand("Silver chariot", 6, 6, 6, 15,
              ["Hora Hora", "Remove armour", "Dropping the rapier", "S", "fire watch"]),

    Jojo_stand("The Grateful Dead", 5, 4, 3, 15, ["Smoke", "Grab it", "Aging mode"]),
    Jojo_stand("King Crimson", 11, 11, 3, 15, ["Barage", "Donut", "Epitaph", "Rage mode", "Erasing time"]),
    Jojo_stand("Gold Experiance", 5, 4, 3, 15, ["Barage", "Kick barage", "Create life", "7 page Muda Muda"]),

    Jojo_stand("White Snake", 5, 4, 3, 15, ["Barage", "Memory disk", "Stand disk"])

]

evol_stands_arrow = {
    "Gold Experiance": Jojo_stand("Gold Experiance Requiem", 99, 99, 99, 15, ["Zero","Create life",""]),

    "White Snake": Jojo_stand("C-moon", 10, 4, 1, 15, ["Gravity"])
}

stands7 = []


stand = random.choice(stands)

stand_enemy = random.choice(stands)

stand = (stands[5])
stand.open_ability(stand)

print(stand)

print("\nСпособности:")
print(*opened_abilty)

while True:
    stand.summon_stand(stand)

    if stand.abilitys:
        stand.open_ability(stand)
    else:
        break

print("\nСписок способностей:")
for index, ability in enumerate(opened_abilty):
    print(f"{index + 1}. {ability}")

stand_abil = [
    Timestop(), Erasing_time(), Life(), Barage()
]



def arrow():
    global stand, opened_abilty
    if stand != stands[0]:
        print(stand.name)
        print("Хочешь воткнуть в себя стрелой?(R)")
        keyboard.wait("R")
        if stand.name in evol_stands_arrow:
            print("АТкой ключ есть")
            sleep(0.6)
            stand = evol_stands_arrow[stand.name]
            print(stand)
            opened_abilty = stand.abilitys

            print("\nСпособности:")
            for index, ability in enumerate(opened_abilty):
                print(f"{index + 1}. {ability}")
        else:
            print("Неиту ключаr")
    else:
        print("лохххххххх")

def use_abil():
    global opened_abilty
    print("\nчто хоотите исполльзовать?:")
    for index, ability_name in enumerate(opened_abilty):
        print(f"{index + 1}. {ability_name}")
    while True:
        try:
            choice = int(input())
            if 0 <= choice - 1 < len(opened_abilty):
                choice_name = opened_abilty[choice - 1]
                print(choice_name)
                log_abil(choice_name)
                break
        except ValueError:
            print("Введите правильное число!")


use_abil()