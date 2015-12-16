from euclid import *


class Camera:

    def __init__(self):
        self.projection = Matrix4().identity()
        self.view = Matrix4().identity()
        self.ortho(0.0, 800.0, 600.0, 0.0, 10.0, -10.0)
        self.look_at(
            Vector3(0.0, 0.0, 1.0),
            Vector3(0.0, 0.0, 0.0),
            Vector3(0.0, 1.0, 0.0),
        )

    def ortho(self, left, right, bottom, top, znear, zfar):
        self.projection = Matrix4().identity()
        self.projection.a = 2.0 / (right - left)
        self.projection.f = 2.0 / (top - bottom)
        self.projection.k = - 2.0 / (zfar - znear)
        self.projection.m = - (right + left) / (right - left)
        self.projection.n = - (top + bottom) / (top - bottom)
        self.projection.o = - (zfar + znear) / (zfar - znear)
        self.projection.transpose()

    def look_at(self, eye, at, up):
        self.view = Matrix4.new_look_at(eye, at, up)
