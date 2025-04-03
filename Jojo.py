from time import sleep
from dataclasses import dataclass
import keyboard
import random
from jojo_abil import Timestop, Erasing_time, Life, Barage

summon = 0
stamina = 120
opened_abilty = []


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

    def open_ability(self):
        global summon, stamina
        if summon % 2 == 0 and self.abilitys:
            self.potential -= 3
            new_ability = self.abilitys.pop(0)
            if new_ability not in opened_abilty:
                opened_abilty.append(new_ability)

    def summon_stand(self):

        global summon, stamina
        if stamina <= 0:
            print("Ты устал. Не удалось вызвать стенд")
        else:
            summon += 1

    def __str__(self):
        return (f"Имя: {self.name}\nСила: {self.charact(self.strength)}\nСкорость: {self.charact(self.speed)}\n"
                f"Точность: {self.charact(self.precision)}\nПотенциал: {self.charact(self.potential)}")

def log_abil(choice, opened_abilty):

    global stand_abil
    for ability in stand_abil:
        if ability.name == choice:
            if isinstance(ability, Erasing_time):
                ability.use(opened_abilty)

            elif isinstance(ability, Barage):
                ability.use(dmg_stand,stand)

            else:
                ability.use()
            return

    print("Способность не найдена!")





class Enemy:
    pass



stands = [
    Jojo_stand("Лох, у тебя нету стенда", 0, 0, 0, 0, []),
    Jojo_stand("Star Platinum", 11, 11, 11, 15, 
              ["Ora Ora", "Star finger", "Ora Ora kick", "Rage mode", "Star Platinum Time Stop"]),
    Jojo_stand("The World", 10, 10, 10, 15, ["Barage", "Knife", "Muda-Muda kick", "Rage mode", "Time stop"]),
    Jojo_stand("Silver Chariot", 6, 6, 6, 15, 
              ["Hora Hora", "Remove armour", "Dropping the rapier", "Fire watch"]),
    Jojo_stand("The Grateful Dead", 5, 4, 3, 15, ["Smoke", "Grab it", "Aging mode"]),
    Jojo_stand("King Crimson", 11, 11, 3, 15, ["Barage", "Donut", "Epitaph", "Rage mode", "Erasing time"]),
    Jojo_stand("Gold Experience", 7, 4, 3, 15, ["Barage", "Kick barrage", "Create life", "7-page Muda Muda"]),
    Jojo_stand("White Snake", 5, 4, 3, 15, ["Barage", "Memory disk", "Stand disk"])
]

evol_stands_arrow = {
    "Gold Experience": Jojo_stand("Gold Experience Requiem", 99, 99, 99, 15, ["Zero", "Create life"]),
}

evol_misc = {
    "White Snake" : Jojo_stand("C-moon", 10, 2, 4, 15, ["Gravity"]),
}

stand = random.choice(stands)
stand = stands[6]
print(stand)

dmg_stand = stand.strength


while True:
    stand.summon_stand()
    if stand.abilitys:
        stand.open_ability()
    else:
        break

print("\nСписок открытых способностей:")
for index, ability in enumerate(opened_abilty):
    print(f"{index + 1}. {ability}")

stand_abil = [
    Timestop(), Erasing_time(), Life(), Barage()
]


def arrow():
    global stand, opened_abilty
    if stand != stands[0]:
        print(f"{stand.name}\nХочешь воткнуть в себя стрелу? (R)")
        keyboard.wait("R")
        if stand.name in evol_stands_arrow:
            sleep(0.6)
            stand = evol_stands_arrow[stand.name]
            opened_abilty = stand.abilitys
            print(stand)
            print("\nСпособности:")
            for index, ability in enumerate(opened_abilty):
                print(f"{index + 1}. {ability}")
        else:
            print("нет такого ключа")
    else:
        print("Лоооххххххх")


def use_abil():
    global opened_abilty
    print("\nКакую способность хотите использовать?")
    for index, ability_name in enumerate(opened_abilty):
        print(f"{index + 1}. {ability_name}")
    while True:
        try:
            choice = int(input())
            if 0 <= choice - 1 < len(opened_abilty):
                choice_name = opened_abilty[choice - 1]
                print(f"Использование способности: {choice_name}")
                log_abil(choice_name, opened_abilty)
                break
        except ValueError:
            print("Введите правильное число!")



