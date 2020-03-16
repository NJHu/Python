import matplotlib.pyplot as pyplot

def main():
    # x_values = [1, 2, 3, 4, 5]
    # y_values = [1, 4, 9, 16, 25]
    
    x_values = list(range(1, 1001))
    y_values = [x**2 for x  in x_values]
    
    #pyplot.scatter(x_values, y_values, s=40, edgecolor='none', c='red')
    pyplot.scatter(x_values, y_values, s=40, edgecolor='none', cmap=pyplot.cm.Blues, c=y_values)
    
    pyplot.title('title', fontsize=24)
    pyplot.xlabel('xValue', fontsize=14)
    pyplot.ylabel('yValue', fontsize=14)
    
    pyplot.tick_params(axis='both', which='major', labelsize=14)
    
    pyplot.axis([0, 1100, 0, 1100000])
    
    pyplot.show()
    
    pyplot.savefig('scatter_plot.png', bbox_inches='tight')

if __name__ == '__main__':
    main()
    