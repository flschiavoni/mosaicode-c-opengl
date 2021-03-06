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
        self.label = "Mouse Click"
        self.color = "250:50:50:100"
        self.group = "I/O"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.float",
                    "label":"X",
                    "conn_type":"Output",
                    "name":"x"},
                    {"type":"mosaicode_lib_c_opengl.extensions.ports.float",
                    "label":"Y",
                    "conn_type":"Output",
                    "name":"y"}
                    ]

      
        self.codes["global"] = """
std::vector<void (*)(float)> $port[x]$; //mouse output
std::vector<void (*)(float)> $port[y]$; //mouse output
"""

        self.codes["function"] = """
    void onMouseButton(int button, int state, int x, int y){
        if(button == GLUT_LEFT_BUTTON){
            if(value01$id$ < 2.0){
                value01$id$ += 0.01;
            }
        }else if(button == GLUT_RIGHT_BUTTON){
            if(value01$id$ > -2.0){
                value01$id$ -= 0.01;
            }
        }
    for(auto n : $port[x]$){
         n(x);
    }
    for(auto n : $port[y]$){
         n(y);
    }
    }
"""

        self.codes["declaration"] = """
"""

        self.codes["execution"] = """
        glutMouseFunc(onMouseButton);

"""
