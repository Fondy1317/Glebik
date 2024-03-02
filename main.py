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

    def dela(self):
        while True:
            ChoiceD = int(input(f'--------------\nТекуший Голод - {self.feed}, Утолить голод - 1\nТекущее Здоровье - {self.hp},восполнить здоровье - 2\nТекущее Счастье - {self.hapiness},восполнить счастье - 3\nВернуться в меню - 4\n-------------\nВаш выбор - '))
            if ChoiceD == 1:
                self.find_food()
            elif ChoiceD == 2:
                self.sleep()
            elif ChoiceD == 3:
                self.fart_public()
            else:
                break
    def delo(self):
        self.hp -= 20
        self.hapiness -= 20
        self.feed -= 20
        self.exp += 10 + int(self.lvl // 10)
        if self.exp == self.lvl * 10:
            self.lvl += 1
            print(f'--------------\nВаш уровень повысился! Теперь ваш уровень {self.lvl}\n--------------')
        b = random.randint(0,3)
        if b == 1:
            self.events()
        if self.feed <= 0 or self.hp <= 0 or self.hapiness <= 0:
            self.death()

    def sleep(self):
        self.delo()
        self.hp += 50
    def fart_public(self):
        self.delo()
        self.hapiness += 50
    def find_food(self):
        self.delo()
        self.feed += 50
    def menu(self):
        while True:
            ChoiceM = int(input(f'--------------\nПриветствуем в Истории {self.name}!\nПерейти к делам {self.name} - 1\nПерейти в статистику - 2\nВаш выбор - '))
            if ChoiceM == 1:
                self.dela()
            else:
                self.stats()
    def stats(self):
        print(f'--------------\nУровень {self.name} - {self.lvl}\nЕго вес - {self.weight}\n')
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

gleb = gleb('glebik')
gleb.menu()


