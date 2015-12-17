from euclid import *


class GameObject:
    def __init__(self):
        self.parent = None
        self.matrix = Matrix4().identity()

    def render(self):
        pass