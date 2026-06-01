from cell import Cell 

game_board_size = 10

def create_game_board(game_board_size: int, number_of_mine: int):

    if not isinstance(game_board_size, int):
        raise TypeError("The size must be int type")
        
    if not isinstance(number_of_mine, int):
        raise TypeError("The number of mine must be int type")

    if number_of_mine > (game_board_size * game_board_size):
        raise IndexError("Must be exist at list 1 free cell in the game board")
    


def main():
    pass

main()
