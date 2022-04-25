import os

def ls(arg=None):
    for i in os.listdir("/bin"):
        print(i)

ls()