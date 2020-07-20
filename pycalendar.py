# tkinter import
from tkinter import *
# calender import module 
import calendar
# tkinter initialize 
root = Tk()
# GUI title 
root.title("GUI Calender")
# calender year which is to be shown on GUI
year = 2020
# storing 2020 year calender data inside variable myCal
myCal = calendar.calendar(year)
# showing calender data using a labeled widget
cal_year = Label(root, text=myCal, font="times new roman 10 bold")
# packaging label widget 
cal_year.pack()
# running the program in ready state 
root.mainloop()
