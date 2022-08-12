import random

class Map():


    def __init__(self):
        list = []
        for y in range(0,10):
            list.append([])
            for x in range(0,10):
                list[y].append(' ')
        self.map = list

    def clear_path(self,cy,cx):
        global list
        list[cy][cx] = ' x'

    def set_coordinate(self,*data):
        self.y_value = data[0]
        self.x_value = data[1]

    def print_map(self):
        print(self.y_value, self.x_value)
        list[self.y_value][self.x_value] = ' 0'
        for y in range(len(list)):
            print('')
            print('-'*40)
            for x in range(len(list)):
                print(list[y][x], '|', end = '')
        print('')
        print('-'*40)
        print('Y:',self.y_value,'X:',self.x_value)

    def return_x(self):
        return self.x_value
    def return_y(self):
        return self.y_value
#
# def map_initialize():
#     global map1
#     map1 = Map()
#     map1.form_map()
#     map1.set_coordinate(4,4)
#     return map1

# def movement():
#     global y,x,oy,ox
#     oy = map1.return_y()
#     ox = map1.return_x()
#     y = map1.return_y()
#     x = map1.return_x()
#     movement = input('W for North, S for South, D for East, A for West')
#     if movement == 'w':
#         if y > 0:
#             y -= 1
#         else:
#             print('you have hit a wall')
#             pass
#     elif movement == 's':
#         if y < 9:
#             y += 1
#         else:
#             print('you have hit a wall')
#             pass
#     elif movement == 'd':
#         if x < 9:
#             x += 1
#         else:
#             print('you have hit a wall')
#     elif movement == 'a':
#         if x > 0:
#             x -= 1
#         else:
#             print('you have hit a wall')
#     else:
#         pass
#     return y, x, oy, ox
#
# def clear_path(cy,cx):
#     list[cy][cx] = ' x'

# if __name__ == "__main__":
#     map_initialize()
#
#     while True:
#         movement()
#         map1.set_coordinate(y,x)
#         clear_path(oy,ox)
#         map1.print_map()




