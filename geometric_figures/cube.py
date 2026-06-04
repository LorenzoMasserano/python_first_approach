from point import Point
import os

class Cube:

    def __init__(self, base: int, height: int, z: int):
        
        if not base == height and height == z:
            raise IndexError("Base, height and z must be identical")

        self.base = base
        self.height = height
        self.z = z 

        self.cube: list[Point] = self.compose_cube()
        
    def compose_cube(self) -> list[Point]:
        
        cube: list[Point] = []

        for b in range(0,self.base):
            for h in range(0,self.height):
                for i in range(0, self.z):
                    cube.append(
                        Point(
                            coordinate= (b, h, i),
                            connections= [])
                    )
        return cube
    
    def drow_cube(self):
        
        cube_drow = ""
        
        canvas_width = (self.base * 2) + self.z + 10
        canvas_height = self.height + self.z + 5

        canvas = [[" " for _ in range(canvas_width)] for _ in range(canvas_height)]
        
        origin_x = 3
        origin_y = 20

        for point in self.cube:

            x, y, z = point.coordinate

            screen_x = origin_x + (x*2) + z
            screen_y = origin_y - y - z

            limits_hit = 0
            if x == 0 or x == self.base - 1: limits_hit += 1
            if y == 0 or y == self.height - 1: limits_hit += 1
            if z == 0 or z == self.z - 1: limits_hit += 1
            
            if limits_hit >= 2:
                if 0 <= screen_x < canvas_width and 0 <= screen_y < canvas_height:
                        canvas[screen_y][screen_x] = "■"

        for row in canvas:
            cube_drow += "".join(row) + "\n"
        
        clear = lambda: os.system('clear')
        clear()
        print(cube_drow)
