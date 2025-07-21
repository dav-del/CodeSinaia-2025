# import pandas as pd

global count 
count = 5

def func():
    global count
    count=7
    return count

func()

print(count)