#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Window class.
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
        self.color = "250:150:150:150"
        self.group = "Types"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.color",
                "label":"Color",
                "conn_type":"Output",
                "name":"color"}
            ]

        self.properties = [{"name": "color",
                            "label": "color",
                            "type": MOSAICODE_COLOR,
                            "value": "#FF0000",
                            }
                           ]
        self.codes["execution"] = """
        $port[color]$ = $prop[color]$;
"""
