from Tools import *

class HTTP:
    def __init__(self, trame, sizeTCP, overheadSize):
        # string of hex
        self.rawHTTP = trame[sizeTCP + overheadSize:]
        
        self.rawASCII = 