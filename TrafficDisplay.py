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
        self.rowSize = 40
        self.columnSize = 160
        self.nbRows = self.numberOfFrames + 1
        self.nbColumns = len(self.ipAddresses) + 2
        self.canvasWidth = self.nbColumns*self.columnSize
        self.canvasHeight = self.nbRows*self.rowSize
        self.frame = Frame(self.window, width=self.canvasWidth, height=self.canvasHeight)
        self.canvas = Canvas(self.frame, width=self.canvasWidth, height=self.canvasHeight, bg="white", scrollregion=(0,0,self.canvasWidth,self.canvasHeight))
        self.horizScroll = Scrollbar(self.frame, orient=HORIZONTAL)
        self.vertiScroll = Scrollbar(self.frame, orient=VERTICAL)
        
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
        
        self.frame.pack(expand=True, fill=BOTH)
        self.horizScroll.pack(side=BOTTOM, fill=X)
        self.horizScroll.config(command=self.canvas.xview)
        self.vertiScroll.pack(side=RIGHT, fill=Y)
        self.vertiScroll.config(command=self.canvas.yview)
        self.canvas.config(width=self.canvasWidth,height=self.canvasHeight)
        self.canvas.config(xscrollcommand=self.horizScroll.set, yscrollcommand=self.vertiScroll.set)
        #self.window.geometry(f"{self.canvasWidth}x{self.canvasHeight}")
        ipStart = 100
        ipIndex=0
        top = 15    #hardcoded, should be right beneath the IP addresses
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
            startCoord = (ipStart+startIndex*self.columnSize, top+rowIndex*self.rowSize)
            endCoord = (ipStart+endIndex*self.columnSize, top+rowIndex*self.rowSize)
            self.canvas.create_line(startCoord[0],startCoord[1],endCoord[0],endCoord[1], arrow=LAST) 
            if frame.ip.hasTCP:
                if startIndex < endIndex:            
                    self.canvas.create_text(startCoord[0],startCoord[1],text=str_to_int(frame.tcp.srcPort),anchor=SE)    
                    self.canvas.create_text(endCoord[0],endCoord[1],text=str_to_int(frame.tcp.dstPort),anchor=SW)
                else:
                    self.canvas.create_text(startCoord[0],startCoord[1],text=str_to_int(frame.tcp.srcPort),anchor=SW)    
                    self.canvas.create_text(endCoord[0],endCoord[1],text=str_to_int(frame.tcp.dstPort),anchor=SE)
            
            rowIndex +=1           
        self.canvas.pack()
               
       
       
       
    def run(self):
        mainloop()

        
	
	
	
	
