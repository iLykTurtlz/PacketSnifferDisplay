from tkinter import *
from tkinter.ttk import *

class TrafficDisplay:

    def __init__(self, traffic):
        self.numberOfFrames = len(traffic.trames)
        self.ipAddresses = traffic.getDistinctIpAddresses()
        self.numberOfIPAddresses = len(self.ipAddresses)
        self.window = Tk()
        self.window.title("Trafic réseau")
	
	
	
	
