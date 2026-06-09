from core.shape import Shape
from core.point import Point

class Pyramid(Shape):
    def __init__(self, base: int, height: int, z: int, only_border: bool = False):
    
        self.only_border = only_border

        super().__init__(base= base, height= height, z= z)
     
    def compose_shape(self) -> list[Point]:

        shape: list[Point] = []
        offset_x = self.base / 2
        offset_y = self.height / 2
        offset_z = self.z / 2

        for h in range(0,self.height):

            shrink_factor = h / (self.height -1) if self.height > 1 else 0

            margin_b = int(round((self.base // 2) * shrink_factor))
            margin_z = int(round((self.z // 2) * shrink_factor))

            min_b, max_b = margin_b, self.base - 1 - margin_b
            min_z, max_z = margin_z, self.z - 1 - margin_z

            for b in range(min_b, max_b + 1):
                for z in range(min_z, max_z + 1):

                    is_inside_pyramid = (min_b <= b <= max_b) and (
                        min_z <= z <= max_z
                    )   

                    if not is_inside_pyramid:
                        continue

                    is_border = (
                        h == 0 and b == min_b
                        or h == 0 and b == max_b
                        or h == 0 and z == min_z
                        or h == 0 and z == max_z
                        or b == max_b and z == min_z    
                        or b == min_b and z == max_z    
                        or b == max_b and z == max_z    
                        or b == min_b and z == min_z    

                    )

                    if self.only_border and not is_border:
                        continue
                    
                    centered_x = float(b - offset_x)
                    centered_h = float(h - offset_y)
                    centered_z = float(z - offset_z)

                    shape.append(
                        Point(
                            coordinate=(centered_x, centered_h, centered_z),
                            connections=[]
                        )
                    )
                    
        return shape
