# NOT Gate File

class NOT_gate:
    input = False


    def set_input(self, inputVal):
        self.input = inputVal


    def get_output(self):
        return not self.input
    
    def draw(self, canvas, x, y):
        self.gate_id = canvas.create_rectangle(x-20, y-20, x+20, y+20, fill='white')
        self.text_id = canvas.create_text(x, y, text='NOT')

        self.input1_id = canvas.create_oval(x-30, y+6, x-20, y+15, fill='red')
        self.output_id = canvas.create_oval(x+20, y+5, x+30, y+15, fill='green')

        canvas.tag_bind(self.input1_id, '<Button-1>', lambda event: self.toggle_input(canvas, 'input'))

        return (self.gate_id, self.text_id, self.input1_id, self.output_id)

    def toggle_input(self, canvas, input_side):
        if input_side == 'input':
            self.input = not self.input
            color = 'green' if self.input else 'red'
        canvas.itemconfig(self.input1_id, fill=color)
        
        output_color = 'green' if self.get_output() else 'black'
        canvas.itemconfig(self.output_id, fill=output_color)
        




