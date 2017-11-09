from euclid3 import *
from bounds import Bounds


class GameObject:
    def __init__(self):
        self.parent = None
        self.children = []
        self.matrix = Matrix4().identity()
        self.position = Vector3(0.0, 0.0, 0.0)
        self.bounds = Bounds(0, 0, 0, 0)
        self.width = 0
        self.height = 0

    def render(self):
        self.bounds.render()

    def update(self, dt):
        pass

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
