import tkinter as tk

# Creating a new tkinter window
master=tk.Tk()

# Assigning a title
master.title("Marksheet")

# Specifying geometry for window size
master.geometry("700x250")

# Declaring objects for entering data
e1=tk.Entry(master)
e2=tk.Entry(master)
e3=tk.Entry(master)
e4=tk.Entry(master)
e5=tk.Entry(master)
e6=tk.Entry(master)
e7=tk.Entry(master)

# Function to display the total subjects
# Credits total credits and SGPA according
# to grades entered
def display():

    # Variable to store total marks
    tot=0

    # 10*number of subject credits
    # Give total credits for grade A
    if e4.get()=='A':

        # Grid method is used for placing
        # The widget at respective positions 
        # In table like structure
        tk.Label(master,text="40").grid(row=3,column=4)
        tot+=40
    # 9*number of subjects credits give
    # Total credits for grade B
    if e4.get()=="B":
        tk.Label(master,text="36").grid(row=3,column=4)
        tot+=36

    # 8*number of subjects credits give
    # Total credits for grade C
    if e4.get()=="C":
        tk.Label(master,text="32").grid(row=3,column=4)
        tot+=32

    # 7*number of subjects credits give
    # Total credits for grade D
    if e4.get()=="D":
        tk.Label(master,text="28").grid(row=3,column=4)
        tot+=28

    # 6*number of subjects credits give
    # Total credits for grade P
    if e4.get()=="P":
        tk.Label(master,text="24").grid(row=3,column=4)
        tot+=24

    # 0*number of subjects credits give
    # Total credits for grade F
    if e4.get()=="F":
        tk.Label(master,text="0").grid(row=3,column=4)
        tot+=0

    # Similarly doing with other subjects
    if e5.get()=="A":
        tk.Label(master,text="40").grid(row=4,column=4)
        tot+=40
    if e5.get()=="B":
        tk.Label(master,text="36").grid(row=4,column=4)
        tot+=36
    if e5.get()=="C":
        tk.Label(master,text="32").grid(row=4,column=4)
        tot+=32
    if e5.get()=="D":
        tk.Label(master,text="28").grid(row=4,column=4)
        tot+=28
    if e5.get()=="P":
        tk.Label(master,text="24").grid(row=4,column=4)
        tot+=24
    if e5.get()=="F":
        tk.Label(master,text="0").grid(row=4,column=4)
        tot+=0
    
    if e6.get()=="A":
        tk.Label(master,text="30").grid(row=5,column=4)
        tot+=30
    if e6.get()=="B":
        tk.Label(master,text="27").grid(row=5,column=4)
        tot+=27
    if e6.get()=="C":
        tk.Label(master,text="24").grid(row=5,column=4)
        tot+=24
    if e6.get()=="D":
        tk.Label(master,text="21").grid(row=5,column=4)
        tot+=21
    if e6.get()=="P":
        tk.Label(master,text="24").grid(row=5,column=4)
        tot+=24
    if e6.get()=="F":
        tk.Label(master,text="0").grid(row=5,column=4)
        tot+=0
    
    if e7.get()=="A":
        tk.Label(master,text="40").grid(row=6,column=4)
        tot+=40
    if e7.get()=="B":
        tk.Label(master,text="36").grid(row=6,column=4)
        tot+=36
    if e7.get()=="C":
        tk.Label(master,text="32").grid(row=6,column=4)
        tot+=32
    if e7.get()=="D":
        tk.Label(master,text="28").grid(row=6,column=4)
        tot+=28
    if e7.get()=="P":
        tk.Label(master,text="24").grid(row=6,column=4)
        tot+=24
    if e7.get()=="F":
        tk.Label(master,text="0").grid(row=6,column=4)
        tot+=0

    # To display total credits
    tk.Label(master,text=str(tot)).grid(row=7,column=4)

    # To display SGPA
    tk.Label(master,text=str(tot/15)).grid(row=8,column=4)

# End of display function

# Label to Enter name 
tk.Label(master,text="Name").grid(row=0,column=0)
# Label for Registration number
tk.Label(master,text="Reg.No").grid(row=0,column=3)
# Label for Roll Number
tk.Label(master,text="Roll.No").grid(row=1,column=0)

# Labels for Serial numbers
tk.Label(master,text="Srl.No").grid(row=2,column=0)
tk.Label(master,text="1").grid(row=3,column=0)
tk.Label(master,text="2").grid(row=4,column=0)
tk.Label(master,text="3").grid(row=5,column=0)
tk.Label(master,text="4").grid(row=6,column=0)

# Label for subject codes
tk.Label(master,text="Subject").grid(row=2,column=1)
tk.Label(master,text="CS 201").grid(row=3,column=1)
tk.Label(master,text="CS 202").grid(row=4,column=1)
tk.Label(master,text="MA 201").grid(row=5,column=1)
tk.Label(master,text="EC 201").grid(row=6,column=1)

# Label for grades
tk.Label(master,text="Grade").grid(row=2,column=2)
e4.grid(row=3,column=2)
e5.grid(row=4,column=2)
e6.grid(row=5,column=2)
e7.grid(row=6,column=2)

# Label for subject credit
tk.Label(master,text="Sub Credit").grid(row=2,column=3)
tk.Label(master,text="4").grid(row=3,column=3)
tk.Label(master,text="4").grid(row=4,column=3)
tk.Label(master,text="3").grid(row=5,column=3)
tk.Label(master,text="4").grid(row=6,column=3)

tk.Label(master,text="Credit obtained").grid(row=2,column=4)

# Taking Entries of name,reg,rollno respectively
e1=tk.Entry(master)
e2=tk.Entry(master)
e3=tk.Entry(master)

# Organizing them in the grid
e1.grid(row=0,column=1)
e2.grid(row=0,column=4)
e3.grid(row=1,column=1)

# Button to display all the calculated credit scores and SGPA
button1=tk.Button(master,text="Submit",bg="green",command=display)
button1.grid(row=8,column=1)

tk.Label(master,text="Total Credit").grid(row=7,column=3)
tk.Label(master,text="SGPA").grid(row=8,column=3)

master.mainloop()

# This marksheet can be snapshooted and printed out
# as a report card for the semester












    



















