from mosaicode.model.port import Port

class Flow(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.hint = "FLOW"
        self.color = "#2c6324"
        self.multiple = False
        #self.code = "memcpy($output$, $input$,  sizeof($input$));\n"
        self.var_name = "$block[label]$_$block[id]$_$port[name]$"
