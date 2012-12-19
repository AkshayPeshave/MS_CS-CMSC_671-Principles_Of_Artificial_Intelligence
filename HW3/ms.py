from constraint import *
import time
import sys

def createMagicSquare(squareSize):
    problem = Problem() 
    
    magicSum = squareSize*(((squareSize*squareSize)+1)/2)
    elements = squareSize*squareSize
    
    problem.addVariables(range(0,elements), range(1, elements+1))
    problem.addConstraint(AllDifferentConstraint(), range(0, elements))
    
    problem.addConstraint(ExactSumConstraint(magicSum),
                          [(squareSize*i)+i for i in range(squareSize)])
    
    
    
    for row in range(squareSize):
        problem.addConstraint(ExactSumConstraint(magicSum),
                              [row*squareSize+i for i in range(squareSize)])
    for col in range(squareSize):
        problem.addConstraint(ExactSumConstraint(magicSum),
                              [col+squareSize*i for i in range(squareSize)])

    problem.addConstraint(ExactSumConstraint(magicSum),
                          [((squareSize)*(i+1))-(i+1) for i in range(squareSize)])
    ##backtracking solver
        
    problem.setSolver(BacktrackingSolver())
    
    start = time.time()
    solution = problem.getSolution()
    
    stop = time.time()
    
    print 'Solution using BacktrackingSolver()...time taken %.3f seconds' % (stop-start)
    print '\n'
    
    #for s in solution:
    for row in range(squareSize):
        for col in range(squareSize):
            print solution[row*squareSize+col],
        print
    print
    print


    ##recursive backtracking

    problem.setSolver(RecursiveBacktrackingSolver())

    start = time.time()
    solution = problem.getSolution()
    stop = time.time()

    print 'Solution using RecursiveBacktrackingSolver()...time taken %.3f seconds' % (stop-start)
    print '\n'
    

    #for s in solution:
    for row in range(squareSize):
        for col in range(squareSize):
            print solution[row*squareSize+col],
        print
    print
    print
        
    ##MinConflictsSolver()

    problem.setSolver(MinConflictsSolver())

    start = time.time()
    solution = problem.getSolution()
    stop = time.time()

    print 'Solution using MinConflictsSolver()...time taken %.3f seconds' % (stop-start)
    print '\n'
    print solution
    
def main():
    createMagicSquare(3)
    createMagicSquare(4)
    createMagicSquare(5)



if __name__ == "__main__":

    # 1st command line arg is always the command name (e.g., my.py)
    nargs = len(sys.argv)

    # Note that we call eval on any command line arguments to convert
    # the string into a python data structure

    if nargs > 3:
        print "Usage: python mc.py [initial_state [goal_state]]"
    elif nargs == 3:
        main(initial=eval(sys.argv[1]), goal=eval(sys.argv[2]))
    elif nargs == 2:
        main(initial=eval(sys.argv[1]))
    else:
        main()
