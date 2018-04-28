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
        self.color = "150:150:250:150"
        self.group = "Types"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.color",
                "label":"Color",
                "conn_type":"Output",
                "name":"color"}
            ]

        self.properties = [{"name": "color",
                            "label": "Color",
                            "value":"#FF0000",
                            "format":"FF0000",
                            "type": MOSAICODE_COLOR
			                }]

        self.codes["function"] = """
void convert_text_to_color(const char * rgbColor, float * output){
    if (strlen(rgbColor) < 7 || rgbColor[0] != '#'){
        output[0] = 0;
        output[1] = 0;
        output[2] = 0;
        }

    char r[2], g[2], b[2];
    strncpy(r, rgbColor+1, 2);
    strncpy(g, rgbColor+3, 2);
    strncpy(b, rgbColor+5, 2);

    float ri, gi, bi = 0;
    ri = (float) strtol(r, NULL, 16);
    gi = (float) strtol(g, NULL, 16);
    bi = (float) strtol(b, NULL, 16);

    output[0] = ri / 255.0;
    output[0] = gi / 255.0;
    output[0] = bi / 255.0;
}
"""

        self.codes["declaration"] = """
        // Color Baby!
		float $port[color]$[3];
        convert_text_to_color("$prop[color]$", $port[color]$);
"""
