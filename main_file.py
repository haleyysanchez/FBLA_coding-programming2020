"""
Assuming this is file main_file.py, then this string, being the
first statement in the file, will become the "main_file" module's
docstring when the file is imported.
"""

# technologies used include sqlite3 and Tkinter
import sqlite3
from tkinter import *
from datetime import date
from tkinter import ttk
from tkinter import messagebox

# connects/creates the database for this project and adds/updates it in this directory
conn = sqlite3.connect('student.db')

c = conn.cursor()

# The code below only needs to be executed once to avoid the creation of multiple tables with the same name
# c.execute("""CREATE TABLE students (
#             id integer,
#             first text,
#             last text,
#             grade integer,
#             hours integer,
#             community integer,
#             service integer,
#             achieve integer,
#             date text
#              )""")

# conn.commit()

# Boolean values are stored as integers 0 (false) and 1 (true) in sqlite3


def insert_stu(stu_id, first_name, last_name, grade, hours):
    """

        This function inserts/adds a student into the student database and sets the values for the community service
        awards associated with the number of hours the student has completed.

        Parameters:
            stu_id (int): The student's number/ID.
            first_name(str): The student's first name.
            last_name(str): The student's last name.
            grade(int): The student's grade.
            hours(int): The number of community service hours the student has completed.

        Returns:
            no value

        """
    # initializing local variables
    csa_community = 0
    csa_service = 0
    csa_achieve = 0
    # the if-statements below utilize the local variables above in order to update each award category for the student
    if hours >= 50:
        csa_community = 1
    if hours >= 200:
        csa_service = 1
    if hours >= 500:
        csa_achieve = 1
    # uses with conn instead of conn.commit, however has the same functionality
    with conn:
        # using SQL commands to make queries to the database
        c.execute("INSERT INTO students VALUES (:id, :first, :last, :grade, :hours, :community, :service, :achieve, "
                  ":date)",
                  {'id': stu_id, 'first': first_name, 'last': last_name, 'grade': grade,
                   'hours': hours, 'community': csa_community, 'service': csa_service,
                   'achieve': csa_achieve, 'date': date.today()})


def get_stu_by_name_id(last_name, first_name, stu_id):
    """

        This function returns a student's information based on the given parameters.

        Parameters:
            stu_id (int): The student's number/ID.
            first_name(str): The student's first name.
            last_name(str): The student's last name.

        Returns:
            (list): Student(s) who match the first name, last name and student number/ID from the database that matches
            the parameters entered

        """
    # using SQL commands to make queries to the database
    # no with conn or conn.commit needed because no changes are being made to the database
    # the code below is grabbing data directly from the database
    c.execute("SELECT * FROM students WHERE last=:last AND first=:first AND id=:id",
              {'last': last_name, 'first': first_name, 'id': stu_id})
    return c.fetchall()


# needs to input total hours
def update_hours(first_name, last_name, stu_id, grade, hours):
    """

        This function updates a student's hours and the awards associated with the student's hours in the database.

        Parameters:
            stu_id (int): The student's number/ID.
            first_name(str): The student's first name.
            last_name(str): The student's last name.
            grade(int): The student's grade.
            hours(int): The number of community service hours the student has completed.

        Returns:
            no value

        """
    # initializing local variables
    csa_community = 0
    csa_service = 0
    csa_achieve = 0
    # the if-statements below utilize the local variables above in order to update each award category for the student
    if hours >= 50:
        csa_community = 1
    if hours >= 200:
        csa_service = 1
    if hours >= 500:
        csa_achieve = 1
    # uses with conn instead of conn.commit, however has the same functionality
    with conn:
        # using SQL commands to make queries to the database
        c.execute("""UPDATE students SET hours=:hours, community=:community, service=:service, achieve=:achieve,
                    date =:date
                    WHERE first=:first AND last=:last AND id=:id AND grade=:grade""",
                    {'first': first_name, 'last': last_name, 'id': stu_id, 'grade': grade, 'hours': hours,
                     'community': csa_community, 'service': csa_service, 'achieve': csa_achieve, 'date': date.today()})


