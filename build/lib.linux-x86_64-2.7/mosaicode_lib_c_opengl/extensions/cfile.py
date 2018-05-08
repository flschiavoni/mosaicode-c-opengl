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
        self.extension = ".c"
        self.command = "gcc -Wall -g $dir_name$$filename$$extension$ -o $dir_name$$filename$ -lGL -lGLU -lglut -lm\n"
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

$single_code[function]$
void display(){

  glMatrixMode(GL_MODELVIEW);
  glClear(GL_COLOR_BUFFER_BIT);         // Limpa o collor buffer
  glLoadIdentity();
  $code[call]$
  glutSwapBuffers();
  glFlush();
}
void idle(){
    $code[idle]$
}
int main (int argc, char** argv){
	glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH);
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
	$code[declaration]$

    $code[execution, connection]$
    display();
    glutIdleFunc(&idle);
    glutMainLoop();
	return 0;
}
"""

# -------------------------------------------------------------------------
