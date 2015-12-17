from pyglet.gl import *
from ctypes import *
from program import Program
from camera import Camera
#from glm import *
#from glm.functions import *
from euclid import *
import math
import time


class GameObject:
    def __init__(self, *args, **kwargs):
        self.program = Program()
        self.vao = GLuint(0)
        self.vbo = GLuint(0)
        self.ebo = GLuint(0)

        # Create Vertex Array Object
        glGenVertexArrays(1, self.vao)

        # Create a Vertex Buffer Object
        glGenBuffers(1, self.vbo)

        # Create an element array
        glGenBuffers(1, self.ebo)

        # use the vao
        glBindVertexArray(self.vao)

        width = float(100)
        height = float(100)
        r = 1.0
        g = 0.0
        b = 0.0

        # self.vertices = [
        #     0.0, 0.0, r, g, b, # Top-left
        #     0.0 + width, 0.0, r, g, b, # Top-right
        #     0.0 + width, 0.0 + height, r, g, b, # Bottom-right
        #     0.0, 0.0 + height, r, g, b  # Bottom-left
        # ]
        # self.vertices_gl = (GLfloat * len(self.vertices))(*self.vertices)

        self.vertices = [
            0.0, 0.0,
            0.0 + width, 0.0,
            0.0 + width, 0.0 + height,
            0.0, 0.0 + height,
        ]
        self.vertices_gl = (GLfloat * len(self.vertices))(*self.vertices)

        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, sizeof(self.vertices_gl), self.vertices_gl, GL_STATIC_DRAW)

        self.elements = [
            0, 1, 2,
            2, 3, 0
        ]
        self.elements_gl = (GLuint * len(self.elements))(*self.elements)

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(self.elements_gl), self.elements_gl, GL_STATIC_DRAW)

        self.program.compile_shader_from_string(
            """
            layout (location = 0) in vec2 position;
            uniform mat4 proj;
            uniform mat4 view;
            uniform mat4 model;

            void main()
            {
                gl_Position = proj * view * model * vec4(position, 0.0, 1.0);
            }
            """, 'vertex')

        self.program.compile_shader_from_string(
            """
            void main()
            {
                gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);
            }
            """, 'fragment')

        if not self.program.link():
            return

        if not self.program.validate():
            return

        self.program.bind()

        # Specify the layout of the vertex data
        position_attribute = glGetAttribLocation(self.program.get_handle(), "position")
        if position_attribute > -1:
            glEnableVertexAttribArray(position_attribute)
            glVertexAttribPointer(position_attribute, 2, GL_FLOAT, GL_FALSE, 2 * sizeof(GLfloat), 0)

        # color_attribute = glGetAttribLocation(self.program.get_handle(), "color")
        # if color_attribute > -1:
        #     glEnableVertexAttribArray(color_attribute)
        #     glVertexAttribPointer(color_attribute, 3, GL_FLOAT, GL_FALSE, 5 * sizeof(GLfloat), 2 * sizeof(GLfloat))

        # stop the vao
        glBindVertexArray(0)

    # def new_look_at(self, eye, at, up):
    #     z = (eye - at).normalized()
    #     x = up.cross(z).normalized()
    #     y = z.cross(x)
    #
    #     m = Matrix4.new_rotate_triple_axis(x, y, z)
    #     m.d, m.h, m.l = -x.dot(eye), -y.dot(eye), -z.dot(eye)
    #     return m

    def ortho(self, left, right, bottom, top, znear, zfar):
        mtx = Matrix4().identity()
        mtx.a = 2.0 / (right - left)
        mtx.f = 2.0 / (top - bottom)
        mtx.k = - 2.0 / (zfar - znear)
        mtx.m = - (right + left) / (right - left)
        mtx.n = - (top + bottom) / (top - bottom)
        mtx.o = - (zfar + znear) / (zfar - znear)
        mtx.transpose()
        return mtx

    def render(self):
        self.program.bind()

        # view_matrix = mat4x4.identity()
        # proj_matrix = mat4x4.identity()
        # model_matrix = mat4x4.identity()
        # mvp_matrix = mat4x4.identity()

        # eye, at, up
        # eye = Vector3(2.5, 2.5, 2.0)
        # at = Vector3(0.0, 0.0, 0.0)
        # up = Vector3(0.0, 0.0, 1.0)
        # #view_matrix = Matrix4.new_look_at(eye, at, up)
        # view_matrix = self.new_look_at(eye, at, up)
        # view_matrix = view_matrix.transposed()
        # view_ctype = (GLfloat * len(view_matrix))(*view_matrix)
        #
        # view_location = glGetUniformLocation(self.program.get_handle(), "view")
        # if view_location > -1:
        #     glUniformMatrix4fv(view_location, 1, GL_FALSE, view_ctype)
        #
        # proj = Matrix4.new_perspective(45.0, 800.0 / 600.0, 1.0, 10.0)
        # proj = proj.transposed()
        # proj_ctype = (GLfloat * len(proj))(*proj)
        # proj_location = glGetUniformLocation(self.program.get_handle(), "proj")
        # if proj_location > -1:
        #     glUniformMatrix4fv(proj_location, 1, GL_FALSE, proj_ctype)
        #
        # model = Matrix4().identity()
        # model = model.transposed()
        # model_ctype = (GLfloat * len(model))(*model)
        # model_location = glGetUniformLocation(self.program.get_handle(), "model")
        # if model_location > -1:
        #     glUniformMatrix4fv(model_location, 1, GL_FALSE, model_ctype)

        eye = Vector3(0.0, 0.0, 1.02)
        at = Vector3(0.0, 0.0, 0.0)
        up = Vector3(0.0, 1.0, 0.0)
        view = Matrix4.new_look_at(eye, at, up)
        view = view[:]
        view_ctype = (GLfloat * len(view))(*view)
        view_location = glGetUniformLocation(self.program.get_handle(), "view")
        if view_location > -1:
            glUniformMatrix4fv(view_location, 1, GL_FALSE, view_ctype)

        #proj = Matrix4.new_perspective(math.radians(45.0), 800.0 / 600.0, 1.0, 10.0)
        proj = self.ortho(0.0, 800.0, 600.0, 0.0, 10.0, -10.0)
        proj = proj[:]
        proj_ctype = (GLfloat * len(proj))(*proj)
        proj_location = glGetUniformLocation(self.program.get_handle(), "proj")
        if proj_location > -1:
            glUniformMatrix4fv(proj_location, 1, GL_FALSE, proj_ctype)

        #model = Quaternion.new_rotate_axis(time.clock() * math.pi, Vector3(0, 0, 1))
        model = Matrix4().identity()
        #model = model.get_matrix()
        model = model[:]
        model_ctype = (GLfloat * len(model))(*model)
        model_location = glGetUniformLocation(self.program.get_handle(), "model")
        if model_location > -1:
            glUniformMatrix4fv(model_location, 1, GL_FALSE, model_ctype)

        # bind vao for use
        glBindVertexArray(self.vao)
        # Draw a rectangle from the 2 triangles using 6 indices
        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0)
        # stop the vao
        glBindVertexArray(0)
