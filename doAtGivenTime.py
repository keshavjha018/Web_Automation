#The following program, perform a set of tasks at a given time (each day) 

from datetime import datetime
from threading import Timer

x=datetime.today()
y=x.replace(day=x.day+1, hour=19, minute=26, second=5, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def hello_world():
    print ("hello world")

t = Timer(secs, hello_world)
t.start()




#  in order to detect if the day of the month must be reset due to the reaching 
# #of the end of the month, the definition of y in this context shall be the following:

# y = x.replace(day=x.day, hour=1, minute=0, second=0, microsecond=0) + timedelta(days=1)

# With this fix, it is also needed to add timedelta to the imports. The other code lines 
# maintain the same. The full solution, using also the total_seconds() function, is therefore:

# from datetime import datetime, timedelta
# from threading import Timer

# x=datetime.today()
# y = x.replace(day=x.day, hour=1, minute=0, second=0, microsecond=0) + timedelta(days=1)
# delta_t=y-x

# secs=delta_t.total_seconds()

# def hello_world():
#     print "hello world"
#     #...

# t = Timer(secs, hello_world)
# t.start()

# link
#   https://stackoverflow.com/questions/15088037/python-script-to-do-something-at-the-same-time-every-day