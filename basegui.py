import tkinter as tk
from andgate import AND_gate
from orgate import OR_gate
from notgate import NOT_gate
from nandgate import NAND_gate
from norgate import NOR_gate
from xorgate import XOR_gate
from powersource import Power_Source
from wire import Wire

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
        self.add_gate_button('Wire', self.toolbar)


        
        self.selected_gate = None
        self.selected_wire = None 
        self.gate_objects = {}

    def connect_wire_to_power(self, wire, power_source):
        power_source.connect_wire(wire)

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
                power_source = Power_Source()
                power_source.draw(self.canvas, x, y)
                self.gate_objects[power_source] = (x, y)
            if self.selected_gate == "Wire":
                new_wire = Wire(self.canvas, None, None, (event.x, event.y), None)
                new_wire.draw(event.x, event.y)
                self.selected_wire = new_wire 
                self.selected_gate = None
            elif self.selected_wire is not None:
                clicked_object = self.canvas.find_withtag("current")
                for obj, (x, y) in self.gate_objects.items():
                    if hasattr(obj, 'button_id') and obj.button_id == clicked_object[0]:
                        self.connect_wire_to_power(self.selected_wire, obj)
                        self.selected_wire = None
                        break 

            clicked_item = self.canvas.find_closest(event.x, event.y)
            for obj, (x, y) in self.gate_objects.items():
                if isinstance(obj, Wire):
                    if clicked_item == obj.start_button:  
                        obj.select()
                    elif self.selected_wire and clicked_item == obj.end_button:
                        obj.deselect()
                elif isinstance(obj, Power_Source):
                    if self.selected_wire: 
                        obj.connect_wire(self.selected_wire)
                        self.selected_wire = None

    def select_wire(self, wire):
        if self.selected_wire == wire:
            wire.deselect()
            self.selected_wire = None
        else:
            if self.selected_wire is not None:
                self.selected_wire.deselect()
            self.selected_wire = wire
            wire.select()
    
    def on_power_source_click(self, power_source):
        for wire in self.wire_objects:  
            if wire.selected:
                power_source.connect_wire(wire)
                break  
        

root = tk.Tk()
app = DragDropToolbar(root)

app.canvas.bind('<Button-1>', app.on_canvas_click)

root.mainloop()
