from pyglet.gl import *
from ctypes import sizeof


class VertexBuffer:

    def __init__(self, data):
        self.id = GLuint(0)
        self.data_gl = (GLfloat * len(data))(*data)
        self.__create_buffer()

    def __create_buffer(self):
        # generate the vert buffer
        glGenBuffers(1, self.id)
        # use the buffer
        glBindBuffer(GL_ARRAY_BUFFER, self.id)
        # allocate memory in the buffer and populate with data
        glBufferData(GL_ARRAY_BUFFER, len(self.data_gl)*4, self.data_gl, GL_STATIC_DRAW)
        # tell opengl how data is packed in buffer
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, 0)
        # enable vertexattrib array at position 0 so shader can read it
        glEnableVertexAttribArray(0)

    def get_id(self):
        return self.id

    def set_attribute(self, index, size, type, normalized, stride, pointer):
        glVertexAttribPointer(index, size, type, normalized, stride, pointer)
        glEnableVertexAttribArray(index)


class IndexBuffer:

    def __init__(self, data, size):
        self.id = GLuint(0)
        self.data_gl = (GLfloat * len(data))(*data)
        self.__create_buffer()

    def __create_buffer(self):
        # generate the index buffer
        glGenBuffers(1, self.id)
        # use the buffer
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.id)
        # allocate memory in the buffer and populate with data
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, len(self.data_gl)*4, self.data_gl, GL_STATIC_DRAW)

    def get_id(self):
        return self.id


class FrameBuffer:

    def __init__(self):
        pass
