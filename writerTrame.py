import datetime
import sys

class writerTrame:
    def __init__(self, trame):
        # trame is a Trame
        x=datetime.datetime.now()
        fileOutputName = f'./PrintedTracesFiles/Trace_cree_{x.strftime("%d")}_{x.strftime("%B")}_{x.strftime("%H")}_{x.strftime("%M")}_{x.strftime("%S")}.txt'
        original_stdout = sys.stdout # Save a reference to the original standard output
        try:
            print(f"Trying to create a file.. {fileOutputName}")
            f = open(fileOutputName, 'w')
            sys.stdout = f # Change the standard output to the file we created.
            tmp = trame.getInfo()
            for info in tmp:
                print(info)
            sys.stdout = original_stdout # Reset the standard output to its original value
            f.close()
        except:
            sys.stdout = original_stdout
            print("Writer Error!")