from datetime import datetime
from threading import Timer

# name = input("type name: ")
name = input("name:  ")
name1 = input("name1:  ")

x=datetime.today()
y=x.replace(day=x.day+1, hour=20, minute=13, second=30, microsecond=0)
delta_t=y-x
secs=delta_t.seconds+1

def hello_world():
    global name, name1
    print(name + name1)

t = Timer(secs, hello_world)
t.start()