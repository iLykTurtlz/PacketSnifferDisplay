from tkinter import *
from tkinter.ttk import *
from Tools import *

class TrafficDisplay:

    def __init__(self, traffic):
        self.traffic=traffic
        self.numberOfFrames = len(traffic.trames)
        ips = traffic.getDistinctIpAddresses()
        self.ipAddresses = [convertIPAddress(a) for a in ips]
        self.numberOfIPAddresses = len(self.ipAddresses)
        self.window = Tk()
        self.window.title("Trafic réseau")
        self.rowSize = 80
        self.columnSize = 160
        self.nbRows = self.numberOfFrames + 1
        self.nbColumns = len(self.ipAddresses)*3 + 2
        self.canvasWidth = self.nbColumns*self.columnSize
        self.canvasHeight = self.nbRows*self.rowSize
        self.canvas = Canvas(self.window, width=self.canvasWidth, height=self.canvasHeight, bg="white")
        self.rightScrollbar = Scrollbar()
        
    def construct(self):
        """
        first = 1
        for i in range(1,10):
            Label(self.window, text="timestamp").grid(row=i, column = 0)
        for addr in self.ipAddresses:
            Label(self.window, text=addr).grid(row=0, column=first, columnspan=2)
            Separator(self.window, orient=VERTICAL).grid(row=1, column = first, rowspan=9, sticky='ns')
            first += 3
        rowIndex=1
        for frame in self.traffic.trames:
        	
        	start = convertIPAddress(frame.ip.srcAddress)
            finish = convertIPAddress(frame.ip.dstAddress)
            startIndex = self.ipAddresses.index(start)
            endIndex = self.ipAddresses.index(finish)
            if startIndex > endIndex:
            	canvas = Canvas(window, bg="white")
                canvas.create_line(ipStart+startIndex*self.columnSize,top+rowIndex*self.rowSize,ipStart+endIndex*self.columnSize,top+rowIndex*self.rowSize, arrow=FIRST) 
                canvas.grid()
            else:
                canvas.create_line(ipStart+startIndex*self.columnSize,top+rowIndex*self.rowSize,ipStart+endIndex*self.columnSize,top+rowIndex*self.rowSize, arrow=LAST)       
        		canvas.grid()
        """        	
        
        
        self.window.geometry(f"{self.canvasWidth}x{self.canvasHeight}")
        ipStart = 100
        ipIndex=0
        top = 15
        bottom = self.canvasHeight
        
        for addr in self.ipAddresses:
            self.canvas.create_text(ipStart+ipIndex*self.columnSize,10, text=addr, fill="black", font=('Helvetica 8'), justify=CENTER)
            self.canvas.create_line(ipStart+ipIndex*self.columnSize,top,ipStart+ipIndex*self.columnSize,bottom)
            ipIndex += 1
        rowIndex=1
        for frame in self.traffic.trames:
            start = convertIPAddress(frame.ip.srcAddress)
            finish = convertIPAddress(frame.ip.dstAddress)
            startIndex = self.ipAddresses.index(start)
            endIndex = self.ipAddresses.index(finish)
            if startIndex > endIndex:
                self.canvas.create_line(ipStart+startIndex*self.columnSize,top+rowIndex*self.rowSize,ipStart+endIndex*self.columnSize,top+rowIndex*self.rowSize, arrow=FIRST) 
            else:
                self.canvas.create_line(ipStart+startIndex*self.columnSize,top+rowIndex*self.rowSize,ipStart+endIndex*self.columnSize,top+rowIndex*self.rowSize, arrow=LAST)
                       
        self.canvas.pack()
               
       
       
       
    def run(self):
        mainloop()

        
	
	
	
	
