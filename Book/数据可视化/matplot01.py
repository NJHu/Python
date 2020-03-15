import matplotlib.pyplot as pyplot

def main():
    input_values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    pyplot.plot(input_values, squares, lineWidth=5)
    
    pyplot.title("title", fontsize=24)
    pyplot.xlabel("xLabel", fontsize=24)
    pyplot.ylabel("yLabel", fontsize=24)
    pyplot.tick_params(axis='both', labelsize=14)
    
    pyplot.show()


if __name__ == '__main__':
    main()
    
