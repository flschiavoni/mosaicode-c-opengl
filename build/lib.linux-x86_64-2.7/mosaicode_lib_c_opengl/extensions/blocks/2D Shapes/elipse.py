#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Elipse(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Elipse"
        self.color = "250:250:50:150"
        self.group = "2D Shapes"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.color",
                "label":"Color",
                "conn_type":"Input",
                "name":"color"}
            ]

        self.properties = [{"name": "radius",
                            "label": "Radius",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "value": 0.5,
                            },
                            {"name": "focusX",
                            "label": "Focus X",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "value": 0.0,
                            },
                            {"name": "focusY",
                            "label": "Focus Y",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "value": 0.5,
                            }
                           ]
        self.codes["function"] = """
        void mosaicgraph_draw_elipse(float radius,float elipse_x,float elipse_y){
            glColor3f(0.8f,0.6f,0.0);
            glBegin(GL_POLYGON);       
            for (int i=0; i < 360; i++){
                    float degInRad = i*3.14159/180;
                    glVertex2f(cos(degInRad)*(radius+elipse_x),sin(degInRad)*(radius+elipse_y));
                }     
            glEnd();
        }

"""
        self.codes["call"] = """
        mosaicgraph_draw_elipse($prop[radius]$,$prop[focusY]$,$prop[focusX]$);
"""