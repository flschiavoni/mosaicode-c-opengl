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
        self.command = "g++ -Wall -g $dir_name$$filename$$extension$ -o $dir_name$$filename$ -lGL -lGLU -lglut -lm\n"
        self.command += "$dir_name$./$filename$"
        self.code_parts = ["global", "function", "call","idle","declaration", "execution"]
        self.code = r"""
#include <GL/glut.h>    // Header File For The GLUT Library 
#include <GL/gl.h>  // Header File For The OpenGL32 Library
#include <GL/glu.h> // Header File For The GLu32 Library
#include <unistd.h> 
#include <string.h>
#include <stdio.h>
#include <math.h>
#define ESCAPE 27 //Valor em ASCII do Esc
int window;
$code[global]$

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
}mosaicgraph_window_t;
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
$single_code[function]$
void display(){
  glMatrixMode(GL_MODELVIEW);
  //glClearColor(0.0f, 0.0f, 0.0f, 1.0f); // Seta Background
  glClear(GL_COLOR_BUFFER_BIT);         // Limpa o collor buffer
  $code[call]$
  glutSwapBuffers(); 
  glFlush();
}
void idle(){
    $code[idle]$
    display();
}
int main (int argc, char** argv){
	glutInit(&argc, argv);

	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH);
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
	mosaicgraph_window_t * window1 = mosaicgraph_create_window(500,500);
	strcpy(window1->title, "Casinha");
        mosaicgraph_draw_window(window1);
	
	$code[declaration]$

    $code[execution, connection]$
    glutDisplayFunc(display);
    glutIdleFunc(&idle);
    glutSwapBuffers();
    glutMainLoop();
	return 0;
}
"""

# -------------------------------------------------------------------------
