import datetime
import sys

class writer:
    def __init__(self, infos):
        # infos is an array type that prints the objects inside it
        x=datetime.datetime.now()
        fileOutputName = f'{x.strftime("%x")}_{x.strftime("%X")}'
        original_stdout = sys.stdout # Save a reference to the original standard output
        with open(fileOutputName, 'a') as f:
            sys.stdout = f # Change the standard output to the file we created.
            
            
            
            
            
            
            sys.stdout = original_stdout # Reset the standard output to its original value