def get_community():
    """

        This function gets a list of students who have the community award from the student database.

        Returns:
            (list): Student(s) who have obtained the community award.

        """
    # using SQL commands to make queries to the database
    # no with conn or conn.commit needed because no changes are being made to the database
    # the code below is grabbing data directly from the database
    c.execute("SELECT * FROM students WHERE community=:community",
              {'community': 1})
    return c.fetchall()


def get_service():
    """

        This function gets a list of students who have the service award from the student database.

        Returns:
            (list): Student(s) who have obtained the service award.

        """
    # using SQL commands to make queries to the database
    # no with conn or conn.commit needed because no changes are being made to the database
    # the code below is grabbing data directly from the database
    c.execute("SELECT * FROM students WHERE service=:service",
              {'service': 1})
    return c.fetchall()


def get_achieve():
    """

        This function gets a list of students who have the achieve award from the student database.

        Returns:
            (list): Student(s) who have obtained the achieve award.

        """
    # using SQL commands to make queries to the database
    # no with conn or conn.commit needed because no changes are being made to the database
    # the code below is grabbing data directly from the database
    c.execute("SELECT * FROM students WHERE achieve=:achieve",
              {'achieve': 1})
    return c.fetchall()


def get_all_awards():
    """

        This function gets a list of students who have any award from the student database.

        Returns:
            (list): Student(s) who have obtained any award.

        """
    # using SQL commands to make queries to the database
    # no with conn or conn.commit needed because no changes are being made to the database
    # the code below is grabbing data directly from the database
    c.execute("SELECT * FROM students WHERE community=:community OR service=:service OR achieve=:achieve",
              {'community': 1, 'service': 1, 'achieve': 1})
    return c.fetchall()


def week():
    """

        This function generates a list of dates that represent the past week.

        Returns:
            (list): Dates that represent the past week.

        """
    # gets today's date
    t = str(date.today())
    # creates a list to hold all the dates for the past week based off of the current date
    dates1 = []
    dates1.append(t)
    # adds 7 dates to the dates1 list
    for i in range(7):
        # checks to see if the day is a single digit or not
        if int(t[8]) == 0:
            dates1.append(t[0:9] + str(int(t[9]) - (1 + i)))
        else:
            dates1.append(t[0:8] + str(int(t[8:]) - (1 + i)))
    return dates1


def month():
    """

        This function generates a list of dates that represent the month.

        Returns:
            (list): Dates that represent the month.

        """
    # gets today's date
    t = str(date.today())
    # creates a list to hold all the dates for the current month based off of the current date
    dates = []
    # adds all possible days of that month to the dates list
    for i in range(31):
        if (i + 1) < 10:
            dates.append(t[0:9] + str(i + 1))
        else:
            dates.append(t[0:8] + str(i + 1))
    return dates


def week_hours():
    """

        This function gets a list of students who have updated or logged hours within this week from the
        student database.

        Returns:
            (list): Student(s) who have updated their hours within this current week and the student's hours.

        """
    # uses the list of dates returned from calling the week function to find students who have updated within the week
    date_a = week()
    # using SQL commands to make queries to the database
    c.execute("SELECT id, first, last, grade, hours FROM students WHERE date=:date1 OR date=:date2 OR date=:date3 OR "
              "date=:date4 OR date=:date5 OR date=:date6 OR date=:date7 OR date=:date8",
              {'date1': date_a[0], 'date2': date_a[1], 'date3': date_a[2], 'date4': date_a[3], 'date5': date_a[4],
               'date6': date_a[5], 'date7': date_a[6], 'date8': date_a[7]})
    return c.fetchall()


