#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Circle(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Circle"
        self.color = "250:150:150:150"
        self.group = "2D Shapes"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.flow",
                "label":"Flow",
                "conn_type":"Input",
                "name":"flow"},
                {"type":"mosaicode_lib_c_opengl.extensions.ports.flow",
                "label":"Flow",
                "conn_type":"Output",
                "name":"flow"},
                {"type":"mosaicode_lib_c_opengl.extensions.ports.color",
                "label":"Color",
                "conn_type":"Input",
                "name":"color"}
            ]

        self.properties = [{"name": "radius",
                            "label": "Radius",
                            "type": MOSAICODE_FLOAT,
                            "lower": -2.0,
                             "upper": 2.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 0.5
                            }
                           ]
        self.codes["function"] = """
        void mosaicgraph_draw_circle(float radius){
            glColor3f(0.8f,0.2f,0.0);
            glBegin(GL_POLYGON);
                for (int i=0; i < 360; i++){
                    float degInRad = i*3.14159/180;
                    glVertex2f(cos(degInRad)*radius,sin(degInRad)*radius);
                }
            glEnd();
        }

"""
        self.codes["call"] = """
        mosaicgraph_draw_circle($prop[radius]$);
"""
