#Power gate

class Power_gate:
    input = False  # Initially off

    def set_input(self, inputVal):
        self.input = inputVal

    def draw(self, canvas, x, y):
        self.input_id = canvas.create_rectangle(x-20, y-20, x+20, y+20, fill='red')  # Initially red
        self.text_id = canvas.create_text(x, y, text='Power')

        # Bind the toggle function to the rectangle
        canvas.tag_bind(self.input_id, '<Button-1>', lambda event: self.toggle_input(canvas))

        return (self.input_id, self.text_id)

    def toggle_input(self, canvas):
        self.input = not self.input
        color = 'green' if self.input else 'red'  # Green if on, red if off
        canvas.itemconfig(self.input_id, fill=color)  # Update the rectangle color
