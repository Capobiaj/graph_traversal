#    Python implementation of a graph traversal algorithm

#    Function takes in three inputs: Board, Source and Destination. The Board
#    parameter will represent a board as a 2D adjency matrix where empty spots on
#    the board are represented with '-' and blocked spots on the board are represented
#    with '#'. The goal is to find the shortest path from the Source parameter location
#    on the board to the destination location on the board. You can move left, right, up
#    or down and must return as an output the path as a list of tuples of the locations.
#    If it is not possible to get to the destination, the function will return a None
#    object. 