def month_hours():
    """

        This function gets a list of students who have updated or logged hours this month from the
        student database.

        Returns:
            (list): Student(s) who have updated their hours within this current month and the student's hours.

        """
    # uses the list of dates returned from calling the month function to find students who have updated this month
    date_m = month()
    # using SQL commands to make queries to the database
    c.execute("SELECT id, first, last, grade, hours FROM students WHERE date=:date1 OR date=:date2 OR date=:date3 OR "
              "date=:date4 OR date=:date5 OR date=:date6 OR date=:date7 OR date=:date8 OR date=:date9 OR date=:date10"
              " OR date=:date11 OR date=:date12 OR date=:date13 OR date=:date14 OR date=:date15 OR date=:date16 OR "
              "date=:date17 OR date=:date18 OR date=:date19 OR date=:date20 OR date=:date21 OR date=:date22 OR "
              "date=:date23 OR date=:date24 OR date=:date25 OR date=:date26 OR date=:date27 OR date=:date28 OR "
              "date=:date29 OR date=:date30 OR date=:date31",
              {'date1': date_m[0], 'date2': date_m[1], 'date3': date_m[2], 'date4': date_m[3], 'date5': date_m[4],
               'date6': date_m[5], 'date7': date_m[6], 'date8': date_m[7], 'date9': date_m[8], 'date10': date_m[9],
               'date11': date_m[10], 'date12': date_m[11], 'date13': date_m[12], 'date14': date_m[13],
               'date15': date_m[14], 'date16': date_m[15], 'date17': date_m[16], 'date18': date_m[17],
               'date19': date_m[18], 'date20': date_m[19], 'date21': date_m[20], 'date22': date_m[21],
               'date23': date_m[22], 'date24': date_m[23], 'date25': date_m[24], 'date26': date_m[25],
               'date27': date_m[26], 'date28': date_m[27], 'date29': date_m[28], 'date30': date_m[29],
               'date31': date_m[30]})
    return c.fetchall()


def week_awards():
    """

        This function gets a list of students who have updated or logged hours within this week from the
        student database.

        Returns:
            (list): Student(s) who have updated their hours within this current week and the student's awards and hours.

        """
    # uses the list of dates returned from calling the week function to find students who have updated within the week
    date_a = week()
    # using SQL commands to make queries to the database
    c.execute("SELECT id, first, last, grade, hours, community, service, achieve FROM students "
              "WHERE date=:date1 OR date=:date2 OR date=:date3 OR "
              "date=:date4 OR date=:date5 OR date=:date6 OR date=:date7 OR date=:date8",
              {'date1': date_a[0], 'date2': date_a[1], 'date3': date_a[2], 'date4': date_a[3], 'date5': date_a[4],
               'date6': date_a[5], 'date7': date_a[6], 'date8': date_a[7]})
    return c.fetchall()


def month_awards():
    """

        This function gets a list of students who have updated or logged hours this month from the
        student database.

        Returns:
            (list): Student(s) who have updated their hours within this current month and the student's awards and
            hours.

        """
    # uses the list of dates returned from calling the month function to find students who have updated this month
    date_m = month()
    # using SQL commands to make queries to the database
    c.execute("SELECT id, first, last, grade, hours, community, service, achieve FROM students "
              "WHERE date=:date1 OR date=:date2 OR date=:date3 OR "
              "date=:date4 OR date=:date5 OR date=:date6 OR date=:date7 OR date=:date8 OR date=:date9 OR date=:date10"
              " OR date=:date11 OR date=:date12 OR date=:date13 OR date=:date14 OR date=:date15 OR date=:date16 OR "
              "date=:date17 OR date=:date18 OR date=:date19 OR date=:date20 OR date=:date21 OR date=:date22 OR "
              "date=:date23 OR date=:date24 OR date=:date25 OR date=:date26 OR date=:date27 OR date=:date28 OR "
              "date=:date29 OR date=:date30 OR date=:date31",
              {'date1': date_m[0], 'date2': date_m[1], 'date3': date_m[2], 'date4': date_m[3], 'date5': date_m[4],
               'date6': date_m[5], 'date7': date_m[6], 'date8': date_m[7], 'date9': date_m[8], 'date10': date_m[9],
               'date11': date_m[10], 'date12': date_m[11], 'date13': date_m[12], 'date14': date_m[13],
               'date15': date_m[14], 'date16': date_m[15], 'date17': date_m[16], 'date18': date_m[17],
               'date19': date_m[18], 'date20': date_m[19], 'date21': date_m[20], 'date22': date_m[21],
               'date23': date_m[22], 'date24': date_m[23], 'date25': date_m[24], 'date26': date_m[25],
               'date27': date_m[26], 'date28': date_m[27], 'date29': date_m[28], 'date30': date_m[29],
               'date31': date_m[30]})
    return c.fetchall()

