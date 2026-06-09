from core.point import Point

class Shape():
    def __init__(self, base: int, height: int, z:int):

        self.base: int = base
        self.height: int = height
        self.z: int = z

        self.shape = self.compose_shape()

    def compose_shape(self) -> list[Point]:
        return []

    def drow(self):
        
        cube_drow = ""
        
        canvas_width = (self.base * 4) + self.z + 20
        canvas_height = (self.height * 2) + self.z + 10

        canvas = [[" " for _ in range(canvas_width)] for _ in range(canvas_height)]
        
        origin_x = canvas_width // 2
        origin_y = canvas_height // 2

        for point in self.shape:

            x, y, z = point.coordinate

            screen_x = int(round(origin_x + (x*2) + z))
            screen_y = int(round(origin_y - y - z))

            if 0 <= screen_x < canvas_width and 0 <= screen_y < canvas_height:
                        canvas[int(screen_y)][int(screen_x)] = "■"

        for row in canvas:
            cube_drow += "".join(row) + "\n"
        
        print(cube_drow)
