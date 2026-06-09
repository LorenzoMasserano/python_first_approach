from animations.rotation import start_rotate
from core.point import CoordinateType
from shapes.pyramid import Pyramid
from shapes.cube import Cube

def main():
    animate_cube()

def animate_cube():
    user_choice_border = input("Enter 1 for the side only mode, or 0 to normal mode: ")
    user_choice_speed = input("Enter the rotation speed: ")
    user_choice_axes = input("Enter which axes us to rotate, X, Y or Z, or all 3: ")

    speed = float(user_choice_speed)
    only_border = user_choice_border == "1"
    
    axes_choice = []
    string_splitted = user_choice_axes.split(",")
    for c in string_splitted:
        c = c.rstrip()
        c = c.lower()

        if c == "x":
            axes_choice.append(CoordinateType.X) 
        elif c == "y":
            axes_choice.append(CoordinateType.Y)
        elif c == "z":
            axes_choice.append(CoordinateType.Z)        
            
    axes_choice= set(axes_choice)
    axes_choice= list(axes_choice)
    
    shape_istance = Pyramid(base=15, height=15, z=15,only_border=only_border)
    # shape_istance = Cube(base=15, height=15, z=15,only_border=only_border)
    start_rotate(shape_instance= shape_istance, speed=speed, rotation_axis= axes_choice)

main()  
