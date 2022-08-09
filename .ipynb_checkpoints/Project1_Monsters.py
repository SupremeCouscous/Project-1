from Project1_Creature import *
import random
import time

class Monster(Creature):
    def set_data(self, *data):
        super().set_data(*data)
    def show_data(self):
        super().show_data()

class Ogre(Monster):
    def set_data(self, *data):
        super().set_data(*data)
    def show_data(self):
        super().show_data()
    def ogre_start(self):
        global ogre_name, ogre_race, ogre_con,ogre_pwr,ogre_dfc,ogre_luc
        ogre_name_list = ['Stonehead','Stonebrain','Thick']
        ogre_name = random.choice(ogre_name_list )
        ogre_race = 'ogre'
        ogre_con = random.randint(4,6)
        ogre_pwr = random.randint(4,6)
        ogre_dfc = random.randint(1,3)
        ogre_luc = random.randint(0,3)
        return ogre_name, ogre_race, ogre_con,ogre_pwr,ogre_dfc,ogre_luc
    def return_name(self):
        return(self.name)
    def return_race(self):
        return(self.race)
    def return_con(self):
        return(self.con)
    def return_pwr(self):
        return(self.pwr)
    def return_dfc(self):
        return(self.dfc)
    def return_luc(self):
        return(self.luc)

class Undead(Monster):
    def set_data(self, *data):
        super().set_data(*data)
    def show_data(self):
        super().show_data()
    def undead_start(self):
        global undead_name, undead_race, undead_con,undead_pwr,undead_dfc,undead_luc
        undead_name_list = ['Brittle','Tibia','Themer']
        undead_name = random.choice(undead_name_list)
        undead_race = 'undead'
        undead_con = random.randint(4,8)
        undead_pwr = random.randint(1,3)
        undead_dfc = random.randint(4,4)
        undead_luc = random.randint(0,1)
        return undead_name, undead_race, undead_con,undead_pwr,undead_dfc,undead_luc
    def return_name(self):
        return(self.name)
    def return_race(self):
        return(self.race)
    def return_con(self):
        return(self.con)
    def return_pwr(self):
        return(self.pwr)
    def return_dfc(self):
        return(self.dfc)
    def return_luc(self):
        return(self.luc)

class Goblin(Monster):
    def set_data(self, *data):
        super().set_data(*data)
    def show_data(self):
        super().show_data()
    def goblin_start(self):
        global goblin_name, goblin_race, goblin_con,goblin_pwr,goblin_dfc,goblin_luc
        goblin_name_list = ['Snitch','Ratnose','Shwifty']
        goblin_name = random.choice(goblin_name_list)
        goblin_race = 'goblin'
        goblin_con = random.randint(1,4)
        goblin_pwr = random.randint(1,3)
        goblin_dfc = random.randint(4,6)
        goblin_luc = random.randint(6,9)
        return goblin_name, goblin_race, goblin_con,goblin_pwr,goblin_dfc,goblin_luc
    def return_name(self):
        return(self.name)
    def return_race(self):
        return(self.race)
    def return_con(self):
        return(self.con)
    def return_pwr(self):
        return(self.pwr)
    def return_dfc(self):
        return(self.dfc)
    def return_luc(self):
        return(self.luc)

class Orc(Monster):
    def set_data(self, *data):
        super().set_data(*data)
    def show_data(self):
        super().show_data()
    def orc_start(self):
        global orc_name, orc_race, orc_con,orc_pwr,orc_dfc,orc_luc
        orc_name_list = ['Bloodmane','Teethbreaker','Curbstomp']
        orc_name = random.choice(orc_name_list)
        orc_race = 'orc'
        orc_con = random.randint(3,5)
        orc_pwr = random.randint(4,6)
        orc_dfc = random.randint(2,3)
        orc_luc = random.randint(2,4)
        return orc_name, orc_race, orc_con,orc_pwr,orc_dfc,orc_luc
    def return_name(self):
        return(self.name)
    def return_race(self):
        return(self.race)
    def return_con(self):
        return(self.con)
    def return_pwr(self):
        return(self.pwr)
    def return_dfc(self):
        return(self.dfc)
    def return_luc(self):
        return(self.luc)

class Dark_elf(Monster):
    def set_data(self, *data):
        super().set_data(*data)
    def show_data(self):
        super().show_data()
    def dark_elf_start(self):
        global dark_elf_name, dark_elf_race, dark_elf_con,dark_elf_pwr,dark_elf_dfc,dark_elf_luc
        dark_elf_name_list = ['Kabip','Lanik','Wadeep']
        dark_elf_name = random.choice(dark_elf_name_list)
        dark_elf_race = 'dark_elf'
        dark_elf_con = random.randint(2,5)
        dark_elf_pwr = random.randint(3,5)
        dark_elf_dfc = random.randint(1,3)
        dark_elf_luc = random.randint(1,9)
        return dark_elf_name, dark_elf_race, dark_elf_con,dark_elf_pwr,dark_elf_dfc,dark_elf_luc
    def return_name(self):
        return(self.name)
    def return_race(self):
        return(self.race)
    def return_con(self):
        return(self.con)
    def return_pwr(self):
        return(self.pwr)
    def return_dfc(self):
        return(self.dfc)
    def return_luc(self):
        return(self.luc)

def ogre_start():
    global ogre1
    ogre1 = Ogre()
    ogre1.ogre_start()
    ogre1.set_data(ogre_name, ogre_race, ogre_con,ogre_pwr,ogre_dfc,ogre_luc)

def undead_start():
    global undead1
    undead1 = Undead()
    undead1.undead_start()
    undead1.set_data(undead_name, undead_race, undead_con,undead_pwr,undead_dfc,undead_luc)

def goblin_start():
    global goblin1
    goblin1 = Goblin()
    goblin1.goblin_start()
    goblin1.set_data(goblin_name, goblin_race, goblin_con,goblin_pwr,goblin_dfc,goblin_luc)

def dark_elf_start():
    global dark_elf1
    dark_elf1 = Dark_elf()
    dark_elf1.dark_elf_start()
    dark_elf1.set_data(dark_elf_name, dark_elf_race, dark_elf_con,dark_elf_pwr,dark_elf_dfc,dark_elf_luc)

def orc_start():
    global orc1
    orc1 = Orc()
    orc1.orc_start()
    orc1.set_data(orc_name, orc_race, orc_con,orc_pwr,orc_dfc,orc_luc)

def monster_line_up():
    global lineup_list
    lineup_list = []
    for x in range(5):
        monster_tick = random.randint(0,4)
        if monster_tick == 0:
            ogre_start()
            lineup_list.append(ogre1)
        elif monster_tick == 1:
            undead_start()
            lineup_list.append(undead1)
        elif monster_tick == 2:
            goblin_start()
            lineup_list.append(goblin1)
        elif monster_tick == 3:
            orc_start()
            lineup_list.append(orc1)
        elif monster_tick == 4:
            dark_elf_start()
            lineup_list.append(dark_elf1)

    return lineup_list

# def monster_allocation():
#     global lineup_list, y_list, x_list
#     y_list = []
#     x_list = []
#     for ll in range(len(lineup_list)):
#         y1 = random.randint(0,9)
#         y_list.append(y1)
#         x1 = random.randint(0,9)
#         x_list.append(x1)
#     for ll2 in range(len(lineup_list)):
#         print('Monster',ll2,'is at Y:', y_list[ll2],'X:',x_list[ll2])
#         return y_list, x_list

#need to address recurring location

monster_line_up()