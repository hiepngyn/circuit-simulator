# OR Gate File

def class OR_gate:
    top_Input = True
    bottom_Input = True
    output = True

 def set_output(self):
        output = !input
    

    def set_TopInput(self, input_Val):
        self.top_Input = input_Val
    
    def set_BottomInput(self, input_Val):
        self.bottom_Input = input_Val


    

    def get_output(self):
        return (top_Input or bottom_Input)

