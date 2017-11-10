from euclid3 import *
from bounds import Bounds


class GameObject:
    def __init__(self, width, height):
        self.parent = None
        self.children = []
        self.matrix = Matrix4().identity()
        self.position = Vector3(0.0, 0.0, 0.0)
        self.width = width
        self.height = height
        self.bounds = Bounds(0, self.width, 0, self.height)

    def render(self):
        if self.bounds:
            self.bounds.render()

    def update(self, dt):
        if self.bounds:
            if self.parent:
                x, y, z = self.parent.position.x + self.position.x, self.parent.position.y + self.position.y, self.parent.position.z + self.position.z
                self.bounds.set_bounds(x, x + self.width, y, y + self.height)
            else:
                x, y, z = self.position.x, self.position.y, self.position.z
                self.bounds.set_bounds(x, x + self.width, y, y + self.height)

    def Translate(self, x, y, z):
        """ new translation """
        self.position.x = x
        self.position.y = y
        self.position.z = z
        self.matrix = Matrix4.new_translate(x, y, z)
        self.compose()

    def translate(self, x, y, z):
        """ incremental translation """
        self.position.x += x
        self.position.y += y
        self.position.z += z
        self.matrix.translate(x, y, z)
        self.compose()

    def compose(self):
        self.matrix = Matrix4.new_translate(self.position.x, self.position.y, self.position.z)
        if self.parent:
            self.matrix = self.parent.matrix * self.matrix

        for child_index, child in enumerate(self.children):
            child.compose()
