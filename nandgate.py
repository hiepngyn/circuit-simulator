# NAND Gate File

class NAND_gate:
    top_Input = False
    bottom_Input = False
    output = True

    def set_top_Input(self,in_Val):
        self.top_Input = in_Val

    def set_top_Input(self,in_Val):
        self.bottom_Input = in_Val

    def set_output(self):
        if((self.top_input == True) or (self.bottom_Input == True)):
            self.output = False
        else:
            self.output = True
    
    def get_output(self):
        return self.output