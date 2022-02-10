#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : Name: HIMANSHU HIMANSHU UserName: hhimansh
#
# Based on skeleton code in CSCI B551, Fall 2021.

import sys

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Count total # of pichus on house_map
def count_pichus(house_map):
    return sum([ row.count('p') for row in house_map ] )

# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    return "\n".join(["".join(row) for row in house_map])

# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    return house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]

# Getting location of all pichus in the house_map
def get_agent_loc(house_map):
    return [(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"]

# Passing two list and deleting common elements(i.e. location of pichus in current state and successor state) from agent_loc_successors
def delete_common_pichu_locations(agent_loc_successors, agent_locs):
    return[agent_loc_successor for agent_loc_successor in agent_loc_successors if agent_loc_successor not in agent_locs]

# Get list of successors of given house_map state
def successors(house_map):
    
    # Finding location of pichus in current house_map(state)
    agent_locs = get_agent_loc(house_map)

    # Placing pichus in all the empty cells and making list for it from different cells
    successors_states = [add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) if house_map[r][c] == '.']
    
    # Making list of all successor state which are valid(where pichus cannot see each other), for now setting it empty
    valid_succesors_state = []
    
    # Iterating through each succesor state to find which is valid(where pichus cannot see each other)
    for successors_state in successors_states:

        # Get position of pichus in the succesor state
        agent_loc_successors = get_agent_loc(successors_state)

        # Deleting all the pichus position which were present in previous state
        agent_loc_successors = delete_common_pichu_locations(agent_loc_successors, agent_locs) [0]
        
        # Iterating through each coordinate of pichu from previous to check if new position of pichu in the given succesor state conflict with old coordinates
        for agent_loc in agent_locs:

            # Finding difference in rows and columns of new position of pichu and old position of pichus 
            row_diff = agent_loc_successors[0] - agent_loc[0]
            col_diff = agent_loc_successors[1] - agent_loc[1]

            # Checking Conditions if pichus are in exact adjacent cell for which three conditions persist(same row - adjacent column for which condition is row difference is 0 and absolute value of column difference is 1, same column - adjacent row for which condition is absolute value of row difference is 1 and column difference is 0, or diagonally adjacent for which condition is absolute value of row difference and column difference is 1 )
            # If the above mention condition is true then new location is not a valid one hence breaking the loop and not entering it to valid states map 
            if ((row_diff == 0 and abs(col_diff) == 1) or (col_diff ==0 and abs(row_diff) == 1) or (abs(row_diff) == abs(col_diff) == 1)):
                break
            
            # Checking Condition when the pichus are in same row but not adjacent columns(row difference is 0 and absolute column difference is greater than 1 ), So there can be wall between them or not checking that
            elif row_diff == 0:
                
                # Taking max and min column Index of pichu from both sates to find map between them
                maxPichuIndex = max(agent_loc_successors[1], agent_loc[1])
                minPichuIndex = min(agent_loc_successors[1], agent_loc[1])

                # Checking if there is a wall(represented by X) between both pichus so, slicing the row between both the pichus
                #If there is no wall pichus then new location is not a valid one hence breaking the loop and not entering it to valid states map
                if not('X' in house_map[agent_loc_successors[0]][minPichuIndex+1 : maxPichuIndex] or '@' in house_map[agent_loc_successors[0]][minPichuIndex+1 : maxPichuIndex]):
                     break
            
            # Checking Condition when the pichus are in same column but not adjacent rows( absolute row difference is greater than 1 and column difference is 0 ), So there can be wall between them or not checking that
            elif col_diff == 0:
                
                # Taking max and min row Index of pichu from both sates to find map between them
                maxPichuIndex = max(agent_loc_successors[0], agent_loc[0])
                minPichuIndex = min(agent_loc_successors[0], agent_loc[0])

                # Initialising Empty list to store the map(same column and different row cells) between pichus
                map_of_pichu_row = []

                # Looping through particular column between particular row indexes
                for i in range(minPichuIndex+1, maxPichuIndex):
                    
                    # Appending each row data into the list
                    map_of_pichu_row.append(house_map[i][agent_loc_successors[1]])
                
                # Checking if there is a wall(represented by X) between both pichus(data is in the list)
                #If there is no wall pichus then new location is not a valid one hence breaking the loop and not entering it to valid states map
                if not('X' in map_of_pichu_row or '@' in map_of_pichu_row):
                    break
            
            # Checking Condition when the pichus are present diagonally but not adjacent diagonal cell( absolute row difference and absolute column difference is same but is greater than 1), So there can be wall between them or not checking that
            elif abs(col_diff) == abs(row_diff):
                
                # Initialising Empty list to store the map(diagonal cells data) between pichus
                map_of_pichus_diagonal = []
                
                # Finding row step difference in diagonal(in which row direction we are moving)
                row_step = row_diff//abs(row_diff)
                
                # Finding col step difference in diagonal(in which column direction we are moving)
                col_step = col_diff//abs(col_diff)
                
                # Initialising curr_state_row(Row)Index to move in diagonal
                curr_state_row = agent_loc[0] + row_step

                # Initialising curr_state_col (Column) Index to move in diagonal
                curr_state_col = agent_loc[1] + col_step

                # Iterating through diagonal till reach the succesor state cell
                while curr_state_row != agent_loc_successors[0] and curr_state_col != agent_loc_successors[1]:
                    
                    # Appending the data into the list
                    map_of_pichus_diagonal.append(house_map[curr_state_row][curr_state_col])
                   
                   # Changing current row by step value for row
                    curr_state_row = curr_state_row + row_step

                    # Changing current step by step value for column
                    curr_state_col = curr_state_col + col_step
                
                # Checking if there is a wall(represented by X) between both pichus(data is in the list)
                #If there is no wall pichus then new location is not a valid one hence breaking the loop and not entering it to valid states map
                if not('X' in map_of_pichus_diagonal or '@' in map_of_pichus_diagonal):
                    break

        else:
            # Appending valid map to list
            valid_succesors_state.append(successors_state)
        
    # Returning valid successor list
    return valid_succesors_state
# check if house_map is a goal state
def is_goal(house_map, k):
    return count_pichus(house_map) == k 

# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_house_map, success), where:
# - new_house_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_house_map,k):

    # Initializing fringe inserting initial map 
    fringe = [initial_house_map]
    
    # iterating through fringe untill we find a solution or finge is empty
    while len(fringe) > 0:

        # Finding Successor states for a given state by putting nect pichu where it is possible to put in the map
        for new_house_map in successors( fringe.pop() ):
            
            # Checking if the succesor state found is solution
            if is_goal(new_house_map,k):
                
                # Returning solution state house map and true
                return(new_house_map,True)
            
            # Otherwise appending successor state to the fringe
            fringe.append(new_house_map)
    
    # Returning Empty house map and False if no solution is present
    return([], False)
# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map,k)
    print ("Here's what we found:")
    print (printable_house_map(solution[0]) if solution[1] else "False")


