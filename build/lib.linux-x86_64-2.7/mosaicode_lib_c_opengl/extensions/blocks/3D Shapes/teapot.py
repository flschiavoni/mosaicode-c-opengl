#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Teapot(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Teapot"
        self.color = "50:250:150:150"
        self.group = "3D Shapes"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.color",
                "label":"Color",
                "conn_type":"Input",
                "name":"color"}
            ]

        self.properties = [{"name": "size",
                            "label": "size",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "value": 0.5,
                            }
                           ]
        self.codes["function"] = """
        void mosaicgraph_draw_teapot(float size){
            glColor3f(0.8f,0.2f,0.0);
            glutSolidTeapot(size);
        }

"""
        self.codes["call"] = """
        mosaicgraph_draw_teapot($prop[size]$);
"""