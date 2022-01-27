# Author: Joseph Capobianco
# Date: 11/22/21
# Description: Python implementation of graph traversal algorithm

def solve_puzzle(Board, Source, Destination):
    """
    Function takes in three inputs: Board, Source and Destination. The Board
    parameter will represent a board as a 2D adjency matrix where empty spots on
    the board are represented with '-' and blocked spots on the board are represented
    with '#'. The goal is to find the shortest path from the Source parameter location
    on the board to the destination location on the board. You can move left, right, up
    or down and must return as an output the path as a list of tuples of the locations.
    If it is not possible to get to the destination, the function will return a None
    object. 
    """
    length_of_board = len(Board)
    length_of_rows = len(Board[0])
    around_destination = {}

    up_destination = (Destination[0] - 1, Destination[1])
    down_destination = (Destination[0] + 1, Destination[1])
    left_destination = (Destination[0], Destination[1] - 1)
    right_destination = (Destination[0], Destination[1] + 1)

    if up_destination[0] < 0 or up_destination == '#':
        around_destination['up'] = False
    if down_destination[0] == length_of_board or down_destination == '#':
        around_destination['down'] = False
    if left_destination[1] < 0 or left_destination == '#':
        around_destination['left'] = False
    if right_destination[1] >= length_of_rows or right_destination == '#':
        around_destination['right'] = False

    if len(around_destination) == 4:
        return None
    else:
        directions = []
        queue = []
        visited = []
        node_path = {}
        queue.append(Source)
        visited.append(Source)
        while len(queue) != 0:
            value = queue.pop(0) 
            x = value[0]
            y = value[1]
            if (x, y) == Destination:
                tuple_list = []
                tuple_list.append(Destination)
                while tuple_list[0] != Source:
                    for keys, values in node_path.items():
                        if keys == tuple_list[0]:
                            tuple_list.insert(0, values)
    
                for elements in range(1, len(tuple_list)):
                    if tuple_list[elements][0] > tuple_list[elements - 1][0] and tuple_list[elements][1] == tuple_list[elements-1][1]:
                        directions.append('D')
                    elif tuple_list[elements][0] < tuple_list[elements-1][0] and tuple_list[elements][1] == tuple_list[elements-1][1]:
                        directions.append('U')
                    elif tuple_list[elements][1] > tuple_list[elements-1][1] and tuple_list[elements][0] == tuple_list[elements-1][0]:
                        directions.append('R')
                    else:
                        directions.append('L')
                return tuple_list, directions
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if 0 <= x2 < length_of_board and 0 <= y2 < length_of_rows and Board[x2][y2] != '#' and (x2, y2) not in visited:
                    queue.append((x2, y2))
                    visited.append((x2, y2))
                    node_path[(x2, y2)] = value
            


if __name__ == '__main__':
    aboard = [
        ['-', '-', '-', '-', '-'],
        ['-', '-', '#', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['#', '-', '#', '#', '-'],
        ]
    asource = (0,0)
    adestination = (3,4)
    print(solve_puzzle(aboard, asource, adestination))