# can be used if needed to reset/delete the database for a new school year
# c.execute("DROP TABLE students")


##################
# GUI CODE BELOW #
##################


# this method would help with navigation within the application
# def home():
#     # hide the visibility of the landing page
#     # write a method with the logic to destroy and reopen the windows
#     if pr.state() == 'normal':
#         pr.destroy()
#     if lh.state() == 'normal':
#         lh.destroy()
#     if sa.state() == 'normal':
#         sa.destroy()
#     root.deiconify()


def help_():
    """

        This function generates a message box to display the help information to the user.


        """
    s = """Help Info Below:
    
     - If you are looking to generate either a weekly or monthly report for awards and/ or hours, then click the Print Report button
    
     - If you are wanting to see a list of students who have obtained awards, then click the See Awards button
     
      - If you are wanting to update hours for a student, click on the Log Hours button"""
    # makes a messagebox appear on top of the screen
    messagebox.showinfo("Help Info", s)


# base/Home page
root = Tk()
root.geometry("1000x1000")
# # home button below
# photo0 = PhotoImage(file="house.png")
# photo_image = photo0.subsample(20, 20)
# b1 = Button(root, text="Home", image=photo_image).place(relx=.02, rely=.02, anchor = NW)
# help button added to the top left corner of window
photo1 = PhotoImage(file="question.png")
photo_image1 = photo1.subsample(7, 7)
b2 = Button(root, text="Help", image=photo_image1, command=help_).place(relx=.02, rely=.02, anchor = NW)
# fbla logo added on home /landing page
photo = PhotoImage(file="FBLA1.png")
panel = Label(root, image=photo)
panel.pack()


def add_label(page, str1):
    """

        This function adds a Label widget to the given page displaying the given string.

        Parameters:
            page (Toplevel): The student's number/ID.
            str1 (str): A string that was meant to be displayed.

        Returns:
            no value

        """
    title1 = Label(page, text=str1)
    title1.pack()


def add_message(page, str1):
    """

        This function adds a Message widget to the given page displaying the given string.

        Parameters:
            page (Toplevel): The student's number/ID.
            str1 (str): A string that was meant to be displayed.

        Returns:
            no value

        """
    title1 = Message(page, text=str1, width=750)
    title1.pack()


def insert_tree_all(tree, info_):
    """

        This function updates a tkinter treeview widget with the corresponding information for each student. This
        treeview will contain all of each student's attributes except for date of most recent update.

        Parameters:
            tree (Treeview): The student's number/ID.
            info_ (list): Student(s) information

        Returns:
            no value

        """
    tree.pack()
    # gets rid of any information in there from before, so the information is updated each time
    tree.delete(*tree.get_children())
    # gets the information from the list about each student and updates the treeview widget accordingly
    for x in range(len(info_)):
        # each student has an index on the info_ list
        # each index on the info_ list can be further broken down into another list to get each attribute of the student
        stu = list(info_[x])
        for i in range(5, 8):
            # Checks to see if the student has any awards and if so the value will appear as either
            # 'yes' or 'no' in the tree view widget shown to the user
            if stu[i] == 1:
                stu[i] = 'Yes'
            else:
                stu[i] = 'No'
        # adds the student's information to the treeview widget
        tree.insert("", 0, text="Line 1", values=(stu[0], stu[1], stu[2], stu[3], stu[4], stu[5], stu[6], stu[7]))


