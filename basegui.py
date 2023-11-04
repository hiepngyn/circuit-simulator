import tkinter as tk
from andgate import AND_gate
from orgate import OR_gate
from notgate import NOT_gate
from nandgate import NAND_gate
from norgate import NOR_gate
from xorgate import XOR_gate
from powersource import Power_gate

class DragDropToolbar:
    def __init__(self, root):
        self.root = root
        self.root.title('Logic Gates Simulator')
        
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack(expand=True, fill='both')
        
        self.toolbar = tk.Frame(root, bg='grey')
        self.toolbar.pack(side='bottom', fill='x')
        
        self.add_gate_button('AND', self.toolbar)
        self.add_gate_button('OR', self.toolbar)
        self.add_gate_button('NOT', self.toolbar)
        self.add_gate_button('NAND', self.toolbar)
        self.add_gate_button('NOR', self.toolbar)
        self.add_gate_button('XOR', self.toolbar)
        self.add_gate_button('Power', self.toolbar)


        
        self.selected_gate = None

        self.gate_objects = {}

    def add_gate_button(self, gate_type, parent):
        button = tk.Button(parent, text=gate_type, command=lambda: self.select_gate(gate_type))
        button.pack(side='left', padx=2, pady=2)

    def select_gate(self, gate_type):
        self.selected_gate = gate_type
        print(f'Selected {gate_type} gate')

    def on_canvas_click(self, event):
        if self.selected_gate:
            x, y = event.x, event.y
            if self.selected_gate == 'AND':
                gate = AND_gate() 
                items = gate.draw(self.canvas, x, y)
                item_id = items[0] 
            elif self.selected_gate == 'OR':
                gate = OR_gate()
                items = gate.draw(self.canvas,x,y)
                items_id = items[0]
            elif self.selected_gate == 'NOT':
                gate = NOT_gate()
                items = gate.draw(self.canvas,x,y)
                items_id=items[0]
            elif self.selected_gate == 'NAND':
                gate = NAND_gate()
                items = gate.draw(self.canvas,x,y)
                items_id=items[0]
            elif self.selected_gate == 'NOR':
                gate = NOR_gate()
                items = gate.draw(self.canvas,x,y)
                items_id=items[0]
            elif self.selected_gate == 'XOR':
                gate = XOR_gate()
                items = gate.draw(self.canvas,x,y)
                items_id=items[0]
            elif self.selected_gate == 'Power':
                gate = Power_gate()
                items = gate.draw(self.canvas,x,y)
                items_id=items[0]
            self.selected_gate = None 
        

root = tk.Tk()
app = DragDropToolbar(root)

app.canvas.bind('<Button-1>', app.on_canvas_click)

root.mainloop()
