import random
import time
from Project1_Creature import *
from Project1_Monsters import *
from Project1_Hero import *
from Project1_Mapping import *

global hero1
global lineup_list


def hero_combat_initialize(*data):
    global h_hp
    global h_atk
    global h_crit
    global h_dfc_rate
    global h_name
    # constitution to hp conversion
    h_hp = data[0] * 25
    # power to attack conversion
    h_atk = data[1] * 4.5
    # critical chance calculation
    h_crit = data[2] * 2.5
    # defence rating conversion
    h_dfc_rate = data[3]/20
    h_name = data[4]
    print('Hero HP:',h_hp,'Hero Attack: ',h_atk, "Hero crit chance: ", h_crit, "Hero defence:",h_dfc_rate)
    return h_hp, h_atk, h_crit, h_dfc_rate

def hero_combat_initialize2(*data):
    global h_hp
    global h_atk
    global h_crit
    global h_dfc_rate
    global h_name
    # constitution to hp conversion
    h_hp = data[0]
    # power to attack conversion
    h_atk = data[1] * 4.5
    # critical chance calculation
    h_crit = data[2] * 2.5
    # defence rating conversion
    h_dfc_rate = data[3]/20
    h_name = data[4]
    print('Hero HP:',h_hp,'Hero Attack: ',h_atk, "Hero crit chance: ", h_crit, "Hero defence:",h_dfc_rate)
    return h_hp, h_atk, h_crit, h_dfc_rate, h_name

def monster_combat_initialize(*data):
    global m_hp
    global m_atk
    global m_crit
    global m_dfc_rate
    global m_name
    global m_race
    # constitution to hp conversion
    m_hp = data[0] * 20
    # power to attack conversion
    m_atk = data[1] * 3
    # critical chance calculation
    m_crit = data[2]*2
    # defence rating conversion
    m_dfc_rate = (data[3]/20)
    m_name = str(data[4])
    m_race = str(data[5])
    print('Monster HP:',m_hp,'Monster Attack: ',m_atk, "Monster crit chance:", m_crit, "Monster defence:",m_dfc_rate)
    return m_hp, m_atk, m_crit, m_dfc_rate, m_name, m_race

def crit_chance(crit1,atk1):
    a = random.randint(1,100)
    # b = random.randint(80,120)
    if a > crit1:
        return atk1
    elif a <= crit1:
        time.sleep(1)
        print('it is a critical hit')
        return atk1*2


def fight_sequence(h_hp1, h_atk1, h_crit1, h_dfc1, m_hp1, m_atk1, m_crit1, m_dfc1,h_name1,m_name1,m_race1):
    print('-'*20,'combat mode','-'*20)
    global turn
    global post_fight_hp
    global monster_fought
    turn = 2
    while True:
        if turn == 2:
            if h_crit1/2.5 > m_crit1/2:
                turn = 0
                print(h_name1, 'managed to sneak up on', m_name1,'the',m_race1)
            elif h_crit1/2.5 < m_crit1/2:
                turn = 1
                print(h_name1,'You have been ambushed by ', m_name1,'the',m_race1)
        elif turn == 0:
            turn = 1
            time.sleep(1)
            print('Hero attacks')
            h_damage = round(crit_chance(h_crit1,(h_atk1-h_atk1*m_dfc1)))
            m_hp1 -= h_damage
            time.sleep(1)
            print(h_name1,' have caused', h_damage, 'damage to ', m_name1,'the',m_race1,' have',m_hp1,'left')
            print('-'*50)
            if m_hp1 < 0:
                print('you have won the fight')
                post_fight_hp = h_hp1
                monster_fought = m_race1
                return post_fight_hp, monster_fought
        elif turn == 1:
            turn = 0
            time.sleep(1)
            print('Monster attacks')
            m_damage = round(crit_chance(m_crit1,(m_atk1-m_atk1*h_dfc1)))
            h_hp1 -= m_damage
            print(m_name1,'the',m_race1, 'have caused', m_damage, 'damage to the hero have', h_hp1, 'hp left')
            print('-'*50)
            if h_hp1 < 0:
                print('YOU HAVE DIED')
                post_fight_hp = h_hp1
                monster_fought = m_race1
                return post_fight_hp, monster_fought

