from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import *
from Tools import *
# from PIL import ImageGrab
#import subprocess #for the pdf saver that doesn't work
#import os


class TrafficDisplay:

    def __init__(self, traffic):
        self.traffic=traffic
        ips = traffic.getDistinctIpAddresses()
        self.ipAddresses = [convertIPAddress(a) for a in ips]
        self.trames = self.traffic.trames
        self.numberOfFrames = len(self.trames)
        self.numberOfIPAddresses = len(self.ipAddresses)
        self.window = Tk()
        self.window.geometry("1000x700")
        self.window.title("Trafic réseau")
        self.rowSize = 20
        self.columnSize = 110
        self.commentSize = 500
        self.nbRows = self.numberOfFrames + 1
        self.nbColumns = len(self.ipAddresses) 
        self.commentStart = (self.nbColumns+1)*self.columnSize
        self.canvasWidth = (self.nbColumns+1)*self.columnSize+self.commentSize
        self.canvasHeight = self.nbRows*self.rowSize        
        self.frame = Frame(self.window, width=self.canvasWidth, height=self.canvasHeight)
        self.canvas = Canvas(self.frame, width=self.canvasWidth, height=self.canvasHeight, bg="white", scrollregion=(0,0,self.canvasWidth,self.canvasHeight))
        self.horizScroll = Scrollbar(self.frame, orient=HORIZONTAL)
        self.vertiScroll = Scrollbar(self.frame, orient=VERTICAL)
        self.filterEntryLabel = Label(self.frame, text="Saississez des adresses IP (séparées par des ||)")
        self.filterEntry = Entry(self.frame, width = 40)
        #self.protocolFilterEntryLabel = Label(self.frame, text="Sélectionnez un protocole")
        self.options = [
            "Aucun filtre",
            "IP",
            "TCP",
            "HTTP"
        ]
        self.protocol = StringVar()
        self.protocol.set(self.options[0])
        self.dropDown = OptionMenu(self.frame, self.protocol, *self.options, command=self.applyProtocolFilter)


        

        
    def construct(self):
        self.frame.pack(expand=True, fill=BOTH)
        self.horizScroll.pack(side=BOTTOM, fill=X)
        self.horizScroll.config(command=self.canvas.xview)
        self.vertiScroll.pack(side=RIGHT, fill=Y)
        self.vertiScroll.config(command=self.canvas.yview)
        self.filterEntryLabel.pack(side=TOP, anchor=NW)
        self.filterEntry.pack(side=TOP, anchor=NW)
        self.filterEntry.bind('<Return>', self.applyIPFilter)
        #self.protocolFilterEntryLabel.pack(side=TOP,anchor=NE)
        self.protocol = StringVar()
        self.protocol.set(self.options[0])
        self.dropDown = OptionMenu(self.frame, self.protocol, *self.options, command=self.applyProtocolFilter)

        self.dropDown.pack()
        #self.dropDown.bind('<<ComboboxSelected>>', self.applyProtocolFilter)
        self.canvas.config(width=self.canvasWidth,height=self.canvasHeight)
        self.canvas.config(xscrollcommand=self.horizScroll.set, yscrollcommand=self.vertiScroll.set)
        self.canvas.bind("<Button 1>",self.displayInfo)
        #self.window.geometry(f"{self.canvasWidth}x{self.canvasHeight}")
        ipStart = 100
        ipIndex=0
        self.top = 15    #hardcoded, should be right beneath the IP addresses
        bottom = self.canvasHeight
        
        for addr in self.ipAddresses:
            self.canvas.create_text(ipStart+ipIndex*self.columnSize,10, text=addr, fill='black', font=('Helvetica 8'), justify=CENTER)
            self.canvas.create_line(ipStart+ipIndex*self.columnSize,self.top,ipStart+ipIndex*self.columnSize,bottom, fill="#B5B5B5")
            ipIndex += 1
        rowIndex=1
        for frame in self.trames:
            #draw arrows from src to dst
            start = convertIPAddress(frame.ip.srcAddress)
            finish = convertIPAddress(frame.ip.dstAddress)
            startIndex = self.ipAddresses.index(start)
            endIndex = self.ipAddresses.index(finish)
            startCoord = (ipStart+startIndex*self.columnSize, self.top+rowIndex*self.rowSize)
            endCoord = (ipStart+endIndex*self.columnSize, self.top+rowIndex*self.rowSize)
            self.canvas.create_line(startCoord[0],startCoord[1],endCoord[0],endCoord[1], arrow=LAST) 
            
            #add port numbers
            if frame.ip.hasTCP:
                if startIndex < endIndex:            
                    self.canvas.create_text(startCoord[0],startCoord[1],text=str_to_int(frame.tcp.srcPort),font=('Helvetica 8'),fill='black',anchor=SE)    
                    self.canvas.create_text(endCoord[0],endCoord[1],text=str_to_int(frame.tcp.dstPort),font=('Helvetica 8'),fill='black',anchor=SW)
                else:
                    self.canvas.create_text(startCoord[0],startCoord[1],text=str_to_int(frame.tcp.srcPort),font=('Helvetica 8'),fill='black',anchor=SW)    
                    self.canvas.create_text(endCoord[0],endCoord[1],text=str_to_int(frame.tcp.dstPort),font=('Helvetica 8'),fill='black',anchor=SE)
            
            #add line comments
            averageCoord = ((startCoord[0]+endCoord[0])//2,(startCoord[1]+endCoord[1])//2)
            self.canvas.create_text(averageCoord[0],averageCoord[1],text=frame.getHighestLayer().getShortInfo(),font=('Helvetica 8'),fill='black',anchor=S)

            #add right-side comments
            self.canvas.create_text(self.commentStart,startCoord[1],text=frame.getHighestLayer().getInfo(),font=('Helvetica 8'), fill='black',anchor=SW)
            rowIndex +=1         
        self.canvas.pack()
       
    def run(self):
        mainloop()

   
    def applyProtocolFilter(self, event):
        p = self.protocol.get()
        self.trames=[x for x in self.traffic.trames if x.has(p)]
        ips = set()
        for frame in self.trames:
            ips.add(frame.ip.srcAddress)
            ips.add(frame.ip.dstAddress)
        self.ipAddresses=[convertIPAddress(a) for a in ips]
        self.numberOfFrames = len(self.trames)
        self.numberOfIPAddresses = len(self.ipAddresses)
        self.frame.destroy()
        self.nbRows = self.numberOfFrames + 1
        self.nbColumns = self.numberOfIPAddresses 
        self.commentStart = (self.nbColumns+1)*self.columnSize
        self.canvasWidth = (self.nbColumns+1)*self.columnSize+self.commentSize
        self.canvasHeight = self.nbRows*self.rowSize        
        self.frame = Frame(self.window, width=self.canvasWidth, height=self.canvasHeight)
        self.canvas = Canvas(self.frame, width=self.canvasWidth, height=self.canvasHeight, bg="white", scrollregion=(0,0,self.canvasWidth,self.canvasHeight))
        self.horizScroll = Scrollbar(self.frame, orient=HORIZONTAL)
        self.vertiScroll = Scrollbar(self.frame, orient=VERTICAL)
        self.filterEntryLabel = Label(self.frame, text="Saississez des adresses IP (séparées par des ||)")
        self.filterEntry = Entry(self.frame, width = 40)
        self.construct()


    def applyIPFilter(self,event):
        ips = self.filterEntry.get()
        #if "&&" not in.... but that doesn't make sense
        ipList = ips.split("||")
        addySet = {x.lstrip().rstrip() for x in ipList if x != ""}
        if len(addySet) == 0:
            messagebox.showerror("Erreur","Vous n'avez pas saisi d'adresse IP")
            return
        starter_ips = self.traffic.getDistinctIpAddresses()
        self.ipAddresses = [convertIPAddress(a) for a in starter_ips]
        for addy in addySet:
            if addy not in self.ipAddresses:
                messagebox.showerror("Erreur", "Vous avez saisi une adresse IP non présente dans le flux")
                self.resetFilters()
                return
        self.trames = [x for x in self.traffic.trames if convertIPAddress(x.ip.srcAddress) in addySet or convertIPAddress(x.ip.dstAddress) in addySet]
        for frame in self.trames:
            addySet.add(convertIPAddress(frame.ip.srcAddress))
            addySet.add(convertIPAddress(frame.ip.dstAddress))
        self.ipAddresses = [x for x in addySet]
        #elif "&&" in ips and "||" not in ips:    
        #    ipList = ips.split("&&")
        #    self.ipAddresses = [x.lstrip().rstrip() for x in ipList if x != ""]
        #    self.trames = [x for x in self.traffic.trames if convertIPAddress(x.ip.srcAddress) in self.ipAddresses and convertIPAddress(x.ip.dstAddress) in self.ipAddresses]
        self.numberOfFrames = len(self.trames)
        self.numberOfIPAddresses = len(self.ipAddresses)
        self.frame.destroy()
        self.nbRows = self.numberOfFrames + 1
        self.nbColumns = self.numberOfIPAddresses 
        self.canvasWidth = (self.nbColumns+1)*self.columnSize+self.commentSize
        self.canvasHeight = self.nbRows*self.rowSize  
        self.commentStart = (self.nbColumns+1)*self.columnSize      
        self.frame = Frame(self.window, width=self.canvasWidth, height=self.canvasHeight)
        self.canvas = Canvas(self.frame, width=self.canvasWidth, height=self.canvasHeight, bg="white", scrollregion=(0,0,self.canvasWidth,self.canvasHeight))
        self.horizScroll = Scrollbar(self.frame, orient=HORIZONTAL)
        self.vertiScroll = Scrollbar(self.frame, orient=VERTICAL)
        self.filterEntryLabel = Label(self.frame, text="Saississez des adresses IP (séparées par des ||)")
        self.filterEntry = Entry(self.frame, width = 40)
        self.construct()

    def resetFilters(self):
        ips = self.traffic.getDistinctIpAddresses()
        self.ipAddresses = [convertIPAddress(a) for a in ips]
        self.trames = self.traffic.trames
        self.numberOfFrames = len(self.trames)
        self.numberOfIPAddresses = len(self.ipAddresses)
        self.frame.destroy()
        self.nbRows = self.numberOfFrames + 1
        self.nbColumns = self.numberOfIPAddresses 
        self.commentStart = (self.nbColumns+1)*self.columnSize
        self.canvasWidth = (self.nbColumns+1)*self.columnSize+self.commentSize
        self.canvasHeight = self.nbRows*self.rowSize        
        self.frame = Frame(self.window, width=self.canvasWidth, height=self.canvasHeight)
        self.canvas = Canvas(self.frame, width=self.canvasWidth, height=self.canvasHeight, bg="white", scrollregion=(0,0,self.canvasWidth,self.canvasHeight))
        self.horizScroll = Scrollbar(self.frame, orient=HORIZONTAL)
        self.vertiScroll = Scrollbar(self.frame, orient=VERTICAL)
        self.filterEntryLabel = Label(self.frame, text="Saississez des adresses IP (séparées par des ||)")
        self.filterEntry = Entry(self.frame, width = 40)
        self.construct()

    def displayInfo(self,event):
        c = event.widget
        x=c.canvasx(event.x)
        y=c.canvasy(event.y)
        clickCoord = (x,y)
        i=int(  (clickCoord[1]-self.top)/self.rowSize  )
        infoBrut = self.trames[i].getInfo()
        info = ""
        for line in infoBrut:
            info += line + "\n"
        self.popup = Toplevel()
        self.popup.title(self.trames[i].getHighestLayer().getShortInfo())
        self.infoLabel = Text(self.popup)
        self.infoLabel.insert(END, info)
        width = self.infoLabel.winfo_width()
        height = self.infoLabel.winfo_height()
        self.popupHScroll = Scrollbar(self.popup, orient=HORIZONTAL)
        self.popupHScroll.pack(side=BOTTOM, fill=X)
        self.popupVScroll = Scrollbar(self.popup, orient=VERTICAL)
        self.popupVScroll.pack(side=RIGHT, fill=Y)
        #self.infoLabel.configure(xscrollcommand=self.popupHScroll.set, yscrollcommand=self.popupVScroll.set)
        self.infoLabel.pack()
        self.popupHScroll.config(command=self.infoLabel.xview)
        self.popupVScroll.config(command=self.infoLabel.yview)
        self.canvas.bind("<Button 1>",self.displayInfo)





	
	
	
