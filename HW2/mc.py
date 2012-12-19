"""Example of two water jugs problem for use with AIMA code"""

#! /usr/bin/python

from search import *

class MC(Problem):

    """
    Three missionaries and three cannibals are on the left bank of a river. A boat is
    available which will hold two people, and which can be navigated by any combination
    of missionaries and cannibals involving one or two people. If the missionaries on
    either bank of the river are outnumbered at any time by cannibals, the cannibals
    will indulge in their anthropophagic tendencies and do away with the missionaries
    who are outnumbered. Find a schedule of crossings that will permit all the missionaries
    and cannibals to cross the river from the left bank to the right bank safely.
    """

    '''
        the state is represented by an array of six values
                    (LM, LH, RM, RH, BM, BH)
        LM=number of missionaries on the left bank
        LH=number of hannibals on the left bank
        RM=number of missionaries on the right bank
        RH=number of hannibals on the right bank
        BM=number of missionaries on the boat
        BH=number of hannibals on the boat

        
       the initial state is when all missionaries and hannibals are on the left bank and boat is empty.
                (3,3,0,0,0,0)

        the final state is when all missionaries and hannibals are on the right bank and boat is empty.
                (0,0,3,3,0,0)
    '''

    def __init__(self, intial=(3,3,0,0,0,0), goal=(0,0,3,3,0,0)):
        self.initial = intial
        self.goal = goal
        self.boat_location = 'L'
        self.step=0;

    def __repr__(self):
        """returns a string representing the object"""
        return "WJ(%s,%s)" % (self.initial, self.goal)

    def goal_test(self, state):
        """returns true if state is a goal state"""
        
        return (state[0]==0 and state[1]==0 and state[2]==3 and state[3]==3
                and state[4]==0 and state[5]==0)
        

    def successor(self, (LM, LH, RM, RH, BM, BH)):
        """returns a list of successors to state"""
        successors = []
       
        self.step=self.step+1
        if self.boat_location=='L':
            '''
                boat has reached left bank and is departing towards right bank
            '''
            self.boat_location='R'
            
            if LM==LH or LM>LH:
                if (BM+BH)==0:
                    #print "%s stepped into L1" % (self.step)
                    #print "(%s,%s,%s,%s,%s,%s)" % (LM,LH,RM,RH,BM,BH)
                    successors.append(('load the boat with a missionary and a hannibal',(LM-1,LH-1,RM,RH,1,1)))
                    
                elif LM==LH:
                    #print "%s stepped into L2" % (self.step)
                    #print "(%s,%s,%s,%s,%s,%s)" % (LM,LH,RM,RH,BM,BH)
                    successors.append((' load a hannibal in the boat ',(LM,LH-1,RM,RH,BM,BH+1)))
                    """left_bank[1]--
                    boat[1]++"""
                else:
                    #print "%s stepped into L3" % (self.step)
                    #print "(%s,%s,%s,%s,%s,%s)" % (LM,LH,RM,RH,BM,BH)
                    successors.append((' load a missionary in the boat ',(LM-1,LH,RM,RH,BM+1,BH)))
                    """left_bank[0]--
                    boat[0]++"""
                
        else:
            '''
                boat has reached right bank
            '''
            self.boat_location='L'

            '''
                decide on unloading
            '''
            if RM==0:
                #print "%s stepped into R1" % (self.step)
                #print "(%s,%s,%s,%s,%s,%s)" % (LM,LH,RM,RH,BM,BH)
                successors.append(('drop a missionary',(LM,LH,RM+1,RH,0,BH)))
            elif ((RM>0) and (RM==RH)):
                #print "%s stepped into R2" % (self.step)
                #print "(%s,%s,%s,%s,%s,%s)" % (LM,LH,RM,RH,BM,BH)
                if RM==2 and RH==2:
                    successors.append(('drop last missionary and hannibal pair',(LM,LH,RM+1,RH+1,BM-1,BH-1)))
                else:
                    successors.append(('drop a missionary',(LM,LH,RM+1,RH,0,BH)))
            elif RM>RH:
                #print "%s stepped into R3" % (self.step)
                #print "(%s,%s,%s,%s,%s,%s)" % (LM,LH,RM,RH,BM,BH)
                successors.append(('drop a hannibal',(LM,LH,RM,RH+1,BM,BH-1)))

            if RM==3:
                #print "%s stepped into exit state" % (self.step)
                #print "(%s,%s,%s,%s,%s,%s)" % (LM,LH,RM,RH,BM,BH)
                successors.append(('drop last hannibal',(LM,LH,RM,RH+1,BM,BH-1)))
                
        
        return successors
    
       

def main():
    searchers = [breadth_first_tree_search, breadth_first_graph_search, depth_first_graph_search,
                 iterative_deepening_search, depth_limited_search]
    problems = [MC((3,3,0,0,0,0),(0,0,3,3,0,0))]
    for p in problems:
        for s in searchers:
            print "Solution to %s found by %s" % (p, s.__name__)
            path = s(p).path()
            path.reverse()
            print path
            print
    print "SUMMARY: successors/goal tests/states generated/solution"
    compare_searchers(problems=problems,
            header=['SEARCHER', 'GOAL:(0,0,0,0,3,3)'],
            searchers=[breadth_first_tree_search,
                      breadth_first_graph_search, depth_first_graph_search,
                      iterative_deepening_search, depth_limited_search])

# if called from the command line, call main()
if __name__ == "__main__":
    main()