# def encounter():
#     global hero1
#     global lineup_list
#     for s in range(len(lineup_list)):
#         time.sleep(1)
#         print('-'*30)
#         monster_encountered = lineup_list[s].return_race()
#         print(hero1.return_name(),'have encountered a wild', monster_encountered)
#         print('Monster encountered stats')
#         if s == 0:
#             hero_combat_initialize(hero1.return_con(),hero1.return_pwr(),hero1.return_luc(),hero1.return_dfc())
#         elif s != 0:
#             hero_combat_initialize2(hero1.return_current_hp(), hero1.return_pwr(), hero1.return_luc(), hero1.return_dfc())
#         monster_combat_initialize(lineup_list[s].return_con(),lineup_list[s].return_pwr(),lineup_list[s].return_luc(),lineup_list[s].return_dfc())
#         while True:
#             battle_choice = input('will you fight or run ?')
#             if battle_choice == 'fight':
#                 print('you will fight like a man')
#                 print('-' * 30)
#                 fight_sequence(h_hp, h_atk, h_crit, h_dfc_rate, m_hp, m_atk, m_crit, m_dfc_rate)
#                 hero1.set_current_hp(hero1.return_name(),post_fight_hp)
#                 break
#             elif battle_choice == 'run':
#                 print('you run for your life')
#                 if hero1.return_luc() > 3:
#                     time.sleep(1)
#                     print('you have successfully become a pussy')
#                     break
#                 else:
#                     time.sleep(1)
#                     print('you have failed to escape')
#                     fight_sequence(h_hp, h_atk, h_crit, h_dfc_rate, m_hp, m_atk, m_crit, m_dfc_rate)
#                     hero1.set_current_hp(hero1.return_name(),post_fight_hp)
#                     break
#             else:
#                 print('please choose fight or run')


def hero_naming():
    global h_name, h_race
    h_name = input('Please input hero name : ')
    time.sleep(0.6)
    h_race = 'human'
    return h_name, h_race

def stat_randomize():
    global a, b, c, d
    while True:
        a = random.randint(1, 7)
        b = random.randint(1, 7)
        c = random.randint(1, 7)
        d = random.randint(1, 7)
        if a + b + c + d == 20:
            return a, b, c, d


def stat_initialize():
    global a,b,c,d
    xs = 3
    z = input('Type roll to determine for your stats : ')
    while xs ==3:
        if z == 'roll':
            stat_randomize()
            print('Constitution:', a,'Power', b, 'Luck:', c, 'Defence:', d)
            xs -= 1
            while xs!= 0:
                print('you have', xs, 'more rolls')
                g = input('would you like to reroll')
                if g == 'yes':
                    xs -= 1
                    stat_randomize()
                    print('Constitution:', a,'Power', b, 'Luck:', c, 'Defence:', d)
                elif g == 'no':
                    print('Constitution:', a,'Power', b, 'Luck:', c, 'Defence:', d)
                    return(a, b, c, d)
                else:
                    print('please type yes or no')
                    continue
        else:
            print('how difficult is it to type the word roll')
            stat_randomize()
            print('Constitution:', a,'Power', b, 'Luck:', c, 'Defence:', d)
            xs -= 1
            while xs!= 0:
                print('you have', xs, 'more rolls')
                g = input('would you like to reroll')
                if g == 'yes':
                    xs -= 1
                    stat_randomize()
                    print('Constitution:', a,'Power', b, 'Luck:', c, 'Defence:', d)
                elif g == 'no':
                    print('Constitution:', a,'Power', b, 'Luck:', c, 'Defence:', d)
                    return(a, b, c, d)
                else:
                    print('please type yes or no')
                    continue



def hero_start():
    global hero1,h_name,h_race,a,b,c,d
    hero1 = Hero()
    print('-'*100)
    print('You have entered character creation')
    print('-'*100)
    time.sleep(0.8)
    hero_naming()
    time.sleep(0.8)
    stat_initialize()
    hero1.set_data(h_name, h_race, a,b, c, d)
    hero1.show_data()
    hero1.set_current_hp(hero1.return_name(),int(a)*25)
    return hero1

def map_initialize():
    global map1
    map1 = Map()
    map1.form_map()
    map1.set_coordinate(4,4)
    time.sleep(1.5)
    map1.print_map()
    return map1

def movement():
    global y,x,oy,ox
    oy = map1.return_y()
    ox = map1.return_x()
    y = map1.return_y()
    x = map1.return_x()
    movement = input('W for North, S for South, D for East, A for West: ')
    if movement == 'w':
        if y > 0:
            y -= 1
        else:
            print('you have hit a wall')
            pass
    elif movement == 's':
        if y < 9:
            y += 1
        else:
            print('you have hit a wall')
            pass
    elif movement == 'd':
        if x < 9:
            x += 1
        else:
            print('you have hit a wall')
    elif movement == 'a':
        if x > 0:
            x -= 1
        else:
            print('you have hit a wall')
    else:
        pass
    return y, x, oy, ox

