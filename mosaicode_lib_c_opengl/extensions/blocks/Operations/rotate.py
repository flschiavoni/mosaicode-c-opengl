#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Rotate(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Rotate"
        self.color = "50:50:50:150"
        self.group = "Operations"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.flow",
                    "label":"Flow",
                    "conn_type":"Input",
                    "name":"flow"},
                    {"type":"mosaicode_lib_c_opengl.extensions.ports.flow",
                    "label":"Flow",
                    "conn_type":"Output",
                    "name":"flow"}
            ]

        self.properties = [{"name": "x",
                            "label": "x",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.001,
                            "value": 0.01,
                            },
                            {"name": "y",
                            "label": "y",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.001,
                            "value": 0.01,
                            },
                            {"name": "z",
                            "label": "z",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.001,
                            "value": 0.01,
                            },
                            {"name": "angle",
                            "label": "angle",
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 1000,
                            "step": 1,
                            "value": 100,
                            }
                           ]
        self.codes["global"] = """
GLfloat xRotated$id$, yRotated$id$, zRotated$id$;
"""
        self.codes["call"] = """
    glRotatef(xRotated$id$,1.0,0.0,0.0);
    // rotation about Y axis
    glRotatef(yRotated$id$,0.0,1.0,0.0);
    // rotation about Z axis
    glRotatef(zRotated$id$,0.0,0.0,1.0);
"""

        self.codes["idle"] = """
     xRotated$id$ += $prop[x]$;
     yRotated$id$ += $prop[y]$;
     zRotated$id$ += $prop[z]$;
     
"""

        self.codes["declaration"] = """
    xRotated$id$ = yRotated$id$ = zRotated$id$ = $prop[angle]$;
"""
