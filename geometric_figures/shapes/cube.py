from core.point import Point
from core.shape import Shape

class Cube(Shape):

    def __init__(self, base: int, height: int, z: int, only_border: bool = False):

        if not base == height and height == z:
            raise IndexError("Base, height and z must be identical")

        self.only_border = only_border

        super().__init__(base= base, height= height, z=z)
        
    def compose_shape(self) -> list[Point]:
        
        shape: list[Point] = []
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

                    shape.append(
                        Point(
                            coordinate=(centered_x, centered_y, centered_z),
                            connections=[]
                        )
                    )        
        return shape

