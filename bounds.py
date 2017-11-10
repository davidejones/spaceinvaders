from program import Program
from buffers import VertexBuffer, IndexBuffer
from camera import Camera
from pyglet.gl import *
from ctypes import *
from euclid3 import *
from utils import uint_to_rgb
from config import *


class Bounds:

    def __init__(self, left, right, top, bottom):
        self.minX = left
        self.maxX = right
        self.minY = top
        self.maxY = bottom

        self.parent = None
        self.children = []
        self.matrix = Matrix4().identity()
        self.position = Vector3(0.0, 0.0, 0.0)

        self.program = Program()
        self.vao = GLuint(0)
        self.vbuf = None
        self.ibuf = None
        self.vertices = []
        self.normals = []
        self.indices = []
        self.uvs = []
        # we should really be getting the camera not creating a new instance..
        self.camera = Camera(800, 600)
        r, g, b = uint_to_rgb(0x00FF00)
        v = [
            0.0, 0.0, r, g, b,
            right, 0.0, r, g, b,
            right, bottom, r, g, b,
            0.0, bottom, r, g, b,
        ]
        i = [
            0, 1, 2,
            2, 3, 0
        ]
        self.set_data(vertices=v, indices=i)

    def set_bounds(self, left, right, top, bottom):
        self.position.x = left
        self.position.y = top
        self.matrix = Matrix4.new_translate(self.position.x, self.position.y, self.position.z)

    def check_intersect(self, bounds):
        if self.maxX < bounds.minX:
            # a is left of b
            return False
        if self.minX > bounds.maxX:
            # a is right of b
            return False
        if self.maxY < bounds.minY:
            # a is above b
            return False
        if self.minY > bounds.maxY:
            # a is below b
            return False
        # boxes overlap
        return True

    def set_data(self, *args, **kwargs):
        self.vertices = kwargs.get('vertices', [])
        self.normals = kwargs.get('normals', [])
        self.indices = kwargs.get('indices', [])
        self.uvs = kwargs.get('uvs', [])
        self.colors = kwargs.get('colors', [])

        # create a vao
        glGenVertexArrays(1, self.vao)
        # use it
        glBindVertexArray(self.vao)
        # create a vertexbuffer
        if self.vertices:
            self.vbuf = VertexBuffer(self.vertices)
            #self.vbuf.set_attribute(0, 2, GL_FLOAT, GL_FALSE, 2 * sizeof(GLfloat), 0)
            #self.vbuf.set_attribute(1, 2, GL_FLOAT, GL_FALSE, 2, 0)
        # create an indexbuffer
        if self.indices:
            self.ibuf = IndexBuffer(self.indices)

        self.program.compile_shader_from_string(
            b"""
            #version 440
            layout (location = 0) in vec2 position;
            layout (location = 1) in vec3 color;
            uniform mat4 proj;
            uniform mat4 view;
            uniform mat4 model;
            smooth out vec3 theColor;

            void main()
            {
                theColor = color;
                gl_Position = proj * view * model * vec4(position, 0.0, 1.0);
            }
            """, 'vertex')

        self.program.compile_shader_from_string(
            b"""
            #version 440
            smooth in vec3 theColor;
            void main()
            {
                gl_FragColor = vec4(theColor, 1.0);
            }
            """, 'fragment')
        self.program.link()
        self.program.validate()
        self.program.bind()

        #self.vbuf.set_attribute(self.program.get_handle(), "position", 2, GL_FLOAT, GL_FALSE, 2 * sizeof(GLfloat), 0)
        #self.vbuf.set_attribute(self.program.get_handle(), "color", 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), 0)

        # Specify the layout of the vertex data
        position_attribute = glGetAttribLocation(self.program.get_handle(), b"position")
        if position_attribute > -1:
            glEnableVertexAttribArray(position_attribute)
            glVertexAttribPointer(position_attribute, 2, GL_FLOAT, GL_FALSE, 5 * sizeof(GLfloat), 0)

        color_attribute = glGetAttribLocation(self.program.get_handle(), b"color")
        if color_attribute > -1:
            glEnableVertexAttribArray(color_attribute)
            glVertexAttribPointer(color_attribute, 3, GL_FLOAT, GL_FALSE, 5 * sizeof(GLfloat), 2 * sizeof(GLfloat))

        # stop the vao
        glBindVertexArray(0)

    def render(self):
        self.program.bind()

        view_location = glGetUniformLocation(self.program.get_handle(), b"view")
        if view_location > -1:
            v = self.camera.view
            v = v[:]
            v_ctype = (GLfloat * len(v))(*v)
            glUniformMatrix4fv(view_location, 1, GL_FALSE, v_ctype)

        proj_location = glGetUniformLocation(self.program.get_handle(), b"proj")
        if proj_location > -1:
            p = self.camera.projection
            p = p[:]
            p_ctype = (GLfloat * len(p))(*p)
            glUniformMatrix4fv(proj_location, 1, GL_FALSE, p_ctype)

        model_location = glGetUniformLocation(self.program.get_handle(), b"model")
        if model_location > -1:
            self.matrix = Matrix4.new_translate(self.position.x, self.position.y, self.position.z)
            if self.parent:
                m = Matrix4().identity()
                m = self.parent.matrix * self.matrix
                m = m[:]
            else:
                m = self.matrix[:]
            m_ctype = (GLfloat * len(m))(*m)
            glUniformMatrix4fv(model_location, 1, GL_FALSE, m_ctype)

        # bind vao for use
        glBindVertexArray(self.vao)
        # Draw a rectangle from the 2 triangles using 6 indices
        if self.indices:
            glDrawElements(GL_LINE_STRIP, len(self.indices), GL_UNSIGNED_INT, 0)
        elif self.vertices:
            pass #gldrawarray?
        # stop the vao
        glBindVertexArray(0)
