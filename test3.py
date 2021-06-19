#prints a given message at given time

from datetime import datetime
from threading import Timer

# name = input("type name: ")
name = input("name:  ")
message = input("message:  ")

x=datetime.today()
y=x.replace(day=x.day+1, hour=20, minute=13, second=30, microsecond=0)
delta_t=y-x
secs=delta_t.seconds+1

def hello_world():
    global name, message
    print(name + message)

t = Timer(secs, hello_world)
t.start()