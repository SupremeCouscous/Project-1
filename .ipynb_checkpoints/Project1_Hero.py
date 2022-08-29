from Project1_Creature import *
import time
import random

def stat_randomize():
    # global a, b, c, d
    while True:
        a = random.randint(1, 7)
        b = random.randint(1, 7)
        c = random.randint(1, 7)
        d = random.randint(1, 7)
        if a + b + c + d == 20:
            return a, b, c, d

class Hero(Creature):
    # def set_data(self, *data):
    #     super().set_data(*data)
    #
    # def show_data(self):
    #     super().show_data()

    def orc_soul(self, pwr):
        self.pwr += pwr

    def ogre_soul(self, con):
        self.con += con

    def dark_elf_soul(self, dfc):
        self.dfc += dfc

    def goblin_soul(self, luc):
        self.luc += luc

    def stat_initialize(self):
        a,b,c,d = stat_randomize()
        x = 3
        h_name = input('Please input hero name : ')
        print('-'*100)
        time.sleep(1)
        h_race = 'human'
        print('-'*100)
        z = input('Type roll to determine for your stats : ')
        print('-'*100)
        while x == 3:
            if z == 'roll':
                stat_randomize()
                print('Constitution:',a,'Power',b,'Luck:',c,'Defence:',d)
                x -= 1
                while x!= 0:
                    print('you have', x, 'more  rolls,', end = '')
                    g = input(' would you like to reroll : ')
                    print('-' * 100)
                    if g == 'yes':
                        x -= 1
                        stat_randomize()
                        print('Constitution:',a,'Power',b,'Luck:',c,'Defence:',d)
                        print('-' * 100)
                    elif g == 'no':
                        print('Constitution:',a,'Power',b,'Luck:',c,'Defence:',d)
                        self.set_data(h_name, h_race, a,b,c,d)
                        print('-' * 100)
                        break
                    else:
                        print('please type yes or no : ')
                        continue
            else:
                print('-' * 100)
                print('How difficult is it to type the word roll :')
                stat_randomize()
                print('Constitution:',a,'Power',b,'Luck:',c,'Defence:',d)
                print('-' * 100)
                x -= 1
                while x!= 0:
                    print('-' * 100)
                    print('You have', x, 'more rolls')
                    g = input(',would you like to reroll (yes/no) : ')
                    print('-' * 100)
                    if g == 'yes':
                        x -= 1
                        stat_randomize()
                        print('Constitution:',a,'Power',b,'Luck:',c,'Defence:',d)
                        print('-'*100)
                    elif g == 'no':
                        print('Constitution:',a,'Power',b,'Luck:',c,'Defence:',d)
                        self.set_data(h_name, h_race, a,b,c,d)
                        print('-' * 100)
                        break
                    else:
                        print('please type yes or no')
                        continue

    # access methods

    def return_name(self):
        return(self.name)

    def set_current_hp(self, h_current_hp):
        self.current_hp = h_current_hp
        print(self.return_name(),'\'s current hp is',h_current_hp)


    def return_current_hp(self):
        return(self.current_hp)

    def combat_initialize1(self):
        # constitution to hp conversion
        self.current_hp = self.return_con()*25
        # power to attack conversion
        self.atk = self.return_pwr()*4.5
        # critical chance calculation
        self.crit = self.return_luc()*2.5
        # defence rating conversion
        self.dfc_rate = self.return_dfc()/20
        print('Hero HP:', self.current_hp, 'Hero Attack: ', self.atk, "Hero crit chance: ", self.crit, "Hero defence:", self.dfc_rate)
        return self.return_name(),self.current_hp, self.atk, self.crit, self.dfc_rate

    def combat_initialize2(self):
        # power to attack conversion
        self.atk = self.return_pwr()* 4.5
        # critical chance calculation
        self.crit = self.return_luc()*2.5
        # defence rating conversion
        self.dfc_rate = self.return_dfc()/20
        print('Hero HP:', self.current_hp, 'Hero Attack: ', self.atk, "Hero crit chance: ", self.crit, "Hero defence:", self.dfc_rate)
        return self.return_name(),self.current_hp, self.atk, self.crit, self.dfc_rate


def main():
    hero1 = Hero()
    hero1.stat_initialize()
    hero1.show_data

if __name__ == '__main__':
    main()