import sys
import time
import os
import math
import select
from core.point import CoordinateType, Point
from core.shape import Shape

def start_rotate(shape_instance: Shape, speed: float, rotation_axis: list[CoordinateType] = []):

    animate = True
    move_cursor_top_left = lambda: sys.stdout.write("\033[H")
    clear = lambda: os.system('clear')
    rotation_speed = speed / 100

    clear()
    while animate: 
        move_cursor_top_left()
        animate = set_up_key_observer()
        shape_instance.shape = set_up_rotation(shape_instance.shape, rotation_speed, rotation_axis) 
        shape_instance.drow()
        time.sleep(0.05)

def set_up_key_observer() -> bool:
    key = ''
    if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
        key = sys.stdin.read(1)

    if key == "Q":
        return False 

    return True
        
def set_up_rotation(shape: list[Point], angle_step: float, rotation_axis: list[CoordinateType]) -> list[Point]:
   
    cosine_zero = math.cos(angle_step)
    sine_zero = math.sin(angle_step)

    for rotation in rotation_axis: 

        if rotation == CoordinateType.Z:
            
            for point in shape:
                origin_x = point[CoordinateType.X]
                origin_y = point[CoordinateType.Y]
                
                point_x = (origin_x * cosine_zero) - (origin_y * sine_zero)
                point_y = (origin_x * sine_zero) + (origin_y * cosine_zero)

                point[CoordinateType.X] = point_x
                point[CoordinateType.Y] = point_y

        elif rotation == CoordinateType.Y:

            for point in shape:
                
                origin_x = point[CoordinateType.X]
                origin_z = point[CoordinateType.Z]
                
                point_x = (origin_x * cosine_zero) - (origin_z * sine_zero)
                point_z = (origin_x * sine_zero) + (origin_z * cosine_zero)

                point[CoordinateType.X] = point_x
                point[CoordinateType.Z] = point_z

        else:
            
            for point in shape:
                 
                origin_y = point[CoordinateType.Y]
                origin_z = point[CoordinateType.Z]
                
                point_z = (origin_z * cosine_zero) - (origin_y * sine_zero)
                point_y = (origin_z * sine_zero) + (origin_y * cosine_zero)

                point[CoordinateType.Z] = point_z
                point[CoordinateType.Y] = point_y    
               
    return shape
