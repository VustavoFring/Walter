# ООП
# ---------------------------------------------------------------------
# программа игры 
class Person:
    def __init__(self,name,helth,damage,defence,endurance):
        # создаем атрибуты класса с заданными параметрами
        self.name = name
        self.helth = helth
        self.damage = damage
        self.defence = defence
        self.endurance = endurance
    # делаем методы класса
    def get_status(self):
        print(f'здоровье {self.name}:{self.helth}')
        print(f'урон {self.name}:{self.damage}')
        print(f'защита {self.name}:{self.defence}')
        print(f'выносливость {self.name}:{self.endurance}')
        print('-------------------------------------------')
    def make_damage(self,enemy,):
        print(f'атака по персонажу {enemy.name}')
        print('-----------------------------------------------------')
        enemy.get_damage(self.damage)
    def get_damage(self,damage):
        final_damage = damage - (damage * (self.defence / 100))
        print(f'по персонажу {self.name} наносится урон {final_damage}')
        print('--------------------------------------------')
        self.helth -= final_damage


surt = Person('сурт',100,20,20,80)
roshan = Person('рошан',120,15,25,60)




# наследование в ооп

class Mage(Person):
    def __init__(self, name, helth, damage, defence, endurance, magic_damage):
        super().__init__(name, helth, damage, defence, endurance)
        self.magic_damage = magic_damage
    
    def make_magic_damage(self,enemy):
        print(f'атака магией по персонажу {enemy.name}')
        print('-----------------------------------------------------')
        enemy.defence -= enemy.defence * 0.15
        enemy.get_damage(self.magic_damage)

invoker = Mage('Инвокер',80,10,10,100,35)
invoker.make_magic_damage(surt)
surt.get_status()
