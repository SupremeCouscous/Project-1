from Project1_Terrain import *
from Project1_Hero import *
from Project1_Monsters import *
from Project1_battle import *

def game_start():
    time.sleep(1)
    print('-'*100)
    print('Welcome to Project 1')
    print('-'*100)
    time.sleep(1)
    print('This project will demonstrate the use of classes and interactions between instances')
    print('-'*100)


def hero_start():
    hero1 = Hero()
    time.sleep(0.8)
    hero1.show_data()
    hero1.set_current_hp(int(hero1.return_con() * 25))
    return hero1

game_start()
hero1 = hero_start()
map1 = map_initialize()
lineup_list = monster_line_up()
map1.index_mapping(lineup_list)

while True:
    map1.movement()
    map1.print_map()
    map1.show_h_coordinate()
    if
        battle(hero1,monster_line_up)

