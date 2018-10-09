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
        self.label = "Keyboard"
        self.color = "150:50:50:100"
        self.group = "I/O"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.float",
                    "label":"Value01",
                    "conn_type":"Output",
                    "name":"value01"},
                    {"type":"mosaicode_lib_c_opengl.extensions.ports.float",
                    "label":"Value02",
                    "conn_type":"Output",
                    "name":"value02"},
                    {"type":"mosaicode_lib_c_opengl.extensions.ports.float",
                    "label":"Value03",
                    "conn_type":"Output",
                    "name":"value03"}
            ]

        self.properties = [{"name": "value01up",
                            "label": "value 01 UP",
                            "type": MOSAICODE_STRING,
                            "value": "a"
                            },
                            {"name": "value01down",
                            "label": "value 01 DOWN",
                            "type": MOSAICODE_STRING,
                            "value": "d"
                            },
                            {"name": "value02up",
                            "label": "value 02 UP",
                            "type": MOSAICODE_STRING,
                            "value": "w"
                            },
                            {"name": "value02down",
                            "label": "value 02 DOWN",
                            "type": MOSAICODE_STRING,
                            "value": "s"
                            },
                            {"name": "value03up",
                            "label": "value 03 UP",
                            "type": MOSAICODE_STRING,
                            "value": "q"
                            },
                            {"name": "value03down",
                            "label": "value 03 DOWN",
                            "type": MOSAICODE_STRING,
                            "value": "e"
                            }]
       
        self.codes["global"] = """
        GLfloat value01$id$, value02$id$, value03$id$;
"""
        self.codes["function"] = """
    void keyPressed(unsigned char key, int x, int y) {
    usleep(100);
    if (key == 27){
      glutDestroyWindow(window);
      exit(0);
    }else if(key == (int)'$prop[value01up]$'){
      if(value01$id$<2.0){
        value01$id$ += 0.001;
      }
    }else if (key == (int)'$prop[value01down]$'){
      if(value01$id$>-2.0){
        value01$id$ -= 0.001;
      }
    }else if (key == (int)'$prop[value02up]$'){
      if(value02$id$<2.0){
        value02$id$ += 0.001;
      }
    }else if (key == (int)'$prop[value02down]$'){
      if(value02$id$>-2.0){
        value02$id$ -= 0.001;
      }
    }else if (key == (int)'$prop[value03up]$'){
      if(value03$id$<2.0){
        value03$id$ += 0.001;
      }
    }else if (key == (int)'$prop[value03down]$'){
      if(value03$id$>-2.0){
        value03$id$ -= 0.001;
      }
    }
}
"""
        self.codes["declaration"] = """
        value01$id$ = 0.5;
        value02$id$ = 0.5;
        value03$id$ = 0.5;
"""
        self.codes["execution"] = """
        glutKeyboardFunc(&keyPressed);


"""
