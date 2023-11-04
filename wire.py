class Wire:
    id = 0
    def __init__(self, canvas, start_gate, end_gate, start_pos, end_pos):
        self.canvas = canvas
        self.start_gate = start_gate
        self.end_gate = end_gate
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.selected = False
        self.connected_to = None

    def draw(self, x, y):
        self.start_pos = (x, y)
        self.end_pos = (x + 100, y)
        self.start_button = self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='white')
        self.end_button = self.canvas.create_oval(x + 95, y - 5, x + 105, y + 5, fill='white')
        self.line_id = self.canvas.create_line(x, y, x + 100, y, fill='black', dash=(4, 2))

        self.canvas.tag_bind(self.start_button, '<Button-1>', self.on_start_button_click)
        self.canvas.tag_bind(self.end_button, '<Button-1>', self.on_end_button_click)


    def on_start_button_click(self, event):
        self.selected = not self.selected 
        if self.selected:
            self.canvas.itemconfig(self.start_button, fill='blue') 
            print(f"Wire {self.id} selected.")
        else:
            self.canvas.itemconfig(self.start_button, fill='white')
            print(f"Wire {self.id} deselected.")
    
    def on_end_button_click(self, event):
        self.end_selected = not self.end_selected
        if self.end_selected:
            self.canvas.itemconfig(self.end_button, fill='blue')
        else:
            self.canvas.itemconfig(self.end_button, fill='white')

    def connect_to(self, source):
        if self.selected:
            self.connected_to = source
            print(f"Wire {self.id} connected to {source}")
            self.update_power(source.power)
            self.deselect()
    
    def connect_end_to(self, gate):
        self.end_gate = gate
        self.update_end_position(gate.get_input_connection_coord())
        print(f"Wire {self} connected to gate {gate}")
    
    def deselect(self):
        self.selected = False
        self.canvas.itemconfig(self.start_button, fill='white')
    
    def update_power(self, power_state):
        color = 'red' if power_state else 'black'
        self.canvas.itemconfig(self.line_id, fill=color)
        if power_state:
            print(f"Wire {self.id} is powered.")
        else:
            print(f"Wire {self.id} is not powered.")
    
    def update_start_position(self, new_start):
        print(f"Updating start position to: {new_start}")
        self.start_pos = new_start
        self.canvas.coords(self.line_id, *new_start, *self.end_pos)
        self.canvas.itemconfig(self.start_button, fill='blue')
        self.canvas.tag_raise(self.start_button)  # Ensure the button is above the line
        self.canvas.tag_raise(self.end_button)    # Ensure the button is above the line
        self.canvas.update_idletasks()  # This forces the canvas to redraw which can help in some cases
    
    def update_end_position(self, new_end):
        self.end_pos = new_end
        self.canvas.coords(self.line_id, *self.start_pos, *new_end)
        self.canvas.itemconfig(self.end_button, fill='blue')  
        self.canvas.tag_raise(self.start_button) 
        self.canvas.tag_raise(self.end_button)   
        self.canvas.update_idletasks()