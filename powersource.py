#Power Source
class Power_Source:

    power = False 

    def draw(self, canvas, x, y):
        self.button_id = canvas.create_oval(x-15, y-15, x+15, y+15, fill='red')
        self.text_id = canvas.create_text(x, y, text='OFF')

        canvas.tag_bind(self.button_id, '<Button-1>', lambda event: self.toggle_power(canvas))

        return self.button_id, self.text_id

    def toggle_power(self, canvas):
        self.power = not self.power
        color = 'green' if self.power else 'red' 
        text = 'ON' if self.power else 'OFF'
        canvas.itemconfig(self.button_id, fill=color) 
        canvas.itemconfig(self.text_id, text=text)
        if hasattr(self, 'wire'):
            self.wire.update_power(self.power)  

    def get_connection_coord(self):
        return self.x, self.y
    
    def connect_wire(self, wire):
        wire.connect_to(self)
        self.wire = wire

    def get_connection_coord(self):
            bbox = self.canvas.bbox(self.button_id)
            return ((bbox[0] + bbox[2]) // 2, bbox[1])