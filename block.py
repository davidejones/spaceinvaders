from mesh import Mesh

BLOCK_SIZE = 5


class Block(Mesh):

    def __init__(self, x=0, y=0):
         Mesh.__init__(self)
         self.x = x
         self.y = y
         v = [
             self.x, self.y,
             self.x + BLOCK_SIZE, self.y,
             self.x + BLOCK_SIZE, self.y + BLOCK_SIZE,
             self.x, self.y,
             self.x, self.y + BLOCK_SIZE,
             self.x + BLOCK_SIZE, self.y + BLOCK_SIZE,
         ]
         i = [
            0, 1, 2,
            2, 3, 0
         ]
         self.set_data(vertices=v, indices=i)