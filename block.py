from mesh import Mesh

BLOCK_SIZE = 4


class Block(Mesh):

    def __init__(self, parent, color=0xFF0000, x=0, y=0):
        Mesh.__init__(self)
        self.parent = parent
        self.position.x = x
        self.position.y = y
        #self.matrix.translate(x, y, 0.0)
        self.color = color
        r, g, b = self.toRgb(self.color)
        v = [
            0.0, 0.0, r, g, b,
            0.0 + BLOCK_SIZE, 0.0, r, g, b,
            0.0 + BLOCK_SIZE, 0.0 + BLOCK_SIZE, r, g, b,
            0.0, 0.0 + BLOCK_SIZE, r, g, b,
        ]
        i = [
            0, 1, 2,
            2, 3, 0
        ]
        self.set_data(vertices=v, indices=i)
