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
        self.color = "150:150:250:150"
        self.group = "Shapes"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.color",
                "label":"Color",
                "conn_type":"Input",
                "name":"color"}
            ]

        self.properties = [{"name": "x1",
                            "label": "x1",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1,
                            "upper": 1,
                            "step": 0.001,
                            "value": 0.0,
                            },
                            {"name": "y1",
                            "label": "y1",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1,
                            "upper": 1,
                            "step": 0.001,
                            "value": 1.0,
                            },
                            {"name": "x2",
                            "label": "x2",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1,
                            "step": 0.001,
                            "upper": 1,
                            "value": 1,
                            },
                            {"name": "y2",
                            "label": "y2",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1,
                            "upper": 1,
                            "step": 0.001,
                            "value": -1,
                            },
                            {"name": "x3",
                            "label": "x3",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1,
                            "upper": 1,
                            "step": 0.001,
                            "value": -1.0,
                            },
                            {"name": "y3",
                            "label": "y3",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1,
                            "step": 0.001,
                            "upper": 1,
                            "value": -1.0,
                            }
                           ]

        self.codes["declaration"] = """
        float $port[color]$[3];
"""

        self.codes["execution"] = """
        // Triangle Baby!
		mosaicgraph_coordinate_t coordinate$id$;
		coordinate$id$.len = 3;
		float tri$id$[6] = {$prop[x1]$,$prop[y1]$,$prop[x2]$,$prop[y2]$,$prop[x3]$,$prop[y3]$};
		coordinate$id$.coordinates = tri$id$;
		mosaicgraph_polygon_t * triangle$id$ = mosaicgraph_create_polygon(coordinate$id$);
		triangle$id$ = mosaicgraph_colored_polygon(triangle$id$, $port[color]$[0], $port[color]$[1], $port[color]$[2]);
		mosaicgraph_draw_polygon(*triangle$id$);
"""
