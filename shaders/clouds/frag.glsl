#version 330

out vec4 frag_color;

uniform sampler2D sampler;

in vec2 interp_tex_coord;

void main(void) {
	frag_color = texture(sampler, interp_tex_coord);
}
