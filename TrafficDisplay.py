from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import *
from Tools import *
from PIL import ImageGrab
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
        self.window.title("Trafic réseau")
        self.rowSize = 40
        self.columnSize = 400
        self.nbRows = self.numberOfFrames + 1
        self.nbColumns = len(self.ipAddresses) 
        self.canvasWidth = self.nbColumns*self.columnSize
        self.canvasHeight = self.nbRows*self.rowSize        
        self.frame = Frame(self.window, width=self.canvasWidth, height=self.canvasHeight)
        self.canvas = Canvas(self.frame, width=self.canvasWidth, height=self.canvasHeight, bg="white", scrollregion=(0,0,self.canvasWidth,self.canvasHeight))
        self.horizScroll = Scrollbar(self.frame, orient=HORIZONTAL)
        self.vertiScroll = Scrollbar(self.frame, orient=VERTICAL)
        self.filterEntryLabel = Label(self.frame, text="Saississez des adresses IP (notation décimal pointée")
        self.filterEntry = Entry(self.frame, width = 40)
        
    def construct(self):
        self.frame.pack(expand=True, fill=BOTH)
        self.horizScroll.pack(side=BOTTOM, fill=X)
        self.horizScroll.config(command=self.canvas.xview)
        self.vertiScroll.pack(side=RIGHT, fill=Y)
        self.vertiScroll.config(command=self.canvas.yview)
        self.filterEntryLabel.pack(side=TOP, anchor=NW)
        self.filterEntry.pack(side=TOP, anchor=NW)
        self.filterEntry.bind('<Return>', self.applyIPFilter)
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
        for frame in self.trames:
            #draw arrows from src to dst
            start = convertIPAddress(frame.ip.srcAddress)
            finish = convertIPAddress(frame.ip.dstAddress)
            startIndex = self.ipAddresses.index(start)
            endIndex = self.ipAddresses.index(finish)
            startCoord = (ipStart+startIndex*self.columnSize, top+rowIndex*self.rowSize)
            endCoord = (ipStart+endIndex*self.columnSize, top+rowIndex*self.rowSize)
            self.canvas.create_line(startCoord[0],startCoord[1],endCoord[0],endCoord[1], arrow=LAST) 
            
            #add port numbers
            if frame.ip.hasTCP:
                if startIndex < endIndex:            
                    self.canvas.create_text(startCoord[0],startCoord[1],text=str_to_int(frame.tcp.srcPort),font=('Helvetica 8'),anchor=SE)    
                    self.canvas.create_text(endCoord[0],endCoord[1],text=str_to_int(frame.tcp.dstPort),font=('Helvetica 8'),anchor=SW)
                else:
                    self.canvas.create_text(startCoord[0],startCoord[1],text=str_to_int(frame.tcp.srcPort),font=('Helvetica 8'),anchor=SW)    
                    self.canvas.create_text(endCoord[0],endCoord[1],text=str_to_int(frame.tcp.dstPort),font=('Helvetica 8'),anchor=SE)
            
            #add line comments
            averageCoord = ((startCoord[0]+endCoord[0])//2,(startCoord[1]+endCoord[1])//2)
            self.canvas.create_text(averageCoord[0],averageCoord[1],text=frame.getHighestLayer().getInfo(),font=('Helvetica 8'),anchor=S)

            rowIndex +=1         
        self.canvas.pack()
       
    def run(self):
        mainloop()

    def save_as_png(self):
        self.file = filedialog.asksaveasfilename(initialdir=".",filetypes=(('PNG File', '.png')))
        self.file = self.file + ".png"
        ImageGrab.grab().save(self.file)

    def saveAs(self):
        #self.file = filedialog.asksaveasfilename(initialdir=".",filetypes(('png','.png')))
        #self.file = self.file + '.png'
        x=self.window.winfo_rootx()+self.frame.winfo_x()+self.canvas.winfo_x()
        y=self.window.winfo_rooty()+self.frame.winfo_y()+self.canvas.winfo_y()
        x1=x+self.canvas.winfo_width()
        y2=y+self.canvas.winfo_height()
        ImageGrab.grab(xdisplay=";0").crop((x,y,x1,y1)).save("example.png")
        
    """
    #ne marche pas
    def generate_pdf(self):
        self.canvas.postscript(file="tmp.ps",colormode='color')
        process=subprocess.Popen(["ps2pdf","tmp.ps","result.pdf"], shell=True)
        process.wait()
        os.remove("tmp.ps")
        self.destroy()
    """
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
        self.canvasWidth = self.nbColumns*self.columnSize
        self.canvasHeight = self.nbRows*self.rowSize        
        self.frame = Frame(self.window, width=self.canvasWidth, height=self.canvasHeight)
        self.canvas = Canvas(self.frame, width=self.canvasWidth, height=self.canvasHeight, bg="white", scrollregion=(0,0,self.canvasWidth,self.canvasHeight))
        self.horizScroll = Scrollbar(self.frame, orient=HORIZONTAL)
        self.vertiScroll = Scrollbar(self.frame, orient=VERTICAL)
        self.filterEntryLabel = Label(self.frame, text="Saississez des adresses IP (notation décimal pointée")
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
        self.canvasWidth = self.nbColumns*self.columnSize
        self.canvasHeight = self.nbRows*self.rowSize        
        self.frame = Frame(self.window, width=self.canvasWidth, height=self.canvasHeight)
        self.canvas = Canvas(self.frame, width=self.canvasWidth, height=self.canvasHeight, bg="white", scrollregion=(0,0,self.canvasWidth,self.canvasHeight))
        self.horizScroll = Scrollbar(self.frame, orient=HORIZONTAL)
        self.vertiScroll = Scrollbar(self.frame, orient=VERTICAL)
        self.filterEntryLabel = Label(self.frame, text="Saississez des adresses IP (notation décimal pointée")
        self.filterEntry = Entry(self.frame, width = 40)
        self.construct()



	
	
	
