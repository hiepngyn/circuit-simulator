# AND Gate File

class AND_gate:
    top_Input = False
    bottom_Input = False
    output = False

    def set_top_Input(self,in_Val):
        self.top_Input = in_Val

    def set_bottom_Input(self,in_Val):
        self.bottom_Input = in_Val

    def set_output(self):
        if((self.top_Input == True) and (self.bottom_Input == True)):
            self.output = True
        else:
            self.output == False
    
    def get_output(self):
        return self.output