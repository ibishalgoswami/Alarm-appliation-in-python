import time
from win10toast import ToastNotifier
#def rem():

#rem()
class inperror(Exception):
    def __init__(self, msg):
        self.msg = msg


inptime = input('Enter the input time in the given format hh-mm-ss')
res = inptime.split("-")
inptext = input("What do you want to be remained?")
# start=int(time.time())+inptime

try:
    if len(res) == 3:
        H = int(res[0])
        M = int(res[1])
        S = int(res[2])
        if H > 24:
            try:
                raise inperror("Please Provide the correct time")
            except inperror as e:
                print(e.msg)

        elif M > 60:
            try:
                raise inperror("Please Provide the correct time")
            except inperror as e:
                print(e.msg)
        else:
            while True:
                if int(time.localtime().tm_hour) == H and int(time.localtime().tm_min) == M and int(
                        time.localtime().tm_sec) == S:
                    notifier = ToastNotifier()
                    notifier.show_toast("Hello", inptext, duration=12)
                    break

    else:
        H = int(res[0])
        M = int(res[1])
        S = None
        if H > 24:
            try:
                raise inperror("Please Provide the correct time")
            except inperror as e:
                print(e.msg)

        elif M > 60:
            try:
                raise inperror("Please Provide the correct time")
            except inperror as e:
                print(e.msg)
        else:
            while True:
                if int(time.localtime().tm_hour) == H and int(time.localtime().tm_min) == M:
                    notifier = ToastNotifier()
                    notifier.show_toast("Your Alarm", inptext, duration=12)
                    break

except:
    print("Provide the time in the correct input format")
