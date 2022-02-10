# Hide-and-Seek-AI (Modified N Queen) #

This project was done as a part of CSCI-B-551 Elements of Artificial Intelligence Coursework under Prof. Dr. David Crandall.

## Command to run the program ##

python3 arrange_pichus.py [name of map] [number of queens/pichus]

## Abstractions Techniques that can be used ##

Another Abstraction technique I would have used could be the Breadth-First Search. But the problem with the Breadth-First Search is it can be slow for this kind of solution as it iterates to every node on a given depth and the branching factor of the problem is high.

## Abstraction Technique Used ##
I have used the Depth First Search abstraction technique.

## Overview of solution ##
The problem given is a modified n queen with obstacles in it and a non-square board. So, I implemented n queen with some changes so that obstacles can be taken care of. Initially, I developed an n queen solution then made changes to it which are described below.

I have implemented Depth First Search Abstraction in the solution. The code of the search function is the same as it was given in the skeleton. I have just changed the code of the successor_state function. So, in the search function, I have taken a fringe a set it to the initial input map, then I am running a loop on the fringe until I found a solution or fringe becomes empty, this is the case when there is no solution. If there is no solution I am returning an empty set and False. In the loop, I am popping the last element from the fringe and is passing that element into the successor_state function. In successor_state function, firstly I am finding the positions of queens/pichus in the current state. Then I am adding one queens/pichus to all empty positions represented by "." and saving each of them as a separate state. After that, I am checking which of the following states are valid. For checking the valid states I am iterating through each successor state and finding the location of all queens/pichus in that successor state, for that I am deleting coordinates of the current state from the successor state and then comparing the remaining coordinate to coordinates in the current state. For comparing, I am calculating the row difference between both pichu's rows and the column difference between both pichu's columns to find if queens/pichus are in the same row, same column, or diagonal. If the new Pichu is not present in the same row, column, or diagonal as the old present queens/pichus then it is a valid state and adding it to the valid state list. If new Pichu is in the same row like any other Pichu then I am checking whether the column difference is one, if it is then that state is not valid, if not I further check for obstacles between them by slicing a particular row between two indexes of queens/pichus, if there is an obstacle then it's valid otherwise not. The same thing is done if queens/pichus are in the same column I checked the row difference if its one then that state is not valid, if not I further check for obstacles between them by taking all the elements of the column which lies between queens/pichus, if I find an obstacle between then only the state is valid otherwise not. If queens/pichus are present in diagonal and the absolute value of column difference and row difference is one then it's an invalid state, otherwise, I am checking for an obstacle in the diagonal between queens/pichus. For doing so I find the change the row and column in 1 or -1 to generalize my diagonal solution, Then I ran a loop to extract the elements of that particular diagonal if there is an obstacle it's a valid state otherwise not. If according to the above conditions Pichu is in a valid position then I am adding it to the valid state list and returning it.

## Challenges Faced and Solution for it ##
The only main challenge I faced during developing this problem was finding a loop for extracting the diagonal elements for checking diagonal validity. But I have implemented it after brainstorming found the loop conditions for general cases.

## Initial State ##

The initial state for the solution is the input map with the single Pichu placed along with the obstacles.

## Goal State ##
The goal state for the solution is a map with the required k; k = number of queens/pichus to be placed on the map such that they can't see each other.

## Cost Function ##
The cost for every step is the same so there is no cost function in it.

## State Space ##
State-space for the solution are maps with 1,2,3.........k queens/pichus; k = number of queens/pichus to be placed such that queens/pichus can't see each other.

## Succesor Function ##
The successor function for this solution is, appending the current state map with a single queens/pichus on o the empty locations so that the new Pichu cannot see any of the already present Pichu. All such states will be successor states. 

