# -*- coding: utf-8 -*-
# [MOSAICODE PROJECT]
#
"""
This module contains the JavascriptTemplate class.
"""
from mosaicode.model.codetemplate import CodeTemplate


class Html(CodeTemplate):
    """
    This class contains methods related the JavascriptTemplate class.
    """
    # ----------------------------------------------------------------------

    def __init__(self):
        CodeTemplate.__init__(self)
        self.name = "opengl"
        self.language = "C"
        self.description = "A full template to generate opengl code"
        self.extension = ".c"
        self.command = "g++ -Wall -g $dir_name$$filename$$extension$ -o $dir_name$$filename$ -lGL -lGLU -lglut\n"
        self.code_parts = ["onload", "function", "declaration", "execution", "html"]
        self.code = r"""
#include "createCanvas.h"

int main (int argc, char** argv){
	glutInit(&argc, argv);

	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH);
	mosaicgraph_window_t * window1 = mosaicgraph_create_window(500,500);
	strcpy(window1->title, "Casinha");
    mosaicgraph_draw_window(window1);
		mosaicgraph_coordinate_t coordinate;
		coordinate.len = 3;
		float tri[6] = {-1.0,0.0,-0.75,1.0,-0.5,0.0};
		coordinate.coordinates = tri;
		//triangulo do telhado
		mosaicgraph_polygon_t * triangle = mosaicgraph_create_polygon(coordinate);
		triangle = mosaicgraph_colored_polygon(triangle,0.5,0.7,0.3);
		mosaicgraph_draw_polygon(*triangle);
		//retangulo da fachada
		coordinate.len = 4;
		float ret[8] = {-1.0,-1.0,-0.5,-1.0,-0.5,0.0,-1.0,0.0};
		coordinate.coordinates = ret;
		mosaicgraph_polygon_t * retangle = mosaicgraph_create_polygon(coordinate);
		retangle = mosaicgraph_colored_polygon(retangle,1.0,0.4,0.7);
		mosaicgraph_draw_polygon(*retangle);
		//retangulo da porta
		float ret2[8] = {-0.85,-1.0,-0.85,-0.5,-0.65,-0.5,-0.65,-1.0};
		coordinate.len = 4;
		coordinate.coordinates = ret2;
		mosaicgraph_polygon_t * retangle2 = mosaicgraph_create_polygon(coordinate);
		retangle2 = mosaicgraph_colored_polygon(retangle2,0.0,0.4,0.7);
		mosaicgraph_draw_polygon(*retangle2);
		//paralelograma do telhado
		float ret3[8] = {-0.5,0.0,-0.5-0.25,1.0,0.5,1.0,0.5+0.25,0.0};
		coordinate.len = 4;
		coordinate.coordinates = ret3;
		mosaicgraph_polygon_t *paralelogram = mosaicgraph_create_polygon(coordinate);
		paralelogram = mosaicgraph_colored_polygon(paralelogram,0.0,0.4,0.7);
		mosaicgraph_draw_polygon(*paralelogram);
		//retangulo da parede
		float ret4[8] = {-0.5,0.0,0.75,0.0,0.75,-1.0,-0.5,-1.0};
		coordinate.len = 4;
		coordinate.coordinates = ret4;
		mosaicgraph_polygon_t * retangle3 = mosaicgraph_create_polygon(coordinate);
		retangle3 = mosaicgraph_colored_polygon(retangle3,0.0,1.0,0.7);
		mosaicgraph_draw_polygon(*retangle3);
    glutSwapBuffers();
    glutMainLoop();
	return 0;
}
"""

# -------------------------------------------------------------------------
