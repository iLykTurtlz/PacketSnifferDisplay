import datetime

class writer:
    def __init__(self, infos, name):
        # infos is an array type that prints the objects inside it
        x=datetime.datetime.now()
        print (x.strftime("%x"))
        
        
w = writer([], "")