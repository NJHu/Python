import csv
from matplotlib import pyplot

def main():
    filename = 'sitka_weather_history_2014.csv'
    with open(filename) as file:
        reader = csv.reader(file)
        header_low = next(reader)
        
        highs = []
        for row in reader:
            if len(row) > 0:
                highs.append(row[1])
        print(highs)
        fig = pyplot.figure(dpi=128, figsize=(10, 6))
        pyplot.plot(highs, c='red')
        pyplot.title("title", fontsize=24)
        pyplot.xlabel('XLabel', fontsize=10)
        pyplot.ylabel('YLabel', fontsize=10)
        pyplot.tick_params(axis='both', which='major', labelsize=16)
        pyplot.show()
        
            
if __name__ == '__main__':
    main()
    