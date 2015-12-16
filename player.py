from block import Block, BLOCK_SIZE
import pyglet


class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = BLOCK_SIZE * 10
        self.height = BLOCK_SIZE * 10
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
                    myrow.append(Block(col_index, row_index))
            self.blocks.append(myrow)

    def render(self):
        for row in self.blocks:
            for block in row:
                block.render()
