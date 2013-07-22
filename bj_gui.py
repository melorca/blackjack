import Tkinter as Tk

class App(Tk.Tk):
    def __init__(self):
        Tk.Tk.__init__(self)
        
        self.dealButton = Tk.Button(self, text = "Deal")
        self.dealButton.pack()
        self.hitButton = Tk.Button(self, text = "Hit")
        self.hitButton.pack()
        self.standButton = Tk.Button(self, text = "Stand")
        self.standButton.pack()
        
        self.canvas = Tk.Canvas(self, width = 400, height = 400)
        self.canvas.create_rectangle(0, 0, 400, 400, fill = "green")
        self.canvas.pack()
        
        self.T = self.canvas.create_text(200,200)
        self.P = self.canvas.create_text(200,100)
        self.D = self.canvas.create_text(200,300)
        self.S = self.canvas.create_text(350,350)

