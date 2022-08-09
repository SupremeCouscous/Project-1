class Creature():
    def set_data(self, *data):
        self.name = data[0]
        self.race = data[1]
        self.con = data[2]
        self.pwr = data[3]
        self.dfc = data[4]
        self.luc = data[5]
    def show_data(self):
        print('Name:', self.name)
        print('Race:', self.race)
        print('Constitution',self.con)
        print('Power:', self.pwr)
        print('Defence:',self.dfc)
        print('Luck:', self.luc)


