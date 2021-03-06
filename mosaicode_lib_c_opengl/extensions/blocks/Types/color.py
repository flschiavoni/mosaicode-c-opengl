#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Color(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Color"
        self.color = "200:200:150:150"
        self.group = "Types"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.color",
                    "label":"Color",
                    "conn_type":"Output",
                    "name":"color"}
            ]
#        self.properties = [{"name": "size",
#                            "label": "size",
#                            "type": MOSAICODE_FLOAT,
#                            "lower": -1.0,
#                            "upper": 1.0,
#                            "step": 0.01,
#                            "value": 0.5,#
#			    "page_inc": 0.1,
#                            "page_size": 0.1,
#                            }
#                           ]
#        self.codes["declaration"] = """
#        float value$id$ = $prop[size]$;
#"""
