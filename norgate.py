# NOR Gate File
class OR_gate:
    top_Input = True
    bottom_Input = True
    output = True

    def set_output(self):
        self.output = not (self.top_Input or self.bottom_Input)
    

    def set_TopInput(self, input_Val):
        self.top_Input = input_Val
    
    def set_BottomInput(self, input_Val):
        self.bottom_Input = input_Val


    def get_output(self):
        return self.output