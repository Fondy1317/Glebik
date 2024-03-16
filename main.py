import random
class gleb():
    def __init__(self,name):
        self.name = name
        self.weight = 70
        self.hp = 100
        self.hapiness = 100
        self.feed = 100
        self.money = 0
        self.lvl = 1
        self.exp = 0
        self.passivemoney = 0
        self.passivehp = 0
        self.passivehappy = 0
        self.passivefood = 0

    def dela(self):
        while True:
            ChoiceD = int(input(f'--------------\nТекуший Голод - {self.feed}, Утолить голод - 1\nТекущее Здоровье - {self.hp},восполнить здоровье - 2\nТекущее Счастье - {self.hapiness},восполнить счастье - 3\nВернуться в меню - 4\n-------------\nВаш выбор - '))
            if ChoiceD == 1:
                self.plus_food()
            elif ChoiceD == 2:
                self.plus_hp()
            elif ChoiceD == 3:
                self.plus_happy()
            else:
                break
    def delo(self):
        self.hp -= 10
        self.hapiness -= 10
        self.feed -= self.weight*0.1
        self.exp += 10 + int(self.lvl // 10)
        if self.exp == self.lvl * 10:
            self.lvl += 1
            print(f'--------------\nВаш уровень повысился! Теперь ваш уровень {self.lvl}\n--------------')
        b = random.randint(0,3)
        if b == 1:
            self.events()
        if self.feed <= 0 or self.hp <= 0 or self.hapiness <= 0:
            self.death()
        self.money += self.passivemoney
        self.hp += self.passivehp
        self.hapiness += self.passivehappy
        self.feed += self.passivefood

    def plus_hp(self):
        self.delo()
        self.hp += 50
    def plus_happy(self):
        self.delo()
        self.hapiness += 50
    def plus_food(self):
        self.delo()
        self.feed += 50
    def menu(self):
        while True:
            ChoiceM = int(input(f'--------------\nПриветствуем в Истории {self.name}!\nПерейти к делам {self.name} - 1\nПерейти в статистику - 2\nЗаработать денег - 3\nКупить компании - 4\nВаш выбор - '))
            if ChoiceM == 1:
                self.dela()
            elif ChoiceM == 2:
                self.stats()
            elif ChoiceM == 3:
                self.makemoney()
            elif ChoiceM == 4:
                self.passivesmth()
    def stats(self):
        print(f'--------------\nУровень {self.name} - {self.lvl}\nЕго вес - {self.weight}\nЕго количество денег - {self.money}')
    def brick(self):
        self.hapiness -= 30
        self.hp -= 30
        print('=====================\nВам упал кирпич на голову! Вот неудача!\n=====================')
    def bitting(self):
        self.hapiness -= 30
        self.hp -= 30
        print('=====================\nВас избили! Жизнь и так не сахар а сейчас еще и ребра ноют\n=====================')
    def fire(self):
        self.hapiness -= 30
        self.money -= 100
        print('=====================\nВас уволили с работы..\n=====================')
    def events(self):
        a = [self.bitting,self.fire,self.brick]
        random.choice(a)()
    def death(self):
        print('=====================\nВы погибли!\nПричиной смерти стал')
        if self.feed <= 0:
            print('Голод')
        if self.hp <= 0:
            print('Болезни')
        if self.hapiness <= 0:
            print('Депрессия')
        exit()
    def makemoney(self):
        while True:
            ChoiceM = int(input(f'--------------\nКак будете зарабатывать деньги?\nРаботать - 1\nКриминал - 2\nВыйти в меню - 4\nВаш выбор - '))
            if ChoiceM == 1:
                print('Вы поработали на славу!')
                self.money += 100 * self.lvl *0.5
                self.delo()
            elif ChoiceM == 2:
                d = random.randint(0,10)
                if d != 10:
                    print('Удача! Вам удалось подзаработать!!')
                    self.money += 200 * self.lvl * 0.5
                    self.delo()
                else:
                    print('Неудача!Вас загребли, пришлось дать взятку что стоило вам половину вашего состояния!')
                    self.money = self.money * 0.5
            elif ChoiceM == 4:
                break
    def passivesmth(self):
        ChoiceP = int(input(f'--------------\nЧто хотите сделать?\nКупить личную сеть ресторанов(пассивная сытость каждое действие, 50.000p) - 1\nКупить премиум абонемент в платную клинику(пассивное здоровье каждое действие, 65.000p) - 2\nКупить цирк - 3(пассивное счастье каждое действие, 30.000p)\nКупить бизнес - 4'))
        if ChoiceP == 1 and self.money >= 50000:
            self.money -= 50000
            self.passivefood += 20
        elif ChoiceP == 2 and self.money >= 65000:
            self.money -= 65000
            self.passivehp += 20
        elif ChoiceP == 3 and self.money >= 30000:
            self.money -= 30000
            self.passivehappy += 20
        elif ChoiceP == 4:
            ChoiceB = int(input(
                '--------------\nКупить Ларёк(10.000р) - 1\nКупить Маленький магазинчик(75.000) -2\nНичего не покупать - 3'))
            if ChoiceB == 1 and self.money >= 10000:
                self.money -= 10000
                self.passivemoney += 100
                self.delo()
            if ChoiceB == 2 and self.money >= 75000:
                self.money -= 75000
                self.passivemoney += 1000
                self.delo()


gleb = gleb('glebik')
gleb.menu()