def insert_up_to_hours(tree, info_):
    """

        This function updates a tkinter treeview widget with the corresponding information for each student. This
        treeview will contain first name, last name, student number/ID, and hours.

        Parameters:
            tree (Treeview): The student's number/ID.
            info_ (list): Student(s) information

        Returns:
            no value

        """
    tree.pack()
    # gets rid of any information in there from before, so the information is updated each time
    tree.delete(*tree.get_children())
    # gets the information from the list about each student and updates the treeview widget accordingly
    for x in range(len(info_)):
        # each student has an index on the info_ list
        # each index on the info_ list can be further broken down into another list to get each attribute of the student
        stu = list(info_[x])
        # adds the student's information to the treeview widget
        tree.insert("", 0, text="Line 1", values=(stu[0], stu[1], stu[2], stu[3], stu[4]))


# opens the print report page on top of the root/Home page
def open_print_report():
    """

        This function generates a Toplevel widget for the print report page of this project that sits on top of the root
        window.


        """
    pr = Toplevel()

    pr.geometry("1000x1000")

    # # home button below
    # Button(pr, text="Home", image=photo_image).place(relx=.02, rely=.02, anchor = NW)

    # help button below
    Button(pr, text="Home", image=photo_image1, command=help_).place(relx=.02, rely=.02, anchor = NW)

    pr.title('FBLA Community Service Tracker')
    title1 = Label(pr, text='Print Report')
    title1.pack()

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    c1 = Checkbutton(pr, text="Weekly Report - Community Service Hours", variable=var1, onvalue=1, offvalue=0)
    c1.pack()
    c2 = Checkbutton(pr, text="Monthly Report - Community Service Hours", variable=var2, onvalue=2, offvalue=0)
    c2.pack()
    c3 = Checkbutton(pr, text="Weekly Report - Awards with Hours", variable=var3, onvalue=3, offvalue=0)
    c3.pack()
    c4 = Checkbutton(pr, text="Monthly Report - Awards with Hours", variable=var4, onvalue=4, offvalue=0)
    c4.pack()

    def print_():
        """

            This function updates the treeview widgets based on the values from the CheckButton variables.


            """
        if var1.get() == 1:
            title1.pack()
            insert_up_to_hours(tree, week_hours())
        else:
            tree.pack_forget()
            title1.pack_forget()
        if var2.get() == 2:
            title2.pack()
            insert_up_to_hours(tree2, month_hours())
        else:
            tree2.pack_forget()
            title2.pack_forget()
        if var3.get() == 3:
            title3.pack()
            insert_tree_all(tree3, week_awards())
        else:
            tree3.pack_forget()
            title3.pack_forget()
        if var4.get() == 4:
            title4.pack()
            insert_tree_all(tree4, month_awards())
        else:
            tree4.pack_forget()
            title4.pack_forget()

    button0 = Button(pr, text='Print', fg="blue", command=print_)
    button0.pack()

    title1 = Label(pr, text='Weekly Report - Community Service Hours')
    title1.pack_forget()
    tree = ttk.Treeview(pr)
    # the line of code below hides the first column from the tree view
    tree['show'] = 'headings'
    tree["columns"] = ("1", "2", "3", "4", "5")
    tree.column("1", width=85)
    tree.column("2", width=100)
    tree.column("3", width=100)
    tree.column("4", width=50)
    tree.column("5", width=100)
    tree.heading("1", text="ID")
    tree.heading("2", text="First name")
    tree.heading("3", text="Last Name")
    tree.heading("4", text="Grade")
    tree.heading("5", text="Hours")
    tree.pack_forget()

    title2 = Label(pr, text='Monthly Report - Community Service Hours')
    title2.pack_forget()
    tree2 = ttk.Treeview(pr)
    # the line of code below hides the first column from the tree view
    tree2['show'] = 'headings'
    tree2["columns"] = ("1", "2", "3", "4", "5")
    tree2.column("1", width=85)
    tree2.column("2", width=100)
    tree2.column("3", width=100)
    tree2.column("4", width=50)
    tree2.column("5", width=100)
    tree2.heading("1", text="ID")
    tree2.heading("2", text="First name")
    tree2.heading("3", text="Last Name")
    tree2.heading("4", text="Grade")
    tree2.heading("5", text="Hours")
    tree2.pack_forget()

    title3 = Label(pr, text='Weekly Report - Awards with Hours')
    title3.pack_forget()
    tree3 = ttk.Treeview(pr)
    # the line of code below hides the first column from the tree view
    tree3['show'] = 'headings'
    tree3["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")
    tree3.column("1", width=85)
    tree3.column("2", width=100)
    tree3.column("3", width=100)
    tree3.column("4", width=50)
    tree3.column("5", width=100)
    tree3.column("6", width=100)
    tree3.column("7", width=100)
    tree3.column("8", width=100)
    tree3.heading("1", text="ID")
    tree3.heading("2", text="First name")
    tree3.heading("3", text="Last Name")
    tree3.heading("4", text="Grade")
    tree3.heading("5", text="Hours")
    tree3.heading("6", text="Community Award")
    tree3.heading("7", text="Service Award")
    tree3.heading("8", text="Achievement Award")
    tree3.pack_forget()

    title4 = Label(pr, text='Monthly Report - Awards with Hours')
    title4.pack_forget()
    tree4 = ttk.Treeview(pr)
    # the line of code below hides the first column from the tree view
    tree4['show'] = 'headings'
    tree4["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")
    tree4.column("1", width=85)
    tree4.column("2", width=100)
    tree4.column("3", width=100)
    tree4.column("4", width=50)
    tree4.column("5", width=100)
    tree4.column("6", width=100)
    tree4.column("7", width=100)
    tree4.column("8", width=100)
    tree4.heading("1", text="ID")
    tree4.heading("2", text="First name")
    tree4.heading("3", text="Last Name")
    tree4.heading("4", text="Grade")
    tree4.heading("5", text="Hours")
    tree4.heading("6", text="Community Award")
    tree4.heading("7", text="Service Award")
    tree4.heading("8", text="Achievement Award")
    tree4.pack_forget()


