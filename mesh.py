from gameobject import GameObject
from buffers import VertexBuffer, IndexBuffer
from pyglet.gl import *
from ctypes import *


class Mesh(GameObject):

    def __init__(self):
        self.vao = 0
        self.vbuf = 0
        self.ibuf = 0
        self.vertices = []
        self.normals = []
        self.indices = []
        self.uvs = []
        GameObject.__init__(self)

    def set_data(self, *args, **kwargs):
        self.vertices = kwargs.get('verts', [])
        self.normals = kwargs.get('normals', [])
        self.indices = kwargs.get('indices', [])
        self.uvs = kwargs.get('uvs', [])

        # create a vao
        glGenVertexArrays(1, self.vao)
        # use it
        glBindVertexArray(self.vao)
        # create a vertexbuffer
        self.vbuf = VertexBuffer(self.vertices)
        self.vbuf.set_attribute(0, 2, GL_FLOAT, GL_FALSE, 0, 0)
        # create an indexbuffer
        self.ibuf = IndexBuffer(self.indices)
        # stop the vao
        glBindVertexArray(0)

    def render(self):
        GameObject.render(self)
        # bind vao for use
        glBindVertexArray(self.vao)
        # Draw a rectangle from the 2 triangles using 6 indices
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, 0)
        # stop the vao
        glBindVertexArray(0)

