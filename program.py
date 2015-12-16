from pyglet.gl import *
from ctypes import *


class Program:

    def __init__(self):
        self.handle = glCreateProgram()
        self.shader_handle = GLuint(0)

    def get_handle(self):
        return self.handle

    def compile_shader_from_string(self, s, type):
        if type == 'vertex':
            self.shader_handle = glCreateShader(GL_VERTEX_SHADER)
        elif type == 'fragment':
            self.shader_handle = glCreateShader(GL_FRAGMENT_SHADER)

        buff = create_string_buffer(s)
        c_text = cast(pointer(pointer(buff)), POINTER(POINTER(GLchar)))
        glShaderSource(self.shader_handle, 1, c_text, None)
        glCompileShader(self.shader_handle)

        status = c_int()
        glGetShaderiv(self.shader_handle, GL_COMPILE_STATUS, status)
        if status.value == 0:
            length = c_int()
            glGetShaderiv(self.shader_handle, GL_INFO_LOG_LENGTH, length)
            log = c_buffer(length.value)
            glGetShaderInfoLog(self.shader_handle, len(log), None, log)
            print(log.value)
        else:
            glAttachShader(self.handle, self.shader_handle)

    def bind_frag_data_location(self, location, name):
        glBindFragDataLocation(self.handle, location, name)

    def bind_attrib_location(self, location, name):
        glBindAttribLocation(self.handle, location, name)

    def link(self):
        glLinkProgram(self.handle)
        status = GLint(0)
        glGetProgramiv(self.handle, GL_LINK_STATUS, byref(status))
        if status.value == 0:
            print('something went wrong linking')
            return False
        else:
            return True

    def bind(self):
        glUseProgram(self.handle)

    def unbind(self):
        glUseProgram(0)

    def validate(self):
        status = GLint(0)
        glValidateProgram(self.handle)
        glGetProgramiv(self.handle, GL_VALIDATE_STATUS, byref(status))
        if status.value == 0:
            print('something went wrong')
            return False
        else:
            return True
