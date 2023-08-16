# class Human:
#     def __init__(self,name,color_of_hair,height,weight):
#         self.name = name
#         self.color_of_hair = color_of_hair
#         self.height = height
#         self.weight = weight
# human_obj = Human(name='иван',color_of_hair='red',height=190,weight=90)
# human_obj_2 = Human(name='сергей',color_of_hair='blue',height=170,weight=70)

# print(human_obj.name,human_obj.height)
# print(human_obj_2.name,human_obj_2.height)
# human_obj.weight=70
# human_obj.name='андрей'


# игра
import random
class Tank:
    ''' шаблон для танков'''
    def __init__(self,model,max_damage,min_damage,armor,helth):
        self.model = model
        self.damage = random.randint(max_damage,min_damage)
        self.armor =armor
        self.helth =helth
    def print_info(self):
        print(f'{self.model} имеет лобовую броню {self.armor} мм,{self.helth} едениц здоровья и {self.damage} едениц урона')
    def helth_down(self,enemy_damage):
        self.helth -= enemy_damage
        if self.helth > 0:
            print(f'\n{self.model}:')
            print(f'командир,в нас попали,осталось {self.helth} здоровья')
        else:
            print(f'\n{self.model}:')
            print(f'мы подбиты')
    def shot(self,enemy):
        if enemy.helth > 0 and self.helth >0:
            enemy.helth_down(self.damage)
            print(f'\n{self.model}:')
            print(f'точно в цель,у противника {enemy.model} осталось {enemy.helth} здоровья ')
        elif enemy.helth <= 0 and self.helth >0:
            print(f'\n{self.model}:')
            print(f'противник уничтожен')
        else:
            print(f'\n{self.model}:')
            print(f'нас уже подбили')


    
t_34= Tank('Т-34',25,40,90,100)
tiger= Tank('Tiger',25,40,120,100)
t_34.print_info()
tiger.print_info()
t_34.shot(tiger)
tiger.shot(t_34)
t_34.shot(tiger)
tiger.shot(t_34)
t_34.shot(tiger)
tiger.shot(t_34)
t_34.shot(tiger)