from random import randint
import pygal

class Die():
    def __init__(self, number_sides=6):
        self.number_sides = 6
    
    def roll(self):
        return randint(1, self.number_sides)


def main():
    die = Die()
    results = []
    for roll_number in range(1000):
        result = die.roll()
        results.append(result)

    frequences = []
    
    for value in range(1, die.number_sides + 1):
        frequence = results.count(value)
        frequences.append(frequence)
        
    print(frequences)
    
    hist = pygal.Bar()
    hist.title = "title"
    # hist.x_labels = [str(value) for value in range(1, die.number_sides + 1)]
    hist.x_labels = list(range(1, die.number_sides + 1))

    hist.x_title = "Xtitle"
    hist.t_title = "Ytitle"
    
    print(hist.x_labels)
    hist.add("D6", frequences)
    #hist.show()
    hist.render_to_file('die_visval.svg')
    

if __name__ == '__main__':
    main()
    
        