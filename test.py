from Tkinter import *
from pprint import *
import time
class FirstTkinter(object):
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master, width=800, height=1000, bg="", colormap="new")
        self.frame.configure(background='gray')
        self.frame.columnconfigure(0, weight=1)
        self.frame.pack()

        self.title = Label(self.frame, text="TIMER APP", justify=CENTER, anchor=N)
        self.title.grid(row=0, column=0, columnspan=4)
        self.title.configure(background='gray')

        self.timer_bar = Canvas(self.frame, width=400, height=100)
        self.timer_bar.grid(row=1, column=0, columnspan=4)
        self.timer_bar.configure(background='white')

        self.set_label = Label(self.frame, text="Set time (minutes):", justify=LEFT, anchor=W)
        self.set_label.grid(row=2, column=0, columnspan=1)
        self.set_label.configure(background='gray')

        self.set_entry = Entry(self.frame)
        self.set_entry.grid(row=2, column=1, columnspan=3)

        self.start_button = Button(self.frame, text="GO!")
        self.start_button.config(command=self.start_timer, background='gray')
        self.start_button.grid(row=3, column=1, columnspan=2)

        self.actual_time_var = StringVar()
        self.actual_time_var.set("0:00")
        self.actual_time = Label(self.frame, textvariable=self.actual_time_var, justify=CENTER, anchor=S)
        self.actual_time.grid(row=4, column=1, columnspan=2)
    def start_timer(self):
        print "In start_timer"
        minutes = self.set_entry.get()
        try:
            new_minutes = float(minutes)
        except ValueError:
            print "Uh oh, not an integer."
            return
        if new_minutes < 0:
            #error
            pass
        if new_minutes == None:
            #error
            pass
        clock_mins = 0
        clock_seconds = 0
        timer_step_px = 400.0 / (new_minutes*60.0)
        print timer_step_px
        canvas_curr_east = 0
        elapsed_minutes = 0
        while elapsed_minutes < new_minutes:
            print "Got to first loop."
            delta_time = 0
            curr_time = time.time()
            while delta_time < 60:
                print "Got to 2nd loop."
                delta_time += time.time() - curr_time
                curr_time = time.time()
                clock_seconds = delta_time
                self.actual_time_var.set("%s:%s" % (str(clock_mins), str(round(clock_seconds, 2))))
                canvas_curr_east += timer_step_px
                print canvas_curr_east
                self.timer_bar.create_rectangle(0, 100, canvas_curr_east, 0, outline='black', fill='purple')
                print "Time is %s:%s" % (str(clock_mins), str(round(clock_seconds, 2)))
                self.master.update_idletasks()
                time.sleep(1)
                #self.actual_time.config(text="%s:%s" % (str(clock_mins), str(clock_seconds)))
            elapsed_minutes += 1
            clock_mins = elapsed_minutes
        self.timer_bar.create_text(100, 25, text="DONE!")
        print "DONE"
        return
root = Tk()
#root.minsize(400,600)
app = FirstTkinter(root)
root.mainloop()




