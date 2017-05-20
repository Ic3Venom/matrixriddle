

def guess(numList, x, y):
    pass


def printMatrix(matrix):
    for line in matrix:
        print line


def swap():
    #solves the riddle by replacing nearby values in the matrix
    
    numList = range(1,10)
    matrix = [[0,0,0],[0,0,0],[0,0,0]]
    
    print numList, matrix
    printMatrix(matrix)


def random(attempts):
    #solves the riddle by guessing the correct matrix 'attempts' amount of times
    
    numList = range(1,10)
    matrix = [[0,0,0],[0,0,0],[0,0,0]]
    
    print numList, matrix
    printMatrix(matrix)


def main():
    
    swap()
    random(10000)

if __name__ == '__main__':
    main()
    
    exit(0)