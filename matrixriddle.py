import random

def printMatrix(matrix):
    for line in matrix:
        print '\t', line

def verify(numList):
    firstTest = True
    firstValue = 0
    cases = []
    
    #3 Cases: Horizontal, Vertical, Diagonal
    #Case1
    for i in range(3):
        row = 0
        
        for j in range(3):
            row += numList[i][j]

        if firstTest == True:
            firstValue = row
            firstTest = False
        else:
            if row != firstValue:
                firstValue = True
                firstTest = 0
                break
                
            elif i == 2:
                cases.append(1)
        
    #Case2
    for i in range(3):
        column = 0
        
        for j in range(3):
            column += numList[j][i]

        if firstTest == True:
            firstValue = column
            firstTest = False
        else:
            if column != firstValue:
                del firstTest
                del firstValue
                break
                
            elif i == 2:
                cases.append(1)
    #Case3
    diagonal = [0,0]
    
    for i in range(3):
        diagonal[0] += numList[i][i]
    
    for i in range(3):
        diagonal[1] += numList[i][-i-1] 
        
    if diagonal[0] == diagonal[1]:
        if len(cases) == 2:
            return True
        else:
            return False

def randomize():
    matrix  = [[0,0,0],[0,0,0],[0,0,0]]
    numList = [1,2,3,4,5,6,7,8,9]
    
    for i in range(3):
        for j in range(3):
            randomIndex = random.randrange(len(numList))
            matrix[i][j] = numList[randomIndex]
            
            del numList[randomIndex]
    
    return matrix

def guess(attempts):
    #solves the riddle by guessing the correct matrix 'attempts' amount of times
    
    for i in range(attempts):
        print 'Attempt no.%d' % (i + 1)
        matrix = randomize()
        answer = verify(matrix)
        
        if answer == True:
            return matrix

    else:
        print 'Unable to find solution in %d attempts. Terminating program...' % attempts
        exit(1)
        
def main():
    attempts = int( raw_input('How many attempts do you want to do? ') )
    
    answer = guess(int(attempts))

    print 'Answer:' 
    printMatrix(answer)
    
if __name__ == '__main__':
    main()
    
    exit(0)
