from mesh import Mesh
from utils import shape_to_mesh
import pyglet
from config import *


class Player(Mesh):

    def __init__(self):
        Mesh.__init__(self)
        self.shape = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        v, i = shape_to_mesh(self.shape, 0xFF0000)
        self.set_data(vertices=v, indices=i)
        self.width = BLOCK_SIZE * 10
        self.height = BLOCK_SIZE * 10

    def move_left(self):
        self.translate(-10.0, 0.0, 0.0)

    def move_right(self):
        self.translate(10.0, 0.0, 0.0)

    def fire(self):
        sound = pyglet.resource.media('assets/shoot.wav', streaming=False)
        sound.play()

    def update(self, dt):
        self.bounds.set_bounds(self.position.x, self.position.x + 40, self.position.y, self.position.y + 40)
