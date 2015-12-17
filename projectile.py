from mesh import Mesh


class Projectile(Mesh):

    def __init__(self):
        Mesh.__init__(self)

    def render(self):
        Mesh.render(self)
        self.matrix.translate(0.0, -3.0, 0.0)
