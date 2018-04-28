from mosaicode.model.port import Port

class Float(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.hint = "FLOAT"
        self.color = "#2c6300"
        self.multiple = False
        self.code = "$output$ = $input$;\n"
        self.var_name = "$block[label]$_$block[id]$_$port[name]$"	
