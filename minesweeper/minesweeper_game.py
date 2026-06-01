from typing import Tuple
from cell import Cell 

game_board_size = 3

def main():
    cell_list = create_square_game_board(game_board_size, 0)    
    game_board = connect_cell(cell_list)
    

    for cell in game_board:
        
        print(cell.position, f"type: {cell.node_type}")
        for neighbor in cell.neighbors:
            print(neighbor.position)

def create_square_game_board(game_board_size: int, number_of_mine: int) -> list[Cell]:

    if not isinstance(game_board_size, int):
        raise TypeError("The size must be int type")
    
    if game_board_size < 3:
        raise IndexError("The game board is too small, must be at least 3")
        
    if not isinstance(number_of_mine, int):
        raise TypeError("The number of mine must be int type")

    if number_of_mine > (game_board_size * game_board_size):
        raise IndexError("Must be exist at least 1 free cell in the game board")
    
    number_of_total_cell = game_board_size * game_board_size
    cell_list = []

    while len(cell_list) != number_of_total_cell:
        if len(cell_list) < 1:
            starting_cell = Cell(position = (1, 1), neighbors = [], node_type = 0)
            cell_list.append(starting_cell)
        else:
            last_cell = cell_list[-1]

            if last_cell.position[1] != game_board_size:
                if last_cell.position[1] == game_board_size -1: 

                    if last_cell.position[0] in (1, game_board_size): 
                        cell_list.append(Cell(position = (last_cell.position[0], last_cell.position[1] + 1), node_type = 0, neighbors = []))
                    else:
                        cell_list.append(Cell(position = (last_cell.position[0], last_cell.position[1] + 1), node_type = 1, neighbors = []))
                else:

                    if last_cell.position[0] in (1, game_board_size): 
                        cell_list.append(Cell(position = (last_cell.position[0], last_cell.position[1] + 1), node_type = 1, neighbors = []))
                    else:
                        cell_list.append(Cell(position = (last_cell.position[0], last_cell.position[1] + 1), node_type = 2, neighbors = []))
            else:
                if last_cell.position[0] != game_board_size -1:
                    cell_list.append(Cell(position = (last_cell.position[0] + 1, 1), node_type = 1, neighbors = []))
                else:
                    cell_list.append(Cell(position = (last_cell.position[0] + 1, 1), node_type = 0, neighbors = []))
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
