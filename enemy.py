from mesh import Mesh
from utils import shape_to_mesh
from config import *


class Enemy(Mesh):

    def __init__(self, parent=None):
        Mesh.__init__(self, BLOCK_SIZE * 10, BLOCK_SIZE * 10)
        self.parent = parent
        self.shape = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        ]
        v, i = shape_to_mesh(self.shape, 0x1EBDDD)
        self.set_data(vertices=v, indices=i)

    def move_left(self):
        self.matrix.translate(-10.0, 0, 0.0)

    def move_right(self):
        self.matrix.translate(10.0, 0, 0.0)

    def fire(self):
        print('firing')

    def update(self, dt):
        super().update(dt)
