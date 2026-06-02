from typing import Tuple
from cell import Cell 
import os
import random

number_of_mine = 4
number_of_flarg = number_of_mine
is_game_over = False
is_game_lose = False
game_board_size = 9
cover_cell = "■"
empty_cell = "·"
flag = "⚑"
wrong_flag = "Ø"
end_game_mine = "☼"
mine_explose = "X"

def main():

    global is_game_over

    mine_inserted = False
    clear = lambda: os.system('clear')
    cell_list = create_square_game_board(game_board_size)    
    game_board = connect_cell(cell_list)
    drow_game_board(game_board) 
    while not is_game_over:
        cell_selected_x = input("Inset a number to select x, or insert a char 'F' to start insert flarg: ")
        if cell_selected_x == "F":
            cell_selected_x = input("Insert number to select x flarg position: ")
            flag_the_cell = True
            cell_selected_y = input("Insert number to select y flarg position: ")
        else:   
            flag_the_cell = False
            cell_selected_y = input("Insert a number to select y position: ")
        selected_cell = int(cell_selected_y), int(cell_selected_x)
        if not mine_inserted: 
            game_board = distribuite_mine(game_board, number_of_mine, selected_cell)
            mine_inserted = True
        game_board = handle_selection(game_board, selected_cell, flag_the_cell)
            
        clear()
        drow_game_board(game_board)
        check_for_gameover(game_board)
  
    if is_game_lose:
        clear()
        print("You lose!")
    else:
        clear()
        print("You win!")

    drow_game_board(game_board, is_game_over) 

def check_for_gameover(game_board: list[Cell]):
    
    global is_game_over, is_game_lose

    cell_explored = 0
    for cell in game_board:
        if cell.state[0] == 1 and cell.value == 1:
            is_game_over = True
            is_game_lose = True
        if cell.state[0] == 1 or cell.state[0] == 2 or cell.state[0] == 0 and cell.flagged:
            cell_explored += 1
   
    if cell_explored >= (game_board_size * game_board_size) - number_of_mine:
        is_game_lose = False
        is_game_over = True

def handle_selection(game_board: list[Cell], selected_cell: Tuple, flag_the_cell: bool) -> list[Cell]:
    
    for cell in game_board:
       if cell.position == selected_cell:
            if flag_the_cell:
                cell.flagged = True
                return game_board
 
            if cell.value == 1:
                cell.state = (1, 0)
            else:   
                recursive_search_for_mine(cell)
            break                 

    return game_board

def recursive_search_for_mine(cell: Cell):

    if cell.state[0] != 0:
        return

    if cell.value == 0:
        if cell.numberOfMineInNeighboars() == 0:
            cell.state = (1, 0)
            for neighbor in cell.neighbors:
                recursive_search_for_mine(neighbor)
        else:
            worning_mine: int = cell.numberOfMineInNeighboars()
            cell.state = (2, worning_mine)

def drow_game_board(game_board: list[Cell], is_game_over: bool = False):

    drow = "  "

    for i in range(0,game_board_size):
        drow += f" {i + 1}"
    drow += "\n"
    for cell in game_board:
        if cell.position[1] == 1:
            drow += f"{cell.position[0]} " 
        if cell.state[0] == 0 and is_game_over == False:
            if not cell.flagged:
                drow += f" {cover_cell}"
            else:
                drow += f" {flag}"
        elif cell.state[0] == 0 and cell.value == 1 and is_game_over == True:
            drow += f" {end_game_mine}"
        elif cell.state[0] == 1:
            if cell.value == 1:
                drow += f" {mine_explose}"
            else:
                drow += f" {empty_cell}"
        elif cell.state[0] == 2:
           drow += f" {cell.state[1]}" 

        if cell.position[1] == game_board_size:
            drow += "\n"

    print(drow)

def distribuite_mine(game_board: list[Cell], mine_number: int, first_selection: Tuple) -> list[Cell] :
    
    valid_cells = [cell for cell in game_board if cell.position != first_selection]
    
    mined_cells = random.sample(valid_cells, mine_number)
    
    for cell in mined_cells:
        cell.value = 1
        
    return game_board

def create_square_game_board(game_board_size: int) -> list[Cell]:

    if game_board_size < 3:
        raise IndexError("The game board is too small, must be at least 3")
        
    number_of_total_cell = game_board_size * game_board_size
    cell_list = []

    while len(cell_list) != number_of_total_cell:
        if len(cell_list) < 1:
            starting_cell = Cell(position = (1, 1), neighbors = [], node_type = 0, value = 0)
            cell_list.append(starting_cell)
        else:
            last_cell = cell_list[-1]

            if last_cell.position[1] != game_board_size:
                if last_cell.position[1] == game_board_size -1: 

                    if last_cell.position[0] in (1, game_board_size): 
                        cell_list.append(Cell(position = (last_cell.position[0], last_cell.position[1] + 1), node_type = 0, neighbors = [], value = 0))
                    else:
                        cell_list.append(Cell(position = (last_cell.position[0], last_cell.position[1] + 1), node_type = 1, neighbors = [], value = 0))
                else:

                    if last_cell.position[0] in (1, game_board_size): 
                        cell_list.append(Cell(position = (last_cell.position[0], last_cell.position[1] + 1), node_type = 1, neighbors = [], value = 0))
                    else:
                        cell_list.append(Cell(position = (last_cell.position[0], last_cell.position[1] + 1), node_type = 2, neighbors = [], value = 0))
            else:
                if last_cell.position[0] != game_board_size -1:
                    cell_list.append(Cell(position = (last_cell.position[0] + 1, 1), node_type = 1, neighbors = [], value = 0))
                else:
                    cell_list.append(Cell(position = (last_cell.position[0] + 1, 1), node_type = 0, neighbors = [], value = 0))
    return cell_list

