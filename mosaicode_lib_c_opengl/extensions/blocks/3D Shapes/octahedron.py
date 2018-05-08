#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Octahedron(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Octahedron"
        self.color = "150:150:250:150"
        self.group = "3D Shapes"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.color",
                "label":"Color",
                "conn_type":"Input",
                "name":"color"}
            ]

        self.codes["function"] = """
        void mosaicgraph_draw_octahedron(){
            glColor3f(0.8f,0.2f,0.0);
            glutSolidOctahedron();
        }

"""
        self.codes["call"] = """
        mosaicgraph_draw_octahedron();
"""