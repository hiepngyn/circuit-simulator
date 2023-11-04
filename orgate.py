# OR Gate File
class OR_gate:
    top_Input = True
    bottom_Input = True
    output = True

    def set_output(self):
        self.output = (self.top_Input or self.bottom_Input)