def connect_cell(cell_list: list[Cell]) -> list[Cell]:
    for cell in cell_list:
    
        if cell.node_type == 0:
            cell_to_find: list[Tuple] = []

            if cell.position[0] == 1 and cell.position[1] == 1:
                cell_to_find.append((cell.position[0] + 1, cell.position[1]))
                cell_to_find.append((cell.position[0], cell.position[1] + 1))
                cell_to_find.append((cell.position[0] + 1, cell.position[1] + 1))
            if cell.position[0] == game_board_size and cell.position[1] == game_board_size:
                cell_to_find.append((cell.position[0] - 1, cell.position[1]))
                cell_to_find.append((cell.position[0], cell.position[1] - 1))
                cell_to_find.append((cell.position[0] - 1, cell.position[1] - 1))
            if cell.position[0] == 1 and cell.position[1] == game_board_size:
                cell_to_find.append((cell.position[0], cell.position[1] - 1))
                cell_to_find.append((cell.position[0] + 1, cell.position[1]))
                cell_to_find.append((cell.position[0] + 1, cell.position[1] - 1))
            if cell.position[0] == game_board_size and cell.position[1] == 1:
                cell_to_find.append((cell.position[0] - 1, cell.position[1]))
                cell_to_find.append((cell.position[0], cell.position[1] + 1))
                cell_to_find.append((cell.position[0] - 1, cell.position[1] + 1))
                
            cell.neighbors.extend(cell_to_search(cell_list, cell_to_find))
            cell_to_find.clear()

        elif cell.node_type == 1:
            cell_to_find: list[Tuple] = []
            if cell.position[0] == 1:
                cell_to_find.extend([
                    (cell.position[0], cell.position[1] - 1),
                    (cell.position[0], cell.position[1] + 1),
                    (cell.position[0] + 1, cell.position[1] - 1),
                    (cell.position[0] + 1, cell.position[1]),
                    (cell.position[0] + 1, cell.position[1] + 1)
                ])
            elif cell.position[0] == game_board_size:
                cell_to_find.extend([
                    (cell.position[0], cell.position[1] - 1),
                    (cell.position[0], cell.position[1] + 1),
                    (cell.position[0] - 1, cell.position[1] - 1),
                    (cell.position[0] - 1, cell.position[1]),
                    (cell.position[0] - 1, cell.position[1] + 1)
                ])
            elif cell.position[1] == 1:
                 cell_to_find.extend([
                    (cell.position[0] - 1, cell.position[1]),
                    (cell.position[0] + 1, cell.position[1]),
                    (cell.position[0] - 1, cell.position[1] + 1),
                    (cell.position[0], cell.position[1] + 1),
                    (cell.position[0] + 1, cell.position[1] + 1)
                ])
            elif cell.position[1] == game_board_size:
                cell_to_find.extend([
                    (cell.position[0] - 1, cell.position[1]),
                    (cell.position[0] + 1, cell.position[1]),
                    (cell.position[0] - 1, cell.position[1] - 1),
                    (cell.position[0], cell.position[1] - 1),
                    (cell.position[0] + 1, cell.position[1] - 1)
                ])

            cell.neighbors.extend(cell_to_search(cell_list, cell_to_find))
            cell_to_find.clear()

        else:
            cell_to_find: list[Tuple] = []
            cell_to_find.extend([
                    (cell.position[0] - 1, cell.position[1]),
                    (cell.position[0] + 1, cell.position[1]),
                    (cell.position[0], cell.position[1] - 1),
                    (cell.position[0], cell.position[1] + 1),
                    (cell.position[0] + 1, cell.position[1] + 1),
                    (cell.position[0] - 1, cell.position[1] - 1),
                    (cell.position[0] + 1, cell.position[1] - 1),
                    (cell.position[0] - 1, cell.position[1] + 1)
                ])

            cell.neighbors.extend(cell_to_search(cell_list, cell_to_find))
            cell_to_find.clear()

    return cell_list

def cell_to_search(cell_list: list[Cell], positions_to_find: list[Tuple]) -> list[Cell]:

    cells_found = [cell for cell in cell_list if cell.position in positions_to_find]
         
    return cells_found      

main()
