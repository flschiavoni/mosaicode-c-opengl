#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Triangle(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Triangle"
        self.color = "150:250:250:150"
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

        self.properties = [{"name": "x1",
                            "label": "x1",
                            "type": MOSAICODE_FLOAT,
                            "lower": -2.0,
                            "upper": 2.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 0.0,
                            },
                            {"name": "y1",
                            "label": "y1",
                            "type": MOSAICODE_FLOAT,
                           "lower": -2.0,
                            "upper": 2.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 1.0,
                            },
                            {"name": "x2",
                            "label": "x2",
                            "type": MOSAICODE_FLOAT,
                           "lower": -2.0,
                            "upper": 2.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 1.0,
                            },
                            {"name": "y2",
                            "label": "y2",
                            "type": MOSAICODE_FLOAT,
                            "lower": -2.0,
                            "upper": 2.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": -1.0,
                            },
                            {"name": "x3",
                            "label": "x3",
                            "type": MOSAICODE_FLOAT,
                            "lower": -2.0,
                            "upper": 2.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": -1.0,
                            },
                            {"name": "y3",
                            "label": "y3",
                            "type": MOSAICODE_FLOAT,
                           "lower": -2.0,
                            "upper": 2.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": -1.0,
                            }
                           ]
        self.codes["function"] = """

        void mosaicgraph_draw_triangle(float x1, float x2, float x3, float y1, float y2, float y3){
            glColor3f(0.5,0.5,0.5);
            glBegin(GL_POLYGON);
                glVertex2f(x1,y1);
                glVertex2f(x2,y2);
                glVertex2f(x3,y3);
            glEnd();
        }

"""
        self.codes["call"] = """
        mosaicgraph_draw_triangle($prop[x1]$,$prop[x2]$,$prop[x3]$,$prop[y1]$,$prop[y2]$,$prop[y3]$);
"""
