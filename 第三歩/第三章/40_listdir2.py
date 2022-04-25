import os

def ls(arg=None):
    for i in os.listdir():
        print(i)
    
ls()