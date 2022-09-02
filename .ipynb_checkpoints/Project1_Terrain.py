import random


def terrain_randomize():
    in_out_list =[]
    monster_locations = []
    bd_list = [0,9]
    a = random.randint(0,9)
    b = random.choice(bd_list)
    c = random.choice(bd_list)
    d = random.randint(0,9)
    in_out_list.append([a,b])
    in_out_list.append([c,d])
    for k in range(5):
            e = random.randint(0,9)
            f = random.randint(0,9)
            if [e,f] != in_out_list[0] and [e,f] != in_out_list[1]:
                monster_locations.append([e,f]) # how to not overlap

    return in_out_list, monster_locations


class location():
    def set_data(self, *data):
        self.y_value = data[0]
        self.x_value = data[1]
        self.symbol = data[2]
    def show_data(self):
        print(self.symbol, end = '')
        print(' | ', end = '')

class Map():

    def __init__(self):
        in_out_list, monster_locations = terrain_randomize()
        ab = tuple(in_out_list[0])
        cd = tuple(in_out_list[1])
        m1 = tuple(monster_locations[0])
        m2 = tuple(monster_locations[1])
        m3 = tuple(monster_locations[2])
        m4 = tuple(monster_locations[3])
        m5 = tuple(monster_locations[4]) # better way?
        terrain_list = []
        for y in range(0,10):
            terrain_list.append([])
            for x in range(0,10):
                location1 = location()
                if (y, x) == ab:
                    location1.set_data(y, x, 'I')
                elif (y, x) == cd:
                    location1.set_data(y, x, 'O')
                elif (y,x) == m1 or (y,x) == m2 or (y,x) == m3 or (y,x) == m4 or (y,x) == m5:
                    location1.set_data(y, x, 'M')
                else:
                    obstacle_chance = random.randint(0,100)
                    if obstacle_chance < 80:
                        location1.set_data(y, x, ' ')
                    else:
                        location1.set_data(y, x, '#')
                terrain_list[y].append(location1)
                self.map = terrain_list

    def set_coordinate(self,*data):
        self.h_y_value = data[0]
        self.h_x_value = data[1]

    def print_map(self):
        for y in range(len(self.map)):
            print('')
            print('-'*38)
            for x in range(len(self.map)):
                self.map[y][x].show_data()
        print('')
        print('-'*38)

map1 = Map()
map1.print_map()

    # def __init__(self):
    #     list = []
    #     for y in range(0,10):
    #         list.append([])
    #         for x in range(0,10):
    #             list[y].append('  ')
    #     self.map = list
    #
    # def clear_path(self,cy,cx):
    #     self.map[cy][cx] = '  '
# class Map():
#
#     def __init__(self):
#         list = []
#         for y in range(0,10):
#             list.append([])
#             for x in range(0,10):
#                 location1 = location()
#                 slist = [' #',' #','  ']
#                 s = random.choice(slist)
#                 location1.set_data(y,x,s)
#                 list[y][x].append(location1)
#         self.map = list
#
#     def print_map(self):
#         for y in range(len(self.map)):
#             print('')
#             print('-'*40)
#             for x in range(len(self.map)):
#                 print(self.map[y][x].show_data, '|', end = '')
#         print('')
#         print('-'*40)
#
# map1 = Map()
# map1.print_map()

    # def clear_path(self,cy,cx):
    #     self.map[cy][cx] = '  '


#     def set_data(self, *data):
#         self.terrain_type = data[0]
#         self.terrain_symbol = data[1]
#         self.y_value = data[2]
#         self.x_value = data[3]
#         # self.explored = data[4]
#         # self.drops = data[5]

#     def show_data(self):
#         print('Terrain type:', self.terrain_type)
#         print('Terrain_symbol', self.terrain_symbol)
#         print('Y_axis:', self.y_value)
#         print('X_axis',self.x_value)
#         # print('explored:',self.explored)
#         # print('drops:', self.drops)
#
#
#     def terrain_start(self):
#             terrain_name_list = ['wall','tree','Curbstomp']
#             terrain_
#             orc_race = 'orc'
#             orc_con = random.randint(3,5)
#             orc_pwr = random.randint(4,6)
#             orc_dfc = random.randint(2,3)
#             orc_luc = random.randint(2,4)
#             self.set_data(orc_name, orc_race, orc_con,orc_pwr,orc_dfc,orc_luc)


    # terrain_types = obstacle, land, entry, exit
    # y, x value = 0 to 9
    # explored = true false
    # drops = potion, side arm

# class MyClass:
#     def __init__(self, name):
#         self.name = name
#         self.pretty_print_name()
#
#     def pretty_print_name(self):
#         print("This object's name is {}.".format(self.name))
#
# my_objects = {}
# for i in range(1,11):
#     name = 'obj_{}'.format(i)
#     my_objects[name] = my_objects.get(name, MyClass(name = name))
#


