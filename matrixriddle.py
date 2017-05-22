import random

def guess(numList, x, y):
    for line in range(10):
        pass

def printMatrix(matrix):
    for line in matrix:
        print line

def setup():
    pass
    
def randomize():
    matrix  = [[0,0,0],[0,0,0],[0,0,0]]
    numList = [1,2,3,4,5,6,7,8,9]
    
    for i in range(3 ):
        for j in range(3):
            randomIndex = random.randrange(len(numList))
            matrix[i][j] = numList[randomIndex]
            print 'setup() for1;for1 (matrix[i][j])', matrix[i][j]
            
            del numList[randomIndex]
            print 'setup() for1;for1 (len(numList))', len(numList)
    print 'finished', matrix
    
    return matrix

def swap(attempts):
    #solves the riddle by replacing nearby values in the matrix

    matrix = setup()
    count = 0
    x = 0
    y = 0
    
    print matrix
    printMatrix(matrix)


def guess(attempts):
    #solves the riddle by guessing the correct matrix 'attempts' amount of times
    
    matrix = setup()
    for range(attemps):
        matrix = setup()
    count = 0
    x = 0
    y = 0
    
    print matrix
    printMatrix(matrix)


def main():
    
    swap(10000)
    guess(10000)

if __name__ == '__main__':
    main()
    
    exit(0)
