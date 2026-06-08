from core.point import Point

class Cube:

    def __init__(self, base: int, height: int, z: int, only_border: bool = False):
        
        if not base == height and height == z:
            raise IndexError("Base, height and z must be identical")

        self.base = base
        self.height = height
        self.z = z 
        self.only_border = only_border

        self.cube: list[Point] = self.compose_cube()
        
    def compose_cube(self) -> list[Point]:
        
        cube: list[Point] = []
        offset_x = self.base / 2
        offset_y = self.height / 2
        offset_z = self.z / 2

        for b in range(0,self.base):
            for h in range(0,self.height):
                for i in range(0, self.z):
                    
                    limits_hit = sum([
                        b == 0 or b == self.base - 1,
                        h == 0 or h == self.height - 1,
                        i == 0 or i == self.z - 1
                    ]) 

                    if self.only_border and limits_hit < 2:
                        continue

                    centered_x = float(b - offset_x)
                    centered_y = float(h - offset_y)
                    centered_z = float(i - offset_z)

                    cube.append(
                        Point(
                            coordinate=(centered_x, centered_y, centered_z),
                            connections=[]
                        )
                    )        
        return cube

    def drow_cube(self):
        
        cube_drow = ""
        
        canvas_width = (self.base * 4) + self.z + 20
        canvas_height = (self.height * 2) + self.z + 10

        canvas = [[" " for _ in range(canvas_width)] for _ in range(canvas_height)]
        
        origin_x = canvas_width // 2
        origin_y = canvas_height // 2

        for point in self.cube:

            x, y, z = point.coordinate

            screen_x = int(round(origin_x + (x*2) + z))
            screen_y = int(round(origin_y - y - z))

            if 0 <= screen_x < canvas_width and 0 <= screen_y < canvas_height:
                        canvas[int(screen_y)][int(screen_x)] = "■"

        for row in canvas:
            cube_drow += "".join(row) + "\n"
        
        print(cube_drow)
