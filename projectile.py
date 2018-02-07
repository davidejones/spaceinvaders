from mesh import Mesh
from utils import shape_to_mesh
from euclid3 import Vector2
from config import *


class Projectile(Mesh):

    def __init__(self, dir=Vector2(0, -1)):
        Mesh.__init__(self, BLOCK_SIZE * 2, BLOCK_SIZE * 4)
        self.shape = [
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
        ]
        v, i = shape_to_mesh(self.shape, 0xFFFFFF)
        self.set_data(vertices=v, indices=i)
        self.direction = dir
        self.speed = 250.0
        self.in_use = False

    def update(self, dt):
        super().update(dt)
        if self.in_use:
            self.translate(0, (self.speed * dt) * self.direction.y, 0)
            if self.position.y < 0:
                self.in_use = False
