import pyglet
import ctypes

import pyglet.gl as gl

from shader import Shader

COVERAGE = 500

vertex_positions = [
	 COVERAGE, 100,  COVERAGE,
	 COVERAGE, 100, -COVERAGE,
	-COVERAGE, 100, -COVERAGE,
	-COVERAGE, 100,  COVERAGE,
]

tex_coords = [
	0, 0, 1, 0, 1, 1, 0, 1,
]

indices = [
	0, 1, 2, 0, 2, 3,
]

class Clouds:
	def __init__(self, path):
		# create shader

		self.shader = Shader("shaders/clouds/vert.glsl", "shaders/clouds/frag.glsl")
		self.mvp_location = self.shader.find_uniform(b"matrix")
		self.time_location = self.shader.find_uniform(b"time")
		self.sampler_location = self.shader.find_uniform(b"sampler")

		# create texture

		texture_image = pyglet.image.load(path).get_image_data()

		self.texture = gl.GLuint(0)
		gl.glGenTextures(1, self.texture)
		gl.glBindTexture(gl.GL_TEXTURE_2D, self.texture)

		gl.glTexParameterf(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
		gl.glTexParameterf(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)

		gl.glTexImage2D(
			gl.GL_TEXTURE_2D, 0, gl.GL_RGBA,
			texture_image.width, texture_image.height, 0,
			gl.GL_RGBA, gl.GL_UNSIGNED_BYTE,
			texture_image.get_data("RGBA", texture_image.width * 4))

		gl.glGenerateMipmap(gl.GL_TEXTURE_2D)

		# create vertex array object

		self.vao = gl.GLuint(0)
		gl.glGenVertexArrays(1, ctypes.byref(self.vao))
		gl.glBindVertexArray(self.vao)

		# create vertex position vbo

		self.pos_vbo = gl.GLuint(0)
		gl.glGenBuffers(1, ctypes.byref(self.pos_vbo))
		gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.pos_vbo)

		t = gl.GLfloat * len(vertex_positions)

		gl.glBufferData(
			gl.GL_ARRAY_BUFFER,
			ctypes.sizeof(t), (t) (*vertex_positions),
			gl.GL_STATIC_DRAW)

		gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, 0, 0)
		gl.glEnableVertexAttribArray(0)
	
		# create texture coords vbo

		self.tex_coords_vbo = gl.GLuint(0)
		gl.glGenBuffers(1, ctypes.byref(self.tex_coords_vbo))
		gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.tex_coords_vbo)

		t = gl.GLfloat * len(tex_coords)

		gl.glBufferData(
			gl.GL_ARRAY_BUFFER,
			ctypes.sizeof(t), (t) (*tex_coords),
			gl.GL_STATIC_DRAW)

		gl.glVertexAttribPointer(1, 2, gl.GL_FLOAT, gl.GL_FALSE, 0, 0)
		gl.glEnableVertexAttribArray(1)

		# create index buffer object

		self.ibo = gl.GLuint(0)
		gl.glGenBuffers(1, ctypes.byref(self.ibo))
		gl.glBindBuffer(gl.GL_ELEMENT_ARRAY_BUFFER, self.ibo)

		t = gl.GLuint * len(indices)

		gl.glBufferData(
			gl.GL_ELEMENT_ARRAY_BUFFER,
			ctypes.sizeof(t), (t) (*indices),
			gl.GL_STATIC_DRAW)

	def draw(self, player):
		# disable culling

		gl.glDisable(gl.GL_CULL_FACE)
		gl.glEnable(gl.GL_BLEND)

		# set uniforms

		self.shader.use()
		self.shader.uniform_matrix(self.mvp_location, player.world.mvp_matrix)
		self.shader.uniform_float(self.time_location, player.world.time)

		# bind textures

		gl.glActiveTexture(gl.GL_TEXTURE0)
		gl.glBindTexture(gl.GL_TEXTURE_2D, self.texture)
		gl.glUniform1i(self.sampler_location, 0)

		# draw stuff

		gl.glBindVertexArray(self.vao)
		gl.glDrawElements(gl.GL_TRIANGLES, len(indices), gl.GL_UNSIGNED_INT, None)

		# enable culling

		gl.glEnable(gl.GL_CULL_FACE)
		gl.glDisable(gl.GL_BLEND)
