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
    
    def draw(self, canvas, x, y):
        self.gate_id = canvas.create_rectangle(x-20, y-20, x+20, y+20, fill='white')
        self.text_id = canvas.create_text(x, y, text='AND')

        self.input1_id = canvas.create_oval(x-30, y-10, x-20, y, fill='red')
        self.input2_id = canvas.create_oval(x-30, y+10, x-20, y+20, fill='red')
        self.output_id = canvas.create_oval(x+20, y+5, x+30, y+15, fill='black')

        canvas.tag_bind(self.input1_id, '<Button-1>', lambda event: self.toggle_input(canvas, 'top'))
        canvas.tag_bind(self.input2_id, '<Button-1>', lambda event: self.toggle_input(canvas, 'bottom'))

        return (self.gate_id, self.text_id, self.input1_id, self.input2_id, self.output_id)

    def toggle_input(self, canvas, input_side):
        if input_side == 'top':
            self.top_Input = not self.top_Input
            color = 'green' if self.top_Input else 'red'
        elif input_side == 'bottom':
            self.bottom_Input = not self.bottom_Input
            color = 'green' if self.bottom_Input else 'red'
        
        canvas.itemconfig(self.input1_id if input_side == 'top' else self.input2_id, fill=color)
        
        self.set_output()
        output_color = 'green' if self.get_output() else 'black'
        canvas.itemconfig(self.output_id, fill=output_color)
        