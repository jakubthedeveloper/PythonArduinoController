import tkinter as tk
import serial

class App:
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyUSB0')
        self.max = 128
        
        root = tk.Tk()
        root.title("Controller")
        root.geometry("240x240")

        s = tk.Scale(root, from_ = self.max, to = 0, command = self.update, showvalue = 0)
        s.pack()
        
        b = tk.Button(root, text = "Set", command = self.send)
        b.pack()

        tk.mainloop()
        self.ser.close()

    def update(self, value):
        self.value = int(value) / self.max
        
    def send(self):
        self.ser.write(str(self.value).encode())

    
app=App()
