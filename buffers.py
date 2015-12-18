from pyglet.gl import *
from ctypes import sizeof


class Buffer:

    def __init__(self):
        self.id = GLuint(0)

    def get_id(self):
        return self.id


class VertexBuffer(Buffer):

    def __init__(self, data):
        Buffer.__init__(self)
        self.data_gl = (GLfloat * len(data))(*data)
        self.__create_buffer()

    def __create_buffer(self):
        # generate the vert buffer
        glGenBuffers(1, self.id)
        # use the buffer
        glBindBuffer(GL_ARRAY_BUFFER, self.id)
        # allocate memory in the buffer and populate with data
        glBufferData(GL_ARRAY_BUFFER, sizeof(self.data_gl), self.data_gl, GL_STATIC_DRAW)
        # tell opengl how data is packed in buffer
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, 0)
        # enable vertexattrib array at position 0 so shader can read it
        glEnableVertexAttribArray(0)

    # def set_attribute(self, handle, index_str, size, type, normalized, stride, pointer):
    #     index = glGetAttribLocation(handle, index_str)
    #     if index > -1:
    #         glEnableVertexAttribArray(index)
    #         glVertexAttribPointer(index, size, type, normalized, stride, pointer)

    def set_attribute(self, index, size, type, normalized, stride, pointer):
        glEnableVertexAttribArray(index)
        glVertexAttribPointer(index, size, type, normalized, stride, pointer)


class IndexBuffer(Buffer):

    def __init__(self, data):
        Buffer.__init__(self)
        self.data_gl = (GLuint * len(data))(*data)
        self.__create_buffer()

    def __create_buffer(self):
        # generate the index buffer
        glGenBuffers(1, self.id)
        # use the buffer
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.id)
        # allocate memory in the buffer and populate with data
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(self.data_gl), self.data_gl, GL_STATIC_DRAW)


class FrameBuffer(Buffer):

    def __init__(self):
        Buffer.__init__(self)

    def __create_buffer(self):
        # generate the frame buffer
        glGenFramebuffers(1, self.id)
        # use frame buffer
        glBindFramebuffer(GL_FRAMEBUFFER, self.id)

    def bind(self):
        glBindFramebuffer(GL_FRAMEBUFFER, self.id)

    def unbind(self):
        glBindFramebuffer(GL_FRAMEBUFFER, self.id)
