from typing import Tuple
from cell import Cell 
import os

game_board_size = 9
cover_cell = "■"
empty_cell = "·"
flag = "⚑"
wrong_flag = "Ø"
end_game_mine = "☼"
mine_explose = "X"

def main():

    clear = lambda: os.system('clear')
    is_game_over = False
    cell_list = create_square_game_board(game_board_size, 0)    
    game_board = connect_cell(cell_list)
    drow_game_board(game_board)

    while not is_game_over:
        cell_selected_x = input("Select a cell with a coordinate x: ") 
        cell_selected_y = input("Select a cell with a coordinate y: ") 
        game_board = handle_selection(game_board, (int(cell_selected_x), int(cell_selected_y)))
            
        clear()
        drow_game_board(game_board)
        
def handle_selection(game_board: list[Cell], selected_cell: Tuple) -> list[Cell]:
    for cell in game_board:
        
        if cell.position[0] == selected_cell[0] and cell.position[1] == selected_cell[1]:

            print(cell.value)
            if cell.state == 0:
                if cell.value == 0:
                    cell.state = 1
                    return game_board

    return game_board

def drow_game_board(game_board: list[Cell]):
    drow = "  "
    for i in range(0,game_board_size):
        drow += f" {i + 1}"
    drow += "\n"
    for cell in game_board:
        if cell.position[1] == 1:
            drow += f"{cell.position[0]} " 
        if cell.state == 0:
            drow += f" {cover_cell}"
        elif cell.state == 1:
            drow += f" {empty_cell}"
        if cell.position[1] == game_board_size:
            drow += "\n"

    print(drow)

def create_square_game_board(game_board_size: int, number_of_mine: int) -> list[Cell]:

    if game_board_size < 3:
        raise IndexError("The game board is too small, must be at least 3")
        

    if number_of_mine > (game_board_size * game_board_size):
        raise IndexError("Must be exist at least 1 free cell in the game board")
    
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
