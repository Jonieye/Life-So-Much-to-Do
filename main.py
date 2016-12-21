from Tkinter import *
from datetime import datetime
from threading import Timer
from time import sleep

#cur_time = StringVar()
cur_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Controller(object):
    def __init__(self, master):
        self._master = master
        self._master.protocol("WM_DELETE_WINDOW", self.closing)
        
        self._model = Model(self)
        self._view = View(self._master)

    def closing(self):
        self._view.close()
        self._master.destroy()

class View(object):
    def __init__(self, master):
        self._master = master
        self.window_config()
        self._timeframe = TimeFrame(self._master)
        self._e1 = Entry(self._master)
        self._e1.pack()
        

    def window_config(self):
        self._master.title("Life - a heck of a game")
        self._master.minsize(900,500)

    def close(self):
        self._timeframe.close()

class TimeFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self._label1 = Label(self, text = cur_time)
        self.pack(expand = True, fill = BOTH)
        self._label1.pack()

        self._timeupdate = RepeatedTimer(1,self.timeupdate)

    def timeupdate(self):
        cur_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._label1.config(text = cur_time)

    def close(self):
        self._timeupdate.stop()

class Model:
    def __init__(self, controller):
        self._controller = controller

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self._interval = interval
        self._function = function
        self._args = args
        self._kwargs = kwargs
        self._is_running = False
        self.start()

    def _run(self):
        self._is_running = False
        self.start()
        self._function(*self._args, **self._kwargs)
        
    def start(self):
        if not self._is_running:
            self._timer = Timer(self._interval, self._run)
            self._timer.start()
            self._is_running = True

    def stop(self):
        self._timer.cancel()
        self._is_running = False

        
        
if __name__ == "__main__":
    root = Tk()
    controller = Controller(root)
    root.mainloop()
    
