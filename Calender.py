from tkinter import*
import calendar

# function for showing the calender of the given year
def showCal():
    
    # Create a GUI window
    root=Tk()

    # Set the background colour of GUI window
    root.config(background="white")

    # Set the name of tkinter GUI window
    root.title("CALENDER")

    # Set the configuration of GUI window
    root.geometry("550x600")

    # Get method returns current text as a string
    fetch_year=int(year_field.get())

    # Calender method of calender module return
    # The calender of the given year
    cal_content=calendar.calendar(fetch_year)

    # Create a label for showing the content of the calender
    cal_year=Label(root,text=cal_content,font="Consolas 10 bold")

    # Grid method is used for placing 
    # The widgets at respective positions
    # In the label
    cal_year.grid(row=5,column=1,padx=20)

    #Start the GUI
    root.mainloop()

# Driver Code
if __name__=="main_":

    # Create a GUI window
    gui=Tk()

    # Set the background colour of GUI window 
    gui.config(background="white")

    # Set the name of tkinter GUI window 
    gui.title("CALENDER")

    # Set the configration of GUI window
    gui.geometry("250x140")

    # Create a CALENDER :label with specified font and size
    cal=Label(gui,text="CALENDER",bg="dark gray",font=("times",28,'bold'))

    # Createa Enter Year:label
    year=Label(gui,text="Enter year",bg="light green")

    # Create a text entry box for filling or typing the information
    year_field=Entry(gui)

    # Create a show Calender Button and attached to the showCal function
    Show=Button(gui,text="Show Calender",fg="Black",bg="Red",command=showCal)

    # Create a Exit Button and attached to exit function
    Exit=Button(gui,text="Exit",fg="Black",bg="Red",command=exit)

    # Grid method is used for placing
    # The widget at respective positions
    # In table like structure.
    cal.grid(row=1,column=1)

    year.grid(row=2,column=1)

    year_field.grid(row=3,column=1)
    
    Show.grid(row=4,column=1)
    Exit.grid(row=6,column=1)

    # Start the GUI 
    gui.mainloop()