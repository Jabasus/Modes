import threading
import random
import time
from time import sleep
from sounds_jojo import Erasing_time_sound,barage_ge


class Abil:
    def __init__(self, duration):
        self.attack = duration
        self.name = ""

    def use(self):
        pass


class Barage(Abil):
    def __init__(self):

        self.name = "Barage"
        self.dmg = 2.2


    def use(self,dmg_stand,stand):
        dmg_barage = self.dmg * dmg_stand
        if stand.name == "Gold Experience":
            def sound_ge():
                barage_ge()
            def muda_barage():
                for i in range(25):
                    print("Muda")
                    sleep(0.25)

                sleep(0.55)
                print("MUDAAAAAAAAAAAA")
                sleep(0.5)
                print("Вы нанесли",dmg_barage)

            thread = threading.Thread(target=sound_ge)
            thread1 = threading.Thread(target=muda_barage)

            thread.start()
            thread1.start()

            thread.join()
            thread1.join()






class Life(Abil):
    def __init__(self):
        super().__init__(duration=None)
        self.name = "Create life"

    def use(self):
        enities = ["Frog", "Babochka", "Sneak"]

        energy_life = (10, 50)
        while True:
            try:
                time.sleep(0.5)
                choice_energy_life = int(
                    input(f"Сколько хотите вложить энергии в жизнь? ({energy_life[0]} - {energy_life[1]}): "))
                if energy_life[0] <= choice_energy_life <= energy_life[1]:
                    break

                else:
                    print(f"введи нормальное число {energy_life}")
            except ValueError:
                print("введи норм чисолр")

        time.sleep(0.4)
        for index, enity in enumerate(enities):
            print(f"{index + 1} {enity}")
        print("\nКакую форму жизни создать?")

        while True:
            try:

                choice_enety = int(input())
                if 0 <= choice_enety - 1 < len(enities):
                    choice_enety = enities[choice_enety - 1]
                    print(choice_enety)

                    if choice_enety == enities[0] or enities[1]:
                        position = [0, 0]
                        print(f"{choice_enety} появилась!")

                        acts = ["Attack", 'Protect']

                        for index, act in enumerate(acts):
                            print(f"{index + 1} {act}")
                        print("\nКакое действие задать жизни?")
                        while True:
                            try:
                                choice_act = int(input())
                                if 0 <= choice_act - 1 < len(acts):
                                    acts = ['атакует врага', "защищает вас"]
                                    choice_act = acts[choice_act - 1]
                                    print("Вы выбрали действие жизнм")
                                    break
                                else:
                                    print("Введите число")
                            except ValueError:
                                print("Введите число.")

                        if choice_act == "Protect":
                            result_energy_loop = choice_energy_life // 10
                            print(f"{choice_enety} {choice_act}")
                            for i in range(result_energy_loop):
                                position[0] += random.randint(-1, 1)
                                position[1] += random.randint(-1, 1)
                                print(f"позиция {choice_enety}: {position}")

                                chance = random.randint(0, 100)

                                if chance < 30:
                                    print(f" {choice_enety} {choice_act}! ")

                                time.sleep(1)

                            print(f"Жизнь исчезла...")
                        else:
                            result_energy_loop = choice_energy_life // 10
                            print(f"{choice_enety} атакует врага")
                            for i in range(result_energy_loop):

                                position[0] += random.randint(-1, 1)
                                position[1] += random.randint(-1, 1)
                                print(f"позиция {choice_enety}: {position}")

                                chance = random.randint(0, 100)

                                if chance < 30:
                                    print(f"✨ {choice_enety} успешно {choice_act}! ✨")

                                time.sleep(1)

                            print(f"Жизнь исчезла...")

                        break

                break
            except ValueError:
                print("Введите правильное число!")


class Timestop(Abil):
    def __init__(self):
        super().__init__(duration=None)
        self.name = "Time stop"

    def use(self):
        print("\nОстановка времени")
        choice = input("Ваши действия")


class Erasing_time(Abil):
    def __init__(self):
        super().__init__(duration=None)
        self.name = "Erasing time"

    def use(self, opened_abilty):
        def sound():
            Erasing_time_sound()

        def seconds():
            sec = 11
            for i in range(10):
                sec -= 1
                print(f"{sec} секунд")
                time.sleep(1)

        def erasing_time(opened_abilty):
            print("\nKING CRIMSON ВЫРЕЖИ ВРЕМЯ!")

            print("Доступные способности:")
            for index, ability in enumerate(opened_abilty):
                print(f"{index + 1}. {ability}")

        thread = threading.Thread(target=seconds)
        thread1 = threading.Thread(target=erasing_time, args=(opened_abilty,))
        thread2 = threading.Thread(target=sound)

        thread.start()
        thread1.start()
        thread2.start()

        thread.join()
        thread1.join()
        thread2.join()



