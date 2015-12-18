from gameobject import GameObject
from block import Block, BLOCK_SIZE
import pyglet


class Player(GameObject):

    def __init__(self):
        GameObject.__init__(self)
        self.x = 0
        self.y = 0
        self.width = BLOCK_SIZE * 10
        self.height = BLOCK_SIZE * 10
        self.color = 0xFFFFFF
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
        self.blocks = []
        for row_index, row in enumerate(self.shape):
            myrow = []
            for col_index, col in enumerate(row):
                if col == 1:
                    myrow.append(Block(self, self.color, col_index * BLOCK_SIZE, row_index * BLOCK_SIZE))
            self.blocks.append(myrow)

    def render(self):
        for row in self.blocks:
            for block in row:
                block.render()

    def move_left(self):
        self.translate(-10.0, 0.0, 0.0)
        #self.matrix.translate(-10.0, 0, 0.0)

    def move_right(self):
        self.translate(10.0, 0.0, 0.0)
        #self.matrix.translate(10.0, 0, 0.0)


    def fire(self):
        sound = pyglet.resource.media('shoot.wav', streaming=False)
        sound.play()