def which_awards(award):
    """

        This function determines which function to run depending on the input.

        Parameters:
        award (str): A string

        Returns:
        (function): That will return a list of students with that award.


        """
    if award == 'CSA Community':
        return get_community()
    elif award == 'CSA Service':
        return get_service()
    elif award == 'CSA Achievement':
        return get_achieve()
    elif award == 'All CSA Awards':
        return get_all_awards()
    else:
        pass


# opens the see awards page on top of the root/Home page
def open_see_awards():
    """

        This function generates a Toplevel widget for the see awards page of this project that sits on top of the root
        window.


        """
    sa = Toplevel()
    sa.geometry("1000x1000")

    # # home button below
    # Button(sa, text="Home", image=photo_image).place(relx=.02, rely=.02, anchor = NW)

    # help button below
    Button(sa, text="Home", image=photo_image1, command=help_).place(relx=.02, rely=.02, anchor = NW)

    sa.title('FBLA Community Service Tracker')
    title = Label(sa, text='Awards')
    title.pack()

    d = Label(sa, text="Select one of the following to see a list of students with these awards")
    d.pack()
    variable = StringVar(sa)
    variable.set('CSA Community')
    l = OptionMenu(sa, variable, 'CSA Community', 'CSA Service', 'CSA Achievement', 'All CSA Awards')
    l.pack()

    def refresh_value():
        """

            This function updates the treeview widget based on the value in the variable associated with the drop
            down list.


            """
        tree.pack()
        s = which_awards(variable.get())
        insert_tree_all(tree, s)

    button01 = Button(sa, text='Update', fg="blue", command=refresh_value)
    button01.pack()
    awards_chosen = Label(sa, text="")
    awards_chosen.pack()
    tree = ttk.Treeview(sa)
    # the line of code below hides the first column from the tree view widget
    tree['show'] = 'headings'
    tree["columns"] = ("1", "2", "3", "4", "5")
    tree.column("1", width=85)
    tree.column("2", width=100)
    tree.column("3", width=100)
    tree.column("4", width=50)
    tree.column("5", width=100)
    tree.heading("1", text="ID")
    tree.heading("2", text="First name")
    tree.heading("3", text="Last Name")
    tree.heading("4", text="Grade")
    tree.heading("5", text="Hours")
    tree.pack_forget()


