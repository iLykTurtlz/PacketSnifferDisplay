from tkinter import *
from tkinter.ttk import *

class TrafficDisplay:

    def __init__(self, traffic):
        self.numberOfFrames = len(traffic.trames)
        ips = traffic.getDistinctIpAddresses()
        self.ipAddresses = [f"{int(a[0:2],16)}.{int(a[2:4],16)}.{int(a[4:6],16)}.{int(a[6:8],16)}" for a in ips]
        self.numberOfIPAddresses = len(self.ipAddresses)
        self.window = Tk()
        self.window.title("Trafic réseau")
        self.nbRows = self.numberOfFrames + 1
        self.nbColumns = len(self.ipAddresses)*3 + 2
        
    def construct(self):
        first = 1
        for i in range(1,10):
            Label(self.window, text="timestamp").grid(row=i, column = 0)
        for addr in self.ipAddresses:
            Label(self.window, text=addr).grid(row=0, column=first, columnspan=2)
            Separator(self.window, orient=VERTICAL).grid(row=1, column = first, rowspan=9, sticky='ns')
            first += 3
       
    def run(self):
        mainloop()
        
	
	
	
	
