import random


class gleb():

    def __init__(self, name):
        self.name = name
        self.weight = 70
        self.hp = 100
        self.hapiness = 100
        self.feed = 100
        self.money = 0
        self.lvl = 1
    def pvp(obj1,obj2):
        print(f'{obj1.name}({obj1.weight},Lvl:{obj1.lvl}) vs {obj2.name}({obj2.weight},Lvl:{obj1.lvl})')
        events = ['miss','hit','crit hit']
        step = False
        while obj2.hp > 0 and obj1.hp > 0:
            if step:
                hits = random.randint(1,5)
                for i in range(hits):
                    event = random.choice(events)
                    if event == 'miss':
                        print(f'Увы, {obj1.name} промахнулcя')
                    elif event == 'hit':
                        print(f'{obj1.name} ударил')
                        obj2.hp -= (obj1.weight // 10 + obj1.lvl)
                    elif event == 'crit hit':
                        print(f'{obj1.name} ударил со всей силы!!!')
                        obj2.hp -= (obj1.weight // 10 + obj1.lvl)*2
                    step = False
            elif step == False:
                hits = random.randint(1,5)
                for i in range(hits):
                    event = random.choice(events)
                    if event == 'miss':
                        print(f'Увы, {obj2.name} промахнулcя')
                    elif event == 'hit':
                        print(f'{obj2.name} ударил')
                        obj1.hp -= (obj2.weight // 10 + obj2.lvl)
                    elif event == 'crit hit':
                        print(f'{obj2.name} ударил со всей силы!!!')
                        obj1.hp -= (obj2.weight // 10 + obj2.lvl) * 2
                    step = True
        if obj1.hp <= 0:
            obj1.hp = 0
            print(f'{obj1.name} умер\nУ Скуфа {obj2.name} {obj2.hp}хп')
        elif obj2.hp <= 0:
            obj2.hp = 0
            print(f'{obj2.name} умер\nУ Скуфа {obj1.name} {obj1.hp}хп')


glebik = gleb('Глеб')
artem = gleb('Артем')
gleb.pvp(glebik,artem)
