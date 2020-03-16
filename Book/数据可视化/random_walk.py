from random import choice
import matplotlib.pyplot as pyplot

class RandomWalk():
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            
            if x_step == 0 and y_step == 0:
                continue
            
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)
    

def main():
    while True:
        random_walk = RandomWalk()
        random_walk.fill_walk()
        point_numbers = list(range(random_walk.num_points))
        
        pyplot.scatter(random_walk.x_values, random_walk.y_values, s=5, 
                       c=point_numbers, cmap=pyplot.cm.Blues, edgecolor='none')    
        
        # 突出起点和重点
        pyplot.scatter(0, 0, c='green', edgecolors='none', s=100)
        pyplot.scatter(random_walk.x_values[-1], random_walk.y_values[-1], c='red', edgecolors='none', s=100)
        
        # 隐藏最标轴
        pyplot.axes().get_xaxis().set_visible(False)
        pyplot.axes().get_yaxis().set_visible(False)
        
        pyplot.show()

        keep_running = input("make(y/n) : ")
        if keep_running == 'n':
            break

if __name__ == '__main__':
    main()
    