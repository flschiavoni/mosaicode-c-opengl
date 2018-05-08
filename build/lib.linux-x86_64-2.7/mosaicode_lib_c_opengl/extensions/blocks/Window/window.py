#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Window class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Window(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Window"
        self.color = "250:150:150:150"
        self.group = "Window"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.flow",
                "label":"Flow",
                "conn_type":"Output",
                "name":"flow"},
                {"type":"mosaicode_lib_c_opengl.extensions.ports.flow",
                "label":"Flow",
                "conn_type":"Input",
                "name":"flow"}
            ]

        self.properties = [{"name": "x",
                            "label": "x",
                            "type": MOSAICODE_INT,
                            "lower": 100,
                            "upper": 2000,
                            "step": 1,
                            "value": 0,
                            },
                            {"name": "y",
                            "label": "y",
                            "type": MOSAICODE_INT,
                            "lower": 100,
                            "upper": 2000,
                            "step": 1,
                            "value": 0,
                            },
                            {"name": "width",
                            "label": "width",
                            "type": MOSAICODE_INT,
                            "lower": 100,
                            "upper": 2000,
                            "step": 1,
                            "value": 500,
                            },
                            {"name": "height",
                            "label": "height",
                            "type": MOSAICODE_INT,
                            "lower": 100,
                            "upper": 2000,
                            "step": 1,
                            "value": 500,
                            },
                            {"name": "title",
                            "label": "title",
                            "type": MOSAICODE_STRING,
                            "value": "New Window",
                            }
                           ]
        self.codes["call"] = """
        glutSwapBuffers();
        glFlush();
        mosaicgraph_window_t * window$id$ = mosaicgraph_create_window($prop[width]$,$prop[height]$,$prop[x]$,$prop[y]$);
        strcpy(window$id$->title, "$prop[title]$");
        mosaicgraph_draw_window(window$id$);
"""
