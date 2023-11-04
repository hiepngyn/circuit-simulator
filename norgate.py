# NOR Gate File
class NOR_gate:
    top_Input = False
    bottom_Input = False
    output = False

    def set_output(self):
        self.output = not (self.top_Input or self.bottom_Input)
    

    def set_TopInput(self, input_Val):
        self.top_Input = input_Val
    
    def set_BottomInput(self, input_Val):
        self.bottom_Input = input_Val


    def get_output(self):
        return self.output