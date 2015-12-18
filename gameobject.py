from euclid import *


class GameObject:
    def __init__(self):
        self.parent = None
        self.matrix = Matrix4().identity()
        self.position = Vector3(0.0, 0.0, 0.0)

    def render(self):
        pass

    def Translate(self, x, y, z):
        """ new translation """
        self.position.x = x
        self.position.y = y
        self.position.z = z
        self.matrix = Matrix4.new_translate(x, y, z)

    def translate(self, x, y, z):
        """ incremental translation """
        self.position.x += x
        self.position.y += y
        self.position.z += z
        self.matrix.translate(x, y, z)

    def toRgb(self, RGBint):
        Blue = RGBint & 255
        Green = (RGBint >> 8) & 255
        Red = (RGBint >> 16) & 255
        return (1.0/255)*Red, (1.0/255)*Green, (1.0/255)*Blue
