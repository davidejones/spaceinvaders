from mesh import Mesh
from utils import shape_to_mesh
import pyglet
from euclid3 import Vector2
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
        self.direction = Vector2(0, 0)
        self.move_amount = 10.0

    def move_left(self):
        self.direction.x = -1

    def move_right(self):
        self.direction.x = 1

    def move_end(self):
        self.direction.x = 0

    def move_mouse(self, x, y):
        # their x and y is from bottom left
        # my x and y is from top left
        increment_x = x - self.position.x
        if x > self.position.x:
            if self.position.x + self.width + increment_x >= WIDTH:
                self.Translate(WIDTH - self.width, self.position.y, self.position.z)
            else:
                self.translate(increment_x, 0.0, 0.0)
        elif x < self.position.x:
            if self.position.x + increment_x < 0:
                self.Translate(0, self.position.y, self.position.z)
            else:
                self.translate(increment_x, 0.0, 0.0)

    def fire(self):
        sound = pyglet.resource.media('assets/shoot.wav', streaming=False)
        sound.play()

    def update(self, dt):
        if self.direction.x == 1:
            if self.position.x + self.width + self.move_amount >= WIDTH:
                self.Translate(WIDTH - self.width, self.position.y, self.position.z)
            else:
                self.translate(self.move_amount, 0.0, 0.0)
        elif self.direction.x == -1:
            if self.position.x + (self.move_amount * -1) < 0:
                self.Translate(0, self.position.y, self.position.z)
            else:
                self.translate((self.move_amount * -1), 0.0, 0.0)
        self.bounds.set_bounds(self.position.x, self.position.x + 40, self.position.y, self.position.y + 40)