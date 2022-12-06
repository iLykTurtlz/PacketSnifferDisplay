import sys
import Trame
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


class RawData:
	def __init__(self, filename):
		f = open(filename, 'r')
		self.tabTrames = []
		rawInput = ""
		for line in f:	
			offset = line[0:4]
			if (offset == "0000"):
				if rawInput != "":
					self.tabTrames.append(rawInput)
				rawInput=""		
			line = line.lstrip(offset)
			line = line.replace("\n", "")
			line = line.replace(" ", "")
			rawInput += line
		if rawInput != "":
			self.tabTrames.append(rawInput)
		f.close
		
	def printRawData(self):
		for trame in self.tabTrames:
			print(trame+"\n")
	
	def getTrame(self, index):
		return self.tabTrames[index]
