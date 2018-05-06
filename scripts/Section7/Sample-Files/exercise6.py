import datetime
import os
import glob2

filename=datetime.datetime.now()
filename=filename.strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt"

with open(filename,'w') as filetobecreated:
    for i in glob2.glob('file*'):   # this is a third party library which is installed and imported. It lets pull the list of files from a dir with a selection.
        with open(i,'r') as file:
            filetobecreated.write(file.read()+"\n")
