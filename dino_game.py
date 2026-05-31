import os
import time
import sys
import select
import tty
import termios
import random

word_resolution = (100,30)

initial_cactus_speed = 1 
current_creature_count_down = initial_cactus_speed
initial_dino_jump_distance = 4 
initial_dino_jump_speed = 10
current_dino_jump_speed_progress = initial_dino_jump_speed
current_dino_jump_progress = 0
is_dino_falling = False
creature_spown_rate = 5
creature_spown_current_count_down = creature_spown_rate
initial_crouched_duration = 60
current_crouched_count_down = 0
is_dino_crouched = False
game_score = 0
score_string = ""
pigeon_position_list = []
cactus_position_list = [(word_resolution[0] -1)]
dino_position = 0

is_game_over = True
clear = lambda: os.system('clear')
sys.stdout.write("\033[?25l")
clear()
move_cursor_top_left = lambda: sys.stdout.write("\033[H")


def main():
    
    global is_game_over, current_dino_jump_progress, current_dino_jump_speed_progress, is_dino_falling, is_dino_crouched, current_crouched_count_down, creature_spown_current_count_down, current_creature_count_down, game_score, score_string

    dino_char = '↱'
    dino_char_crouched = '¬'
    floor_char = '_'
    cactus_char = 'I'
    pigeon_char = '_;'   
    
    input("Press a button to start!")
    is_game_over = False
   
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())   
    
    try:
        while not is_game_over:
            print(f"{score_string}\n\n\n")
            move_cursor_top_left()

            check_key_pressed()
            
            generate_word(dino_char, dino_char_crouched, cactus_char, floor_char, pigeon_char)

            spawn_cactus_algoritm()
            
            if current_creature_count_down > 0:
                current_creature_count_down -= 1
            else:
                current_creature_count_down = 10
                for index,_ in enumerate(cactus_position_list):
                    cactus_position_list[index] -= 1
                for index,_ in enumerate(pigeon_position_list):
                    pigeon_position_list[index] -= 1
            
            if current_crouched_count_down > 0 and current_crouched_count_down < initial_crouched_duration: 
                        current_crouched_count_down += 1
            elif current_crouched_count_down >= initial_crouched_duration:
                        current_crouched_count_down = 0
                        is_dino_crouched = False

            game_score += 0.01
            score_string = f"Score: {int(game_score)}"
            time.sleep(0.005) 
    finally:
        sys.stdout.write("\033[?25h")
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)    
        
def check_key_pressed():

    global dino_position, word_resolution, current_dino_jump_progress, is_dino_crouched, current_crouched_count_down, is_game_over
   
    key = ''
    if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
        key = sys.stdin.read(1)

    if key == 'a' and dino_position > 0:
        dino_position -= 1
    elif key == 'd' and dino_position < word_resolution[0] - 1:
        dino_position += 1
    elif key == 'w' and current_dino_jump_progress == 0 and not is_dino_crouched:
        current_dino_jump_progress = 1
    elif key == 's' and not is_dino_crouched and current_dino_jump_progress == 0:
        current_crouched_count_down += 1
        is_dino_crouched = True
    elif key == 'q':
        is_game_over = True

def generate_word(dino_char, dino_char_crouched, cactus_char, floor_char, pigeon_char):
   
    global pigeon_position_list, word_resolution, current_dino_jump_progress, dino_position, cactus_position_list, is_dino_crouched

    for i in range(word_resolution[1]):

        ground = ""
        for j in range(word_resolution[0]):
            
            if i == (word_resolution[1] - 2) and j in pigeon_position_list:
                
                ground += pigeon_char

            elif current_dino_jump_progress > 0 and i + current_dino_jump_progress == word_resolution[1] and j == dino_position:
                ground += dino_char
                process_jump()

            elif i == (word_resolution[1] - 1):
                   
                if j == dino_position and current_dino_jump_progress < 1 and not is_dino_crouched:
                    ground += dino_char
                elif j == dino_position and is_dino_crouched:
                    ground += dino_char_crouched

                elif len(cactus_position_list) > 0 and j -1 in cactus_position_list:
                    
                    ground += cactus_char
                else:
                    ground += floor_char

            else:
                ground += " "
        print(ground)
    remove_useles_creature()
    check_game_over()


def process_jump():

    global is_dino_falling, current_dino_jump_speed_progress, current_dino_jump_progress

    if not is_dino_falling:

        if current_dino_jump_speed_progress == 0:
            current_dino_jump_progress += 1
            current_dino_jump_speed_progress = initial_dino_jump_speed
        else:
            current_dino_jump_speed_progress -= 1
            
        if current_dino_jump_progress == initial_dino_jump_distance:
            is_dino_falling = True
    else:
        
        if current_dino_jump_speed_progress == 0:
            current_dino_jump_progress -= 1
            current_dino_jump_speed_progress = initial_dino_jump_speed
        else:
            current_dino_jump_speed_progress -= 1
        if current_dino_jump_progress == 0:
            is_dino_falling = False


def spawn_cactus_algoritm():
    
    global pigeon_position_list, cactus_position_list, creature_spown_current_count_down, creature_spown_rate 

    if creature_spown_current_count_down < 0:
        
        choice = random.choice([True, False])
        if choice:
            pigeon_position_list.append(word_resolution[0] -1)
            creature_spown_current_count_down = creature_spown_rate
        else:
            cactus_position_list.append(word_resolution[0] -1)
            creature_spown_current_count_down = creature_spown_rate
    else:
        creature_spown_current_count_down -= 0.04

def check_game_over():
    
    global dino_position, cactus_position_list, current_dino_jump_progress, is_dino_crouched, pigeon_position_list

    if dino_position in cactus_position_list and current_dino_jump_progress == 0:
        start_game_over()
    if dino_position in pigeon_position_list and not is_dino_crouched:
        start_game_over()

def remove_useles_creature():

    global cactus_position_list, pigeon_position_list
    
    def remove_0(position):
        return position > -1

    if len(cactus_position_list) > 0:
        cactus_position_list = list(filter(remove_0, cactus_position_list))

    if len(pigeon_position_list) > 0:
        pigeon_position_list = list(filter(remove_0, pigeon_position_list))

def start_game_over():
    
    global is_game_over, game_score
 
    clear()
    print("Game Over")
    print(f"Score: {int(game_score)}")
    is_game_over = True
    return 
    
main()
