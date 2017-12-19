from mesh import Mesh
from utils import shape_to_mesh
from config import *


class Enemy(Mesh):

    def __init__(self, parent=None, shape=None, color=0x1EBDDD):
        Mesh.__init__(self, BLOCK_SIZE * 10, BLOCK_SIZE * 10)
        self.parent = parent
        self.shape = shape
        v, i = shape_to_mesh(self.shape, color)
        self.set_data(vertices=v, indices=i)

    def move_left(self):
        self.matrix.translate(-10.0, 0, 0.0)

    def move_right(self):
        self.matrix.translate(10.0, 0, 0.0)

    def fire(self):
        print('firing')

    def update(self, dt):
        super().update(dt)
