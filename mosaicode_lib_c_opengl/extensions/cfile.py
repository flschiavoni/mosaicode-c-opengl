# -*- coding: utf-8 -*-
# [MOSAICODE PROJECT]
#
"""
This module contains the JavascriptTemplate class.
"""
from mosaicode.model.codetemplate import CodeTemplate


class CFile(CodeTemplate):
    """
    This class contains methods related the JavascriptTemplate class.
    """
    # ----------------------------------------------------------------------

    def __init__(self):
        CodeTemplate.__init__(self)
        self.name = "opengl"
        self.language = "c"
        self.description = "A full template to generate opengl code"
        self.extension = ".cpp"
        self.command = "g++ -Wall -g $dir_name$$filename$$extension$ -o $dir_name$$filename$ -lGL -lGLU -lglut\n"
        self.command += "$dir_name$./$filename$"
        self.code_parts = ["function", "declaration", "execution"]
        self.code = r"""
#include <GL/glut.h>
#include <GL/gl.h>
#include <GL/glu.h>
#include <string.h>
#include <stdio.h>

typedef struct mosaicgraph_window{
        float x;
        float y;
        float width;
        float height;
        float red;
        float green;
        float blue;
        float alpha;
        float fullscreen;
        char title[128];
        int id;
        void (*process)(void *self);
} mosaicgraph_window_t;

typedef struct mosaicgraph_coordinate{
        int len;
        float *coordinates;
} mosaicgraph_coordinate_t;

typedef struct mosaicgraph_polygon{
        int len;
        float *coordinates;
        float red;
        float green;
        float blue;
        void (*process)(void *self);
} mosaicgraph_polygon_t;

mosaicgraph_window_t * mosaicgraph_create_window(float width, float height){
	mosaicgraph_window_t * window = (mosaicgraph_window_t *) malloc(sizeof(mosaicgraph_window_t));
	window->fullscreen = 0;
	window->x = 0;
	window->y = 0;
	window->width = width;
	window->height = height;
	window->title[0] = '\0';
	return window;
}
int mosaicgraph_draw_window(mosaicgraph_window_t * window){
    glutInitWindowPosition(window->x, window->y);
    glutInitWindowSize(window->width, window->height);
	glClearColor(window->red, window->green, window->blue, window->alpha);
	glClear(GL_COLOR_BUFFER_BIT);
    window->id = glutCreateWindow(window->title);
    if (window->fullscreen){
   		glutFullScreen();
    }
    glFlush();
	glutSwapBuffers();
    return window->id;
}
mosaicgraph_polygon_t * mosaicgraph_colored_polygon(mosaicgraph_polygon_t * triangle, float red, float green, float blue){
    triangle->red = red;
    triangle->green = green;
    triangle->blue = blue;
  	return triangle;
}

mosaicgraph_polygon_t * mosaicgraph_create_polygon(mosaicgraph_coordinate_t coordinate){
		mosaicgraph_polygon_t * polygon = (mosaicgraph_polygon_t *) malloc(sizeof(mosaicgraph_polygon_t));
		float * vector = (float *)malloc(coordinate.len*2*sizeof(float));
		polygon->len = coordinate.len;
		for (int i=0;i<coordinate.len*2;i++){
			vector[i] = coordinate.coordinates[i];
		}
		polygon->coordinates = vector;
		return polygon;
}
void mosaicgraph_draw_polygon(mosaicgraph_polygon_t polygon){
	glColor3f(polygon.red,polygon.green,polygon.blue);
	glBegin(GL_POLYGON);
		for(int i =0;i < polygon.len*2;i=i+2){
			glVertex3f(polygon.coordinates[i],polygon.coordinates[i+1],0.0);
		}


	glEnd();
}

$single_code[function]$

int main (int argc, char** argv){
	glutInit(&argc, argv);

	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH);
	mosaicgraph_window_t * window1 = mosaicgraph_create_window(500,500);
	strcpy(window1->title, "Casinha");
        mosaicgraph_draw_window(window1);
	
	$code[declaration]$

        $code[execution, connection]$

    glutSwapBuffers();
    glutMainLoop();
	return 0;
}
"""

# -------------------------------------------------------------------------
