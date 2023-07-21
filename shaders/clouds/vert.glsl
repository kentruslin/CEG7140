#version 330

uniform mat4 matrix;
uniform float time;

layout(location = 0) in vec3 pos;
layout(location = 1) in vec2 tex_coord;

out vec2 interp_tex_coord;

void main(void) {
	interp_tex_coord = vec2(tex_coord.x, tex_coord.y + time / 10000.0);
	gl_Position = matrix * vec4(pos, 1.0);
}
