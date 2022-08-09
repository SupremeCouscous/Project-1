from Project1_Creature import *
import time
import random

def stat_randomize():
    global a, b, c, d
    while True:
        a = random.randint(1, 7)
        b = random.randint(1, 7)
        c = random.randint(1, 7)
        d = random.randint(1, 7)
        if a + b + c + d == 20:
            return a, b, c, d

class Hero(Creature):
    def set_data(self, *data):
        super().set_data(*data)

    def show_data(self):
        super().show_data()

    def orc_soul(self, pwr):
        self.pwr += pwr

    def ogre_soul(self, con):
        self.con += con

    def dark_elf_soul(self, dfc):
        self.dfc += dfc

    def goblin_soul(self, luc):
        self.luc += luc

    # def hero_naming(self):
    #     global h_name, h_race
    #     h_name = input('Please input hero name : ')
    #     time.sleep(0.6)
    #     h_race = 'human'
    #     return h_name, h_race

    def stat_initialize(self):
        x = 3
        z = input('Type roll to determine for your stats : ')
        while x ==3:
            if z == 'roll':
                stat_randomize()
                print('Constitution:',a,'Power',b,'Luck:',c,'Defence:',d)
                x -= 1
                while x!= 0:
                    print('you have', x, 'more rolls')
                    g = input('would you like to reroll')
                    if g == 'yes':
                        x -= 1
                        stat_randomize()
                        print('Constitution:',a,'Power',b,'Luck:',c,'Defence:',d)
                    elif g == 'no':
                        print('Constitution:',a,'Power',b,'Luck:',c,'Defence:',d)
                        return(a,b,c,d)
                    else:
                        print('please type yes or no')
                        continue
            else:
                print('how difficult is it to type the word roll')
                stat_randomize()
                print('Constitution:',a,'Power',b,'Luck:',c,'Defence:',d)
                x -= 1
                while x!= 0:
                    print('you have', x, 'more rolls')
                    g = input('would you like to reroll')
                    if g == 'yes':
                        x -= 1
                        stat_randomize()
                        print('Constitution:',a,'Power',b,'Luck:',c,'Defence:',d)
                    elif g == 'no':
                        print('Constitution:',a,'Power',b,'Luck:',c,'Defence:',d)
                        return(a,b,c,d)
                    else:
                        print('please type yes or no')
                        continue


    def return_name(self):
        return(self.name)

    def set_current_hp(self, h_name, h_current_hp):
        self.current_hp = h_current_hp
        print(h_name,'\'s current hp is',h_current_hp)

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
    def return_current_hp(self):
        return(self.current_hp)



# def hero_start():
#     global hero1
#     hero1 = Hero()
#     print('-'*70)
#     print('You have entered character creation')
#     print('-'*70)
#     time.sleep(0.8)
#     hero1.hero_naming()
#     time.sleep(0.8)
#     hero1.stat_initialize()
#     hero1.set_data(h_name, h_race, a, b, c, d)
#     hero1.show_data()
#     hero1.set_current_hp(a*25)
#     return hero1


# hero_start()

# if __name__ == "__main__":
    # hero_start()