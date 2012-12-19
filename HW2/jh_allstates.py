"""Example of two water jugs problem for use with AIMA code"""

#! /usr/bin/python

from search import *

class JH(Problem):

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
        STATES:
        left_bank = (missionary_left, hannibal_left)
        right_bank = (missionary_right, hannibal_right)
        boat = (missionary_boat, hannibal_boat)

        initial states => left_bank=(3,3) | right_bank=(0,0) | boat=(0,0)
        goal => left_bank=(0,0) | boat=(0,0) | right_bank = (3,3)
    '''

    def __init__(self, intial=((1,1,1),(1,1,1),(0,0,0),(0,0,0)), goal=((0,0,0),(0,0,0),(0,0,0),(0,0,0))):
        self.initial = intial
        self.goal = goal
        self.boat_location = 'L'
        self.step=0;

    def __repr__(self):
        """returns a string representing the object"""
        return "WJ(%s,%s)" % (self.initial, self.goal)

    def goal_test(self, state):
        """returns true if state is a goal state"""
        
        return (state[0][0]==0 and state[0][1]==0 and state[0][2]==0 and state[1][0]==0
                and state[1][1]==0 and state[1][2]==0 and state[2][0]==0 and state[2][1]==0 and state[2][2]==0
                and state[3][0]==0 and state[3][1]==0 and state[3][2]==0)
        

    def successor(self, ((W1, W2, W3), (H1, H2, H3), (BW1, BW2, BW3),(BH1, BH2, BH3))):
        """returns a list of successors to state"""
        successors = []
        """ (C0, C1) = self.capacities"""

        '''
            boat states:
            H - H>M OR H=M
            M - M>H
            HH - H>=M+1
            MM - M>H+2
            HM - H=M
        '''
        self.step=self.step+1
        if self.boat_location=='L':
            '''
                boat has reached left bank and is departing towards right bank
            '''
            self.boat_location='R'
            
            if (H1+H2+H3)==3:
                if (W1+W2+W3)>1:
                    
                    #print "%s stepped into L1" % (self.step)
                    #print "(%s,%s,%s,%s,%s,%s)" % (LM,LH,RM,RH,BM,BH)

                    if W1==W2:
                        successors.append(('load the boat with a wife 1 and wife 2',((0, 0, W3), (H1, H2, H3), (1, 1 ,0), (0, 0, 0))))
                    if W1==W3:
                        successors.append(('load the boat with a wife 1 and wife 3',((0, W2, 0), (H1, H2, H3), (1, 0 ,1), (0, 0, 0))))
                    if W2==W3:
                        successors.append(('load the boat with a wife 2 and wife 3',((W1, 0, 0), (H1, H2, H3), (0, 1 ,1), (0, 0, 0))))
                if (W1+W2+W3)==1:
                    if W1==1:
                        successors.append(('load the boat with a husband 2 and husband 3',((W1, W2, W3), (H1, 0, 0), (0, 0 ,0), (0, 1, 1))))
                    if W2==1:
                        successors.append(('load the boat with a husband 1 and husband 3',((W1, W2, W3), (0, H2, 0), (0, 0 ,0), (1, 0, 1))))
                    if W3==1:
                        successors.append(('load the boat with a husband 1 and husband 2',((W1, W2, W3), (0, 0, H3), (0, 0 ,0), (1, 1, 0))))
            elif (H1+H2+H3)==0:
                if W1==1 and W2==1:
                    successors.append(('load the boat with a wife 1 and wife 2',((0, 0, W3), (H1, H2, H3), (1, 1 ,0), (0, 0, 0))))
                if W1==1 and W3==1:
                    successors.append(('load the boat with a wife 1 and wife 3',((0, W2, 0), (H1, H2, H3), (1, 0 ,1), (0, 0, 0))))
                if W2==1 and W3==1:
                    successors.append(('load the boat with a wife 2 and wife 3',((W1, 0, 0), (H1, H2, H3), (0, 1 ,1), (0, 0, 0))))
            elif ((W1+H1)==0) and (H1+H2+H3)>0 and (H1+H2+H3)<3:
                successors.append(('load the boat with a husband 2 and husband 3',((W1, W2, W3), (H1, 0, 0), (0, 0 ,0), (0, 1, 1))))
            elif ((W2+H2)==0 and (H1+H2+H3)>0 and (H1+H2+H3)<3):
               successors.append(('load the boat with a husband 1 and husband 3',((W1, W2, W3), (0, H2, 0), (0, 0 ,0), (1, 0, 1))))
            elif ((W3+H3)==0) and (H1+H2+H3)>0 and (H1+H2+H3)<3:
                successors.append(('load the boat with a husband 1 and husband 2',((W1, W2, W3), (0, 0, H3), (0, 0 ,0), (1, 1, 0))))
        else:
            '''
                boat has reached right bank
            '''
            self.boat_location='L'

            if (H1+H2+H3)==0:
                if (W1+W2+W3)==0 :
                    #goal state
                    successors.append(('all done',((0,0,0),(0,0,0),(0,0,0),(0,0,0))))
                if (W1+W2+W3)> 0 :
                    if W1==0:
                        successors.append(('load the boat with a wife 1',((1, W2, W3), (H1, H2, H3), (1, 0 ,0), (0, 0,0))))
                    if W2==0:
                        successors.append(('load the boat with a wife 2',((W1,1, W3), (H1, H2, H3), (0, 1 ,0), (0,0,0))))
                    if W3==0:
                        successors.append(('load the boat with a wife 3',((W1, W2, 1), (H1, H2, H3), (0, 0 ,1), (0,0,0))))
            elif (H1+H2+H3)==3:
                if W1==0:
                    successors.append(('load the boat with a wife 1',((1, W2, W3), (H1, H2, H3), (1, 0 ,0), (0, 0,0))))
                if W2==0:
                    successors.append(('load the boat with a wife 2',((W1,1, W3), (H1, H2, H3), (0, 1 ,0), (0,0,0))))
                if W3==0:
                    successors.append(('load the boat with a wife 3',((W1, W2, 1), (H1, H2, H3), (0, 0 ,1), (0,0,0))))
            
            elif (W1+W2+W3)==1 and (H1+H2+H3)==1:
                if (W1==0 and H1==0):
                    successors.append(('load the boat with a husband 1 and wife 1',((1, W2, W3), (1, H2, H3), (1, 0 ,0), (1,0,0))))
                if (W2==0 and H2==0):
                    successors.append(('load the boat with a husband 2 and wife 2',((W1, 1, W3), (H1, 1, H3), (0, 1 ,0), (0,1,0))))
                if (W3==0 and H3==0):
                    successors.append(('load the boat with a husband 3 and wife 3',((W1, W2, 1), (H1, H2, 1), (0, 0 ,1), (0,0,1))))          
        
        return successors

def main():
    searchers = [breadth_first_tree_search, breadth_first_graph_search, depth_first_graph_search,
                 iterative_deepening_search, depth_limited_search]
    #searchers = [depth_first_graph_search]
    problems = [JH(((1,1,1),(1,1,1),(0,0,0),(0,0,0)),((0,0,0),(0,0,0),(0,0,0),(0,0,0)))]
    for p in problems:
        for s in searchers:
            print "Solution to %s found by %s" % (p, s.__name__)
            path = s(p).path()
            path.reverse()
            print path
            print
    print "SUMMARY: successors/goal tests/states generated/solution"
    compare_searchers(problems=problems,
                      header=['SEARCHER', 'GOAL:((0,0,0),(0,0,0),(0,0,0),(0,0,0))'],
                      searchers=[breadth_first_tree_search,
                                 breadth_first_graph_search, depth_first_graph_search,
                                 iterative_deepening_search, depth_limited_search])
                      #searchers = [depth_first_graph_search])
'''searchers=[breadth_first_tree_search,
breadth_first_graph_search, depth_first_graph_search,
iterative_deepening_search, depth_limited_search])'''
                      

# if called from the command line, call main()
if __name__ == "__main__":
    main()
