
import time
import schedule

def my_code():
    print("Welcome to my world")

schedule.every(10).seconds.do(my_code)

while True:
    schedule.run_pending()
    time.sleep(1)

-------------------------------------------

# show windows notification

from win10toast import ToastNotifier

toast = ToastNotifier()
toast.show_toast('Notification', 'Notification body', duration=10, icon_path='icon.ico', threaded=True,)
-------------------------------------------------------------------------------

# show windows notification in specific time

import time
from win10toast import ToastNotifier

toast = ToastNotifier()

notification_time = "2023-08-05 15:21:00"

time_diff = (time.mktime(time.strptime(notification_time, "%Y-%m-%d %H:%M:%S")) - time.time())

time.sleep(time_diff)
toast.show_toast("Notification", "Notification body", duration=20, icon_path="icon.ico", threaded=True,)
-----------------------------------------------------------------------------
# show windows notification every three minutes
import time
from win10toast import ToastNotifier

toast = ToastNotifier()

notification_interval = 3

while True:
    
    notification_time = time.time() + (notification_interval * 60)
    
    time_diff = notification_time - time.time()

    time.sleep(time_diff)
    toast.show_toast("Notification", "Notification body", duration=20, icon_path="icon.ico", threaded=True,)
----------------------------------------------------------------------------
# Show windows notification every 10 secondes

import time
from win10toast import ToastNotifier

toast = ToastNotifier()

notification_interval = 10

while True:
    notification_time = time.time() + notification_interval

    time_diff = notification_time - time.time()

    time.sleep(time_diff)
    toast.show_toast("Notification", "Notification body", duration=20, icon_path="icon.ico", threaded=True,)
'''