def game_start():
    global fight_tick
    fight_tick = 0
    time.sleep(1)
    print('-'*100)
    print('Welcome to Project 1')
    print('-'*100)
    time.sleep(1)
    print('This project will demonstrate the use of classes and interactions between instances')
    print('-'*100)
    return fight_tick

def monster_allocation():
    global lineup_list, yx_list
    yx_list = []

    for l1 in range(len(lineup_list)):
        y1 = random.randint(0,9)
        x1 = random.randint(0,9)
        a = str(y1)+str(x1)
        yx_list.append(a)

    for s1 in range(len(yx_list)):
        print('Monster',s1, 'is located at YX: ', end = '')
        print(yx_list[s1])
        print('')

    return yx_list

def map_encounter_check(my,mx):
    global monster_id, monster_encounter
    monster_encounter = 0
    a = str(my)+str(mx)
    for ss1 in yx_list:
        if ss1 == a:
            monster_id = yx_list.index(a)
            print('you have encountered monster ', monster_id)
            monster_encounter = 1
            return monster_id,monster_encounter
    for s1 in range(len(yx_list)):
        print('Monster', s1, 'is located at YX: ', end='')
        print(yx_list[s1])
        print('')

def soul_absorb(a):
    if a == 'orc':
        hero1.orc_soul(1)
    elif a == 'undead':
        pass
    elif a == 'dark_elf':
        hero1.dark_elf_soul(1)
    elif a == 'ogre':
        hero1.ogre_soul(1)
    elif a == 'goblin':
        hero1.goblin_soul(1)

game_start()
hero_start()
map_initialize()
monster_allocation()


while True:
    global hero1,monster_id,monster_encounter, fight_tick
    if int(hero1.return_current_hp()) < 0:
        print('you are exiting the game')
        quit()
    movement()
    map1.set_coordinate(y,x)
    map1.clear_path(oy,ox)
    map1.print_map()
    map_encounter_check(y, x)
    if monster_encounter == 1:
        fight_tick += 1
        monster_encountered = str(lineup_list[monster_id].return_name()+' the '+str(lineup_list[monster_id].return_race()))
        print('-'*100)
        print(hero1.return_name(), 'have encountered', monster_encountered)
        print('-'*100)
        if fight_tick == 0:
            hero_combat_initialize(hero1.return_con(), hero1.return_pwr(), hero1.return_luc(), hero1.return_dfc() , hero1.return_name())
        elif fight_tick != 0:
            hero_combat_initialize2(hero1.return_current_hp(), hero1.return_pwr(), hero1.return_luc(),
                                    hero1.return_dfc(), hero1.return_name())
        monster_combat_initialize(lineup_list[monster_id].return_con(), lineup_list[monster_id].return_pwr(),
                                  lineup_list[monster_id].return_luc(), lineup_list[monster_id].return_dfc(), lineup_list[monster_id].return_name(), lineup_list[monster_id].return_race())
        while True:
            battle_choice = input('will you fight or run ?')
            if battle_choice == 'fight':
                print('you will fight like a man')
                print('-' * 50)
                fight_sequence(h_hp, h_atk, h_crit, h_dfc_rate, m_hp, m_atk, m_crit, m_dfc_rate, h_name, m_name, m_race)
                hero1.set_current_hp(hero1.return_name(), post_fight_hp)
                print('you have captured the soul of the ', monster_fought)
                soul_absorb(monster_fought)
                time.sleep(1)
                hero1.show_data()
                time.sleep(1)
                map1.print_map()
                break
            elif battle_choice == 'run':
                print('you run for your life')
                if hero1.return_luc() > 3:
                    time.sleep(1)
                    print('you have successfully become a pussy')
                    map1.print_map()
                    break
                else:
                    time.sleep(1)
                    print('you have failed to escape')
                    fight_sequence(h_hp, h_atk, h_crit, h_dfc_rate, m_hp, m_atk, m_crit, m_dfc_rate, h_name, m_name)
                    hero1.set_current_hp(hero1.return_name(), post_fight_hp)
                    time.sleep(1)
                    print('-'*50)
                    print('you have captured the soul of the', monster_fought)
                    print('-' * 50)
                    soul_absorb(monster_fought)
                    time.sleep(1)
                    hero1.show_data()
                    time.sleep(1)
                    map1.print_map()
                    break
            else:
                print('please choose fight or run')




