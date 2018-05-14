#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class ScaleLoop(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Scale Loop"
        self.color = "50:250:250:100"
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
                            }
                           ]
        self.codes["global"] = """
GLfloat xScale$id$,yScale$id$,zScale$id$;
"""
        self.codes["call"] = """
    glScalef(xScale$id$,yScale$id$,zScale$id$);
"""
        self.codes["idle"] = """
    xScale$id$ += $prop[x]$;
    yScale$id$ += $prop[y]$;
    zScale$id$ += $prop[z]$;
"""

        self.codes["execution"] = """
    xScale$id$ = yScale$id$ = zScale$id$ = 1.0;

"""
