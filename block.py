from mesh import Mesh

BLOCK_SIZE = 4


class Block(Mesh):

    def __init__(self, parent, color=0xFF0000, x=0, y=0):
         Mesh.__init__(self)
         self.parent = parent
         self.matrix.translate(x, y, 0.0)
         v = [
            0.0, 0.0,
            0.0 + BLOCK_SIZE, 0.0,
            0.0 + BLOCK_SIZE, 0.0 + BLOCK_SIZE,
            0.0, 0.0 + BLOCK_SIZE,
         ]
         i = [
            0, 1, 2,
            2, 3, 0
         ]
         r = 0.0
         g = 0.0
         b = 1.0
         c = [
             r, g, b,
             r, g, b,
             r, g, b,
             r, g, b,
         ]
         self.set_data(vertices=v, indices=i, colors=c)