# opens the log hours page on top of the root/Home page
def open_log_hours():
    """

        This function generates a Toplevel widget for the log hours page of this project that sits on top of the root
        window.


        """
    lh = Toplevel()
    lh.geometry("1000x1000")

    # # home button below
    # Button(lh, text="Home", image=photo_image).place(relx=.02, rely=.02, anchor = NW)

    # help button below
    Button(lh, text="Home", image=photo_image1, command=help_).place(relx=.02, rely=.02, anchor = NW)

    lh.title('FBLA Community Service Tracker')

    title1 = Label(lh, text='Log Hours')
    title1.pack()

    req = Label(lh, text='Fields with a * are required in order to have your hours updated')
    req.pack()

    name = Label(lh, text='Student First Name *')
    name.pack()
    f_name_entry = Entry(lh)
    f_name_entry.pack()

    name = Label(lh, text='Student Last Name *')
    name.pack()
    l_name_entry = Entry(lh)
    l_name_entry.pack()

    name = Label(lh, text='Student Number/ID *')
    name.pack()
    id_entry = Entry(lh)
    id_entry.pack()

    # by only using one variable the user can only check one of the 4 grade options
    var1 = IntVar()
    grade_level = Label(lh, text='Student Grade *')
    grade_level.pack()
    Radiobutton(lh, text="12", variable=var1, value=12).pack()
    Radiobutton(lh, text="11", variable=var1, value=11).pack()
    Radiobutton(lh, text="10", variable=var1, value=10).pack()
    Radiobutton(lh, text=" 9", variable=var1, value=9).pack()

    name = Label(lh, text='Total Hours to Log *')
    name.pack()
    hour_entry = Entry(lh)
    hour_entry.pack()

    fbla_ch = Label(lh, text='Choose Your FBLA Chapter')
    fbla_ch.pack()
    lb1 = Listbox(lh)
    lb1.pack()
    lb1.insert(1, "Steinbrenner High School")
    lb1.insert(2, "Middleton HIgh School")
    lb1.insert(3, "Land'O Lakes High School")
    lb1.insert(4, "River Ridge High School")
    lb1.insert(5, "Sunlake High School")
    lb1.insert(6, "Zephyrhills High School")

    def when_clicked():
        """

            This function processes the input given by the user through the log hours page and either updates the
            database and notifies the user or gives the user an error message and notifies them that their entry
            cannot be processed as is.


            """
        if len(f_name_entry.get()) == 0 or len(l_name_entry.get()) == 0 or len(str(id_entry.get())) == 0 or len(str(var1.get())) == 0 or len(str(hour_entry.get())) == 0:
            messagebox.showerror("Error", "* Required Fields Left Blank *")
        else:
            update_hours(f_name_entry.get(),
                         l_name_entry.get(),
                         int(id_entry.get()),
                         var1.get(),
                         int(hour_entry.get()))
            messagebox.showinfo("Success!", "Your hours have been updated!")

    button_submit = Button(lh, text='Submit', fg="blue", command=when_clicked)
    button_submit.pack()


root.title('FBLA Community Service Tracker')
title = Label(root, text='FBLA Community Service Tracker')
title.pack()
info = Label(root, text="This application keeps record of students' community service hours and awards.")
info.pack()
button1 = Button(root, text='Print Report', fg="blue", command=open_print_report)
button1.pack()
button2 = Button(root, text='See Awards', fg="blue", command=open_see_awards)
button2.pack()
button3 = Button(root, text='Log Hours', fg="blue", command=open_log_hours)
button3.pack()
# the below line of code is necessary to run the root window, which is the base of the whole program
root.mainloop()
# gets all students in the students.db (the database) table students
c.execute("SELECT * FROM students")
# prints out all the student's information in the database
# good to run when wanting to verify that the functions are calling and reading the right attributes
print(c.fetchall())
# good practice to close the database once finished
conn.close()
