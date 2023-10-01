#Final Project in OOP

#Bañar, Jude Michael
#Cuerdo, Charles Tristan Alfred
#manato Johnnina Liliana

#BSIS - 2AB

import tkinter
from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox
from tkinter import *
import sqlite3

#Main Window 
window = tkinter.Tk()
window.title("Movie Ticket Booking System")

#Function that will direct us at Manila branch ticket booking
def manila():
    window1 = tkinter.Toplevel()
    window1.title("Buy Movie Ticket - Manila Branch")
    window1.config(width = 300, height = 200)

    frame = tkinter.Frame(window1)
    frame.pack()

    #Function that will make a window for movie browsing
    def win2():
        window2 = tkinter.Toplevel()
        window2.title("Now Showing!")
        window2.config(width = 1500, height = 800)
        bgImage = PhotoImage (file = "kemecinema.png")
        Label(window2, image = bgImage).place(relwidth = 1, relheight =1)
       
        frame.pack(window2)

    #Choose Movie
    choose_movie_frame = tkinter.LabelFrame(frame, text = "Select Movie")
    choose_movie_frame.grid(row = 0, column = 0, sticky = "news", padx = 10, pady = 10)

    movie_label = tkinter.Label(choose_movie_frame, text = "Select Movie")
    movie_label.grid(row = 0, column = 1)
    movie_combobox = ttk.Combobox(choose_movie_frame, width = 40, values = ["Doctor Strange: In the Multiverse of Madness", "Thor: Love and Thunder", "Black Panther: Wakanda Forever", "Ant-Man and the Wasp: Quantumania"])
    movie_combobox.grid(row = 1, column = 1)

    movies_button = tkinter.Button(choose_movie_frame, text = "Browse Movies", command = win2)
    movies_button.grid(row = 1, column = 0)

    #This will show the rest of the widgets in the tciket booking window
    def proceed():
        movie1 = movie_combobox.get()

        #Connects to a database and create table using SQLITE3
        def submit():
            messagebox.showinfo("Success!", "Movie Ticket Booked!")
            
            name = name_entry.get()
            surname = surname_entry.get()
            gender = gender_combobox.get()
            number = num_entry.get()
            movie = movie_combobox.get()
            quantity = quantity_spinbox.get()
            '''cinema = cinema_combobox.get()'''
            theater = theater_combobox.get()
            month = month_combobox.get()
            day = day_spinbox.get()
            year = year_combobox.get()
            time = time_var.get()

            #creates the database and the table
            conn = sqlite3.connect('cinema.db')
            table_create_query =  '''CREATE TABLE IF NOT EXISTS Buyers_Data_Manila
                    (Name TEXT, Surname TEXT, Gender TEXT, Number INT, Movie TEXT, Quantity INT,
                    Theater TEXT, Month TEXT, Day INT, Year INT, Time INT)
            '''
            conn.execute(table_create_query)

            #insert data in the table
            data_insert_query = '''INSERT INTO Buyers_Data_Manila (name, surname, gender, number, movie,
                    quantity, theater, month, day, year, time) VALUES (?,?,?,?,?,?,?,?,?,?,?)'''
            data_insert_tuple = (name, surname, gender, number, movie,
                    quantity, theater, month, day, year, time)
            cursor = conn.cursor() 
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()
            
        #Payment frame
        def payment():
            pay_frame = tkinter.LabelFrame(frame, text = "Payment")
            pay_frame.grid(row = 3, column = 0, sticky = "news")

            gnum_label = tkinter.Label(pay_frame, text ="Enter G-Cash number")
            gnum_label.grid(row = 0, column = 0)
            gnum_entry = tkinter.Entry(pay_frame)
            gnum_entry.grid(row = 1, column =0, padx = 10)

            quantity = int(quantity_spinbox.get())
            
            price = 350.00

            total = price*quantity

            amt_label = tkinter.Label(pay_frame, text = f"Pay P{total} ?")
            amt_label.grid(row = 0, column = 1, padx = 10, pady = 10)

            num_button = tkinter.Button(pay_frame, text = "Pay", command = submit_button)
            num_button.grid(row = 1, column = 1, padx = 10, pady = 10)

            for widget in pay_frame.winfo_children():
                widget.grid_configure(padx = 20, pady =20)
        
        #Destroy the window          
        def back():
            window1.destroy()
        
        #Check if all data is given by the user
        def submit_button():
            
            name = name_entry.get()
            surname = surname_entry.get()
            gender = gender_combobox.get()
            number = num_entry.get()
            quantity = quantity_spinbox.get()
            theater = theater_combobox.get()
            month = month_combobox.get()
            day = day_spinbox.get()
            year = year_combobox.get()
            time = time_var.get()
            
            if name == "":
                messagebox.showerror("Error", "Please input your First Name")    
            elif surname == "":
                messagebox.showerror("Error", "Please input your Last Name")
            elif gender == "":
                messagebox.showerror("Error", "Please input your Gender")
            elif number == "":
                messagebox.showerror("Error", "Please input your Contact Number")
            elif quantity == "":
                messagebox.showerror("Error", "Please input Ticket Quantity")
            elif theater == "":
                messagebox.showerror("Error", "Please input Theather")
            elif month == "":
                messagebox.showerror("Error", "Please input Month")
            elif day == "":
                messagebox.showerror("Error", "Please input Day")
            elif year == "":
                messagebox.showerror("Error", "Please input Year")
            elif time == "":
                messagebox.showerror("Error", "Please input Time")
            else:
            #Submit button
                submit_button = tkinter.Button(frame, text = "Submit", command = submit)
                submit_button.grid(row = 6, columnspan = 2, sticky = "news", padx= 5, pady =5)
            
        #Basic Information
        U_info_frame = tkinter.LabelFrame(frame, text = "Your Information")
        U_info_frame.grid(row = 1, column = 1, sticky = "news", padx = 10, pady = 10)

        name_label = tkinter.Label(U_info_frame, text = "First Name")
        name_label.grid(row = 0, column = 0)
        surname_label = tkinter.Label(U_info_frame, text = "Last Name")
        surname_label.grid(row = 0, column = 1)

        name_entry = tkinter.Entry(U_info_frame)
        surname_entry = tkinter.Entry(U_info_frame)
        name_entry.grid(row = 1, column = 0)
        surname_entry.grid(row = 1, column = 1)

        gender_label = tkinter.Label(U_info_frame, text = "Gender")
        gender_combobox = ttk.Combobox(U_info_frame, values = ["Male", "Female", "Others"])
        gender_label.grid(row = 0, column = 2)
        gender_combobox.grid(row = 1, column = 2)

        num_label = tkinter.Label(U_info_frame, text = "Contact Number")
        num_entry = tkinter.Entry(U_info_frame)
        num_label.grid(row = 2, column = 1)
        num_entry.grid(row = 3, column = 1)
 
        #Choose Payment
        pay_button = tkinter.Button(U_info_frame, text = "Proceed to Payment", command = payment)
        pay_button.grid(row = 3, column = 2, padx =10, pady = 5)
            
        for widget in U_info_frame.winfo_children():
            widget.grid_configure(padx = 10, pady = 5)
                
        #Choose Time and Date
        choose_time_frame = tkinter.LabelFrame(frame, text = "Select Time")
        choose_time_frame.grid(row = 1, column = 0, sticky = "news", padx = 10, pady = 10)

        date_label = tkinter.Label(choose_time_frame, text = "Choose date")
        date_label.grid(row = 0, column = 0)

        month_combobox = ttk.Combobox(choose_time_frame, values = ["February"])
        month_combobox.grid(row = 1, column = 0)

        day_spinbox = tkinter.Spinbox(choose_time_frame, from_= 1, to = 28)
        day_spinbox.grid(row = 1, column = 1)

        year_combobox = ttk.Combobox(choose_time_frame, values = ["2023"])
        year_combobox.grid(row =1, column = 2)

        time_label = tkinter.Label(choose_time_frame, text = "Choose your time")
        time_label.grid(row = 2, column = 0)

        time_var = tkinter.StringVar()
        time1_chckbttn = tkinter.Checkbutton(choose_time_frame, text = "1:30 PM", variable = time_var, onvalue = "1:30 PM", offvalue = "")
        time1_chckbttn.grid(row = 3, column = 0)
        time2_chckbttn = tkinter.Checkbutton(choose_time_frame, text = "5:00 PM", variable = time_var, onvalue = "5:00 PM", offvalue = "")
        time2_chckbttn.grid(row = 3, column = 1)
        time3_chckbttn = tkinter.Checkbutton(choose_time_frame, text = "8:30 PM", variable = time_var, onvalue = "8:30 PM", offvalue = "")
        time3_chckbttn.grid(row = 3, column = 2)

        for widget in choose_time_frame.winfo_children():
            widget.grid_configure(padx = 10, pady = 5)

        #Back Button
        back_button = tkinter.Button(frame, text = "Back", command = back)
        back_button.grid(row = 5, columnspan = 2, sticky = "news", padx= 5, pady =5)

        #Movie are assigned in a specific cinema. If statement will help to determine the Cinema Number
        if movie1 == "Doctor Strange: In the Multiverse of Madness":
        
            #Choose Cinema 
            choose_cinema_frame = tkinter.LabelFrame(frame, text = "Select Cinema")
            choose_cinema_frame.grid(row = 0, column = 1, sticky = "news", padx = 10, pady = 10)

            theater_label = tkinter.Label(choose_cinema_frame, text = "Choose your Theater")
            theater_label.grid(row = 0, column = 0)
            theater_combobox = ttk.Combobox(choose_cinema_frame, values = ["Cinema 1 - P350.00"])
            theater_combobox.grid(row = 1, column = 0)
            
            quantity_label = tkinter.Label(choose_cinema_frame, text = "Quantity")
            quantity_spinbox = tkinter.Spinbox(choose_cinema_frame, from_ = 1, to = 5)
            quantity_label.grid(row = 0, column = 1)
            quantity_spinbox.grid(row = 1, column = 1)

            for widget in choose_cinema_frame.winfo_children():
                widget.grid_configure(padx = 10, pady = 5)     

        elif movie1 == "Thor: Love and Thunder":

            #Choose Cinema 
            choose_cinema_frame = tkinter.LabelFrame(frame, text = "Select Cinema")
            choose_cinema_frame.grid(row = 0, column = 1, sticky = "news", padx = 10, pady = 10)

            theater_label = tkinter.Label(choose_cinema_frame, text = "Choose your Theater")
            theater_label.grid(row = 0, column = 0)
            theater_combobox = ttk.Combobox(choose_cinema_frame, values = ["Cinema 2 - P350.00"])
            theater_combobox.grid(row = 1, column = 0)
            
            quantity_label = tkinter.Label(choose_cinema_frame, text = "Quantity")
            quantity_spinbox = tkinter.Spinbox(choose_cinema_frame, from_ = 1, to = 5)
            quantity_label.grid(row = 0, column = 1)
            quantity_spinbox.grid(row = 1, column = 1)

            for widget in choose_cinema_frame.winfo_children():
                widget.grid_configure(padx = 10, pady = 5)

        elif movie1 == "Black Panther: Wakanda Forever":

            #Choose Cinema 
            choose_cinema_frame = tkinter.LabelFrame(frame, text = "Select Cinema")
            choose_cinema_frame.grid(row = 0, column = 1, sticky = "news", padx = 10, pady = 10)

            theater_label = tkinter.Label(choose_cinema_frame, text = "Choose your Theater")
            theater_label.grid(row = 0, column = 0)
            theater_combobox = ttk.Combobox(choose_cinema_frame, values = ["Cinema 3 - P350.00"])
            theater_combobox.grid(row = 1, column = 0)
            
            quantity_label = tkinter.Label(choose_cinema_frame, text = "Quantity")
            quantity_spinbox = tkinter.Spinbox(choose_cinema_frame, from_ = 1, to = 5)
            quantity_label.grid(row = 0, column = 1)
            quantity_spinbox.grid(row = 1, column = 1)

            for widget in choose_cinema_frame.winfo_children():
                widget.grid_configure(padx = 10, pady = 5)

        elif movie1 == "Ant-Man and the Wasp: Quantumania":
        
            #Choose Cinema 
            choose_cinema_frame = tkinter.LabelFrame(frame, text = "Select Cinema")
            choose_cinema_frame.grid(row = 0, column = 1, sticky = "news", padx = 10, pady = 10)

            theater_label = tkinter.Label(choose_cinema_frame, text = "Choose your Theater")
            theater_label.grid(row = 0, column = 0)
            theater_combobox = ttk.Combobox(choose_cinema_frame, values = ["Cinema 4 - P350.00"])
            theater_combobox.grid(row = 1, column = 0)
            
            quantity_label = tkinter.Label(choose_cinema_frame, text = "Quantity")
            quantity_spinbox = tkinter.Spinbox(choose_cinema_frame, from_ = 1, to = 5)
            quantity_label.grid(row = 0, column = 1)
            quantity_spinbox.grid(row = 1, column = 1)

            for widget in choose_cinema_frame.winfo_children():
                widget.grid_configure(padx = 10, pady = 5)

        else:
            messagebox.showerror("Error", "Please choose a movie.")


    next_button = tkinter.Button(choose_movie_frame, text = "Next", command = proceed)
    next_button.grid(row = 3, column = 1)

    for widget in choose_movie_frame.winfo_children():
        widget.grid_configure(padx = 10, pady = 5)

#Function that will direct us at QC branch ticket booking
def quezon():
    window1 = tkinter.Toplevel()
    window1.title("Buy Movie Ticket - Quezon City Branch")
    window1.config(width = 300, height = 200)

    frame = tkinter.Frame(window1)
    frame.pack()

    def win2():
        window2 = tkinter.Toplevel()
        window2.title("Now Showing!")
        window2.config(width = 300, height = 200)
        

    #Choose Movie
    choose_movie_frame = tkinter.LabelFrame(frame, text = "Select Movie")
    choose_movie_frame.grid(row = 0, column = 0, sticky = "news", padx = 10, pady = 10)

    movie_label = tkinter.Label(choose_movie_frame, text = "Select Movie")
    movie_label.grid(row = 0, column = 1)
    movie_combobox = ttk.Combobox(choose_movie_frame, width = 40, values = ["Doctor Strange: In the Multiverse of Madness", "Thor: Love and Thunder", "Black Panther: Wakanda Forever", "Ant-Man and the Wasp: Quantumania"])
    movie_combobox.grid(row = 1, column = 1)

    movies_button = tkinter.Button(choose_movie_frame, text = "Browse Movies", command = win2)
    movies_button.grid(row = 1, column = 0)

    def proceed():
        movie1 = movie_combobox.get()

        def submit():
            messagebox.showinfo("Success!", "Movie Ticket Booked!")
            
            name = name_entry.get()
            surname = surname_entry.get()
            gender = gender_combobox.get()
            number = num_entry.get()
            movie = movie_combobox.get()
            quantity = quantity_spinbox.get()
            theater = theater_combobox.get()
            month = month_combobox.get()
            day = day_spinbox.get()
            year = year_combobox.get()
            time = time_var.get()

            
            conn = sqlite3.connect('cinema.db')
            table_create_query =  '''CREATE TABLE IF NOT EXISTS Buyers_Data_Quezon
                    (Name TEXT, Surname TEXT, Gender TEXT, Number INT, Movie TEXT, Quantity INT,
                    Theater TEXT, Month TEXT, Day INT, Year INT, Time INT)
            '''
            conn.execute(table_create_query)

            data_insert_query = '''INSERT INTO Buyers_Data_Quezon (name, surname, gender, number, movie,
                    quantity, theater, month, day, year, time) VALUES (?,?,?,?,?,?,?,?,?,?,?)'''
            data_insert_tuple = (name, surname, gender, number, movie,
                    quantity, theater, month, day, year, time)
            cursor = conn.cursor() 
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()
            

        def payment():
            pay_frame = tkinter.LabelFrame(frame, text = "Payment")
            pay_frame.grid(row = 3, column = 0, sticky = "news")

            gnum_label = tkinter.Label(pay_frame, text ="Enter G-Cash number")
            gnum_label.grid(row = 0, column = 0)
            gnum_entry = tkinter.Entry(pay_frame)
            gnum_entry.grid(row = 1, column =0, padx = 10)

            quantity = int(quantity_spinbox.get())
            
            price = 350.00

            total = price*quantity

            amt_label = tkinter.Label(pay_frame, text = f"Pay P{total} ?")
            amt_label.grid(row = 0, column = 1, padx = 10, pady = 10)

            num_button = tkinter.Button(pay_frame, text = "Pay", command = submit_button)
            num_button.grid(row = 1, column = 1, padx = 10, pady = 10)

            for widget in pay_frame.winfo_children():
                widget.grid_configure(padx = 20, pady =20)
                    
        def back():
            window1.destroy()
        
        def submit_button():
            
            name = name_entry.get()
            surname = surname_entry.get()
            gender = gender_combobox.get()
            number = num_entry.get()
            quantity = quantity_spinbox.get()
            theater = theater_combobox.get()
            month = month_combobox.get()
            day = day_spinbox.get()
            year = year_combobox.get()
            time = time_var.get()
            
            if name == "":
                messagebox.showerror("Error", "Please input your First Name")    
            elif surname == "":
                messagebox.showerror("Error", "Please input your Last Name")
            elif gender == "":
                messagebox.showerror("Error", "Please input your Gender")
            elif number == "":
                messagebox.showerror("Error", "Please input your Contact Number")
            elif quantity == "":
                messagebox.showerror("Error", "Please input Ticket Quantity")
            elif theater == "":
                messagebox.showerror("Error", "Please input Theather")
            elif month == "":
                messagebox.showerror("Error", "Please input Month")
            elif day == "":
                messagebox.showerror("Error", "Please input Day")
            elif year == "":
                messagebox.showerror("Error", "Please input Year")
            elif time == "":
                messagebox.showerror("Error", "Please input Time")
            else:
            #Submit button
                submit_button = tkinter.Button(frame, text = "Submit", command = submit)
                submit_button.grid(row = 6, columnspan = 2, sticky = "news", padx= 5, pady =5)
            

        U_info_frame = tkinter.LabelFrame(frame, text = "Your Information")
        U_info_frame.grid(row = 1, column = 1, sticky = "news", padx = 10, pady = 10)

        name_label = tkinter.Label(U_info_frame, text = "First Name")
        name_label.grid(row = 0, column = 0)
        surname_label = tkinter.Label(U_info_frame, text = "Last Name")
        surname_label.grid(row = 0, column = 1)

        name_entry = tkinter.Entry(U_info_frame)
        surname_entry = tkinter.Entry(U_info_frame)
        name_entry.grid(row = 1, column = 0)
        surname_entry.grid(row = 1, column = 1)

        gender_label = tkinter.Label(U_info_frame, text = "Gender")
        gender_combobox = ttk.Combobox(U_info_frame, values = ["Male", "Female", "Others"])
        gender_label.grid(row = 0, column = 2)
        gender_combobox.grid(row = 1, column = 2)

        num_label = tkinter.Label(U_info_frame, text = "Contact Number")
        num_entry = tkinter.Entry(U_info_frame)
        num_label.grid(row = 2, column = 1)
        num_entry.grid(row = 3, column = 1)
            
        #Choose Payment
        seat_button = tkinter.Button(U_info_frame, text = "Proceed to Payment", command = payment)
        seat_button.grid(row = 3, column = 2, padx =10, pady = 5)
            
        for widget in U_info_frame.winfo_children():
            widget.grid_configure(padx = 10, pady = 5)
                
        #Choose Time and Date
        choose_time_frame = tkinter.LabelFrame(frame, text = "Select Time")
        choose_time_frame.grid(row = 1, column = 0, sticky = "news", padx = 10, pady = 10)

        date_label = tkinter.Label(choose_time_frame, text = "Choose date")
        date_label.grid(row = 0, column = 0)

        month_combobox = ttk.Combobox(choose_time_frame, values = ["February"])
        month_combobox.grid(row = 1, column = 0)

        day_spinbox = tkinter.Spinbox(choose_time_frame, from_= 1, to = 28)
        day_spinbox.grid(row = 1, column = 1)

        year_combobox = ttk.Combobox(choose_time_frame, values = ["", "2023"])
        year_combobox.grid(row =1, column = 2)

        time_label = tkinter.Label(choose_time_frame, text = "Choose your time")
        time_label.grid(row = 2, column = 0)

        time_var = tkinter.StringVar()
        time1_chckbttn = tkinter.Checkbutton(choose_time_frame, text = "1:30 PM", variable = time_var, onvalue = "1:30 PM", offvalue = "")
        time1_chckbttn.grid(row = 3, column = 0)
        time2_chckbttn = tkinter.Checkbutton(choose_time_frame, text = "5:00 PM", variable = time_var, onvalue = "5:00 PM", offvalue = "")
        time2_chckbttn.grid(row = 3, column = 1)
        time3_chckbttn = tkinter.Checkbutton(choose_time_frame, text = "8:30 PM", variable = time_var, onvalue = "8:30 PM", offvalue = "")
        time3_chckbttn.grid(row = 3, column = 2)

        for widget in choose_time_frame.winfo_children():
            widget.grid_configure(padx = 10, pady = 5)

        #Back Button
        back_button = tkinter.Button(frame, text = "Back", command = back)
        back_button.grid(row = 5, columnspan = 2, sticky = "news", padx= 5, pady =5)

        if movie1 == "Doctor Strange: In the Multiverse of Madness":
        
            #Choose Cinema 
            choose_cinema_frame = tkinter.LabelFrame(frame, text = "Select Cinema")
            choose_cinema_frame.grid(row = 0, column = 1, sticky = "news", padx = 10, pady = 10)

            theater_label = tkinter.Label(choose_cinema_frame, text = "Choose your Theater")
            theater_label.grid(row = 0, column = 0)
            theater_combobox = ttk.Combobox(choose_cinema_frame, values = ["Cinema 1 - P350.00"])
            theater_combobox.grid(row = 1, column = 0)
            
            quantity_label = tkinter.Label(choose_cinema_frame, text = "Quantity")
            quantity_spinbox = tkinter.Spinbox(choose_cinema_frame, from_ = 1, to = 5)
            quantity_label.grid(row = 0, column = 1)
            quantity_spinbox.grid(row = 1, column = 1)

            for widget in choose_cinema_frame.winfo_children():
                widget.grid_configure(padx = 10, pady = 5)     

        elif movie1 == "Thor: Love and Thunder":

            #Choose Cinema 
            choose_cinema_frame = tkinter.LabelFrame(frame, text = "Select Cinema")
            choose_cinema_frame.grid(row = 0, column = 1, sticky = "news", padx = 10, pady = 10)

            theater_label = tkinter.Label(choose_cinema_frame, text = "Choose your Theater")
            theater_label.grid(row = 0, column = 0)
            theater_combobox = ttk.Combobox(choose_cinema_frame, values = ["Cinema 2 - P350.00"])
            theater_combobox.grid(row = 1, column = 0)
            
            quantity_label = tkinter.Label(choose_cinema_frame, text = "Quantity")
            quantity_spinbox = tkinter.Spinbox(choose_cinema_frame, from_ = 1, to = 5)
            quantity_label.grid(row = 0, column = 1)
            quantity_spinbox.grid(row = 1, column = 1)

            for widget in choose_cinema_frame.winfo_children():
                widget.grid_configure(padx = 10, pady = 5)

        elif movie1 == "Black Panther: Wakanda Forever":

            #Choose Cinema 
            choose_cinema_frame = tkinter.LabelFrame(frame, text = "Select Cinema")
            choose_cinema_frame.grid(row = 0, column = 1, sticky = "news", padx = 10, pady = 10)

            theater_label = tkinter.Label(choose_cinema_frame, text = "Choose your Theater")
            theater_label.grid(row = 0, column = 0)
            theater_combobox = ttk.Combobox(choose_cinema_frame, values = ["Cinema 3 - P350.00"])
            theater_combobox.grid(row = 1, column = 0)
            
            quantity_label = tkinter.Label(choose_cinema_frame, text = "Quantity")
            quantity_spinbox = tkinter.Spinbox(choose_cinema_frame, from_ = 1, to = 5)
            quantity_label.grid(row = 0, column = 1)
            quantity_spinbox.grid(row = 1, column = 1)

            for widget in choose_cinema_frame.winfo_children():
                widget.grid_configure(padx = 10, pady = 5)

        elif movie1 == "Ant-Man and the Wasp: Quantumania":
        
            #Choose Cinema 
            choose_cinema_frame = tkinter.LabelFrame(frame, text = "Select Cinema")
            choose_cinema_frame.grid(row = 0, column = 1, sticky = "news", padx = 10, pady = 10)

            theater_label = tkinter.Label(choose_cinema_frame, text = "Choose your Theater")
            theater_label.grid(row = 0, column = 0)
            theater_combobox = ttk.Combobox(choose_cinema_frame, values = ["Cinema 4 - P350.00"])
            theater_combobox.grid(row = 1, column = 0)
            
            quantity_label = tkinter.Label(choose_cinema_frame, text = "Quantity")
            quantity_spinbox = tkinter.Spinbox(choose_cinema_frame, from_ = 1, to = 5)
            quantity_label.grid(row = 0, column = 1)
            quantity_spinbox.grid(row = 1, column = 1)

            for widget in choose_cinema_frame.winfo_children():
                widget.grid_configure(padx = 10, pady = 5)

        else:
            messagebox.showerror("Error", "Please choose a movie.")


    next_button = tkinter.Button(choose_movie_frame, text = "Next", command = proceed)
    next_button.grid(row = 3, column = 1)

    for widget in choose_movie_frame.winfo_children():
        widget.grid_configure(padx = 10, pady = 5)

#New window for admin page that will let us know the sales
def admin():
    window4 = tkinter.Toplevel()
    window4.title("Admin Log-In")
    window4.config(width = 300, height = 200)
    
    frame = tkinter.Frame(window4)
    frame.pack()
    
    #Destroy the window
    def logOut():
        window4.destroy()
        
    #Read and totalo the quantity and sales of movie tickets in each cinema
    def totalSales():
        window5 = tkinter.Toplevel()
        window5.title("Total Sales")
        window5.config(width = 300, height = 200)
        
        total_frame = tkinter.Frame(window5)
        total_frame.pack()
        
        manila_frame = tkinter.LabelFrame(total_frame, text = "Manila Branch Sales")
        quezon_frame = tkinter.LabelFrame(total_frame, text = "Quezon City Sales")
        manila_frame.grid(row = 0, column = 0, sticky = "news", padx= 10, pady = 25)
        quezon_frame.grid(row = 1, column = 0, sticky = "news", padx = 10, pady = 25)
        
        tickets = 0
        price = 350.00
        
        for record in records_M:
            tickets += record[5]
            total = price*tickets
        
        total_tix_M = tkinter.Label(manila_frame, text = f"Total Tickets Sold: {tickets}")
        total_tix_M.grid(row = 0, column = 0)
        
        total_price_M = tkinter.Label(manila_frame, text = f"Total Sales: ₱{total}")
        total_price_M.grid(row = 1, column = 0)
        
        for widget in manila_frame.winfo_children():
            widget.grid_configure(padx = 100, pady = 5)
            
        tickets = 0
        price = 350.00
        
        for record in records_Q:
            tickets += record[5]
            total = price*tickets
            
        total_tix_Q = tkinter.Label(quezon_frame, text = f"Total Tickets Sold: {tickets}")
        total_tix_Q.grid(row = 0, column = 0)
        
        total_price_Q = tkinter.Label(quezon_frame, text = f"Total Sales: ₱{total}")
        total_price_Q.grid(row = 1, column = 0)
        
        for widget in quezon_frame.winfo_children():
            widget.grid_configure(padx = 100, pady = 5)
    
    #Admin page widgets
    sales_frame = tkinter.LabelFrame(frame, text = "Sales")
    sales_frame.grid(row = 0, column = 0, sticky = "news", padx = 5, pady = 5)
    
    sales_button = tkinter.Button(sales_frame, text = "Total Sales", command = totalSales)
    sales_button.grid(row = 0, column = 0, padx = 10, pady = 10)
    
    log_out = tkinter.Button(sales_frame, text = "Log-out", command = logOut)
    log_out.grid(row = 0, column = 1)

    #Styles the treeview(table)
    style = ttk.Style()

    style.theme_use('default')

    style.configure("Treeview", 
        background = "#D3D3D3",
        foreground = "black",
        rowheight = 25,
        fieldbackground = "#D3D3D3"
        )
    
    #Treeview for Manila branch sales
    def sales_manila():
        
        global records_M
        
        tree_frame1 = tkinter.LabelFrame(frame, text = "KEME Cinema - Manila Sales")
        tree_frame1.grid(row = 1, column = 0)

        tree_scroll = tkinter.Scrollbar(tree_frame1)
        tree_scroll.pack(side = "right", fill = "y")

        my_tree =  ttk.Treeview(tree_frame1, yscrollcommand = tree_scroll.set, selectmode = "extended")
        my_tree.pack()

        tree_scroll.config(comman = my_tree.yview)

        my_tree['columns'] = ("Name", "Surname","Gender", "Number", "Movie", "Quantity", "Theater", "Month", "Day", "Year", "Time")

        my_tree.column('#0', width = 0, stretch = 0)
        my_tree.column("Name", anchor = 'w', width = 90)
        my_tree.column("Surname", anchor = 'w', width = 90)
        my_tree.column("Gender", anchor = 'w', width = 50)
        my_tree.column("Number", anchor = 'w', width = 100)
        my_tree.column("Movie", anchor = 'w', width = 220)
        my_tree.column("Quantity", anchor = 'center', width = 50)  
        my_tree.column("Theater", anchor = 'w', width = 140)
        my_tree.column("Month", anchor = 'w', width = 80)
        my_tree.column("Day", anchor = 'center', width = 35)
        my_tree.column("Year", anchor = 'center', width = 50)
        my_tree.column("Time", anchor = 'w', width = 60)

        my_tree.heading("#0", text = "", anchor = 'w')
        my_tree.heading("Name", text = "Name", anchor = 'w')
        my_tree.heading("Surname", text = "Surname", anchor = 'w')
        my_tree.heading("Gender", text = "Gender", anchor = 'w')
        my_tree.heading("Number", text = "Number", anchor = 'w')
        my_tree.heading("Movie", text = "Movie", anchor = 'w')
        my_tree.heading("Quantity", text = "Quantity", anchor = 'w')
        my_tree.heading("Theater", text = "Theater", anchor = 'w')
        my_tree.heading("Month", text = "Month", anchor = 'w')
        my_tree.heading("Day", text = "Day", anchor = 'w')
        my_tree.heading("Year", text = "Year", anchor = 'w')
        my_tree.heading("Time", text = "Time", anchor = 'w')

        my_tree.tag_configure('oddrow', background = "white")
        my_tree.tag_configure('evenrow', background = "light green")

        conn = sqlite3.connect('cinema.db')

        c = conn.cursor()

        c.execute("SELECT * FROM Buyers_Data_Manila")
        records_M = c.fetchall()

        conn.commit()

        conn.close()

        count = 0

        for record in records_M:
            if count % 2 == 0:
                my_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10]), tags = ('evenrow',))
            else:
                my_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10]), tags = ('oddrow',))

            count += 1
        
    #Quezon City Branch sales
    def sales_quezon():
        
        global records_Q
        
        tree_frame2 = tkinter.LabelFrame(frame, text = "KEME Cinema - Quezon City Sales")
        tree_frame2.grid(row = 2, column = 0)

        tree_scroll2 = tkinter.Scrollbar(tree_frame2)
        tree_scroll2.pack(side = "right", fill = "y")

        my_tree2 =  ttk.Treeview(tree_frame2, yscrollcommand = tree_scroll2.set, selectmode = "extended")
        my_tree2.pack()

        tree_scroll2.config(comman = my_tree2.yview)

        my_tree2['columns'] = ("Name", "Surname","Gender", "Number", "Movie", "Quantity", "Theater", "Month", "Day", "Year", "Time")

        my_tree2.column('#0', width = 0, stretch = 0)
        my_tree2.column("Name", anchor = 'w', width = 90)
        my_tree2.column("Surname", anchor = 'w', width = 90)
        my_tree2.column("Gender", anchor = 'w', width = 50)
        my_tree2.column("Number", anchor = 'w', width = 100)
        my_tree2.column("Movie", anchor = 'w', width = 220)
        my_tree2.column("Quantity", anchor = 'center', width = 50)  
        my_tree2.column("Theater", anchor = 'w', width = 140)
        my_tree2.column("Month", anchor = 'w', width = 80)
        my_tree2.column("Day", anchor = 'center', width = 35)
        my_tree2.column("Year", anchor = 'center', width = 50)
        my_tree2.column("Time", anchor = 'w', width = 60)

        my_tree2.heading("#0", text = "", anchor = 'w')
        my_tree2.heading("Name", text = "Name", anchor = 'w')
        my_tree2.heading("Surname", text = "Surname", anchor = 'w')
        my_tree2.heading("Gender", text = "Gender", anchor = 'w')
        my_tree2.heading("Number", text = "Number", anchor = 'w')
        my_tree2.heading("Movie", text = "Movie", anchor = 'w')
        my_tree2.heading("Quantity", text = "Quantity", anchor = 'w')
        my_tree2.heading("Theater", text = "Theater", anchor = 'w')
        my_tree2.heading("Month", text = "Month", anchor = 'w')
        my_tree2.heading("Day", text = "Day", anchor = 'w')
        my_tree2.heading("Year", text = "Year", anchor = 'w')
        my_tree2.heading("Time", text = "Time", anchor = 'w')

        my_tree2.tag_configure('oddrow', background = "white")
        my_tree2.tag_configure('evenrow', background = "light green")

        conn = sqlite3.connect('cinema.db')

        c = conn.cursor()

        c.execute("SELECT * FROM Buyers_Data_Quezon")
        records_Q = c.fetchall()

        conn.commit()

        conn.close()

        count = 0

        for record in records_Q:
            if count % 2 == 0:
                my_tree2.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10]), tags = ('evenrow',))
            else:
                my_tree2.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10]), tags = ('oddrow',))

            count += 1
            
    sales_manila()
    sales_quezon()
            


#main window widgets
title = tkinter.Label(text = "Movie Booking System", font = ("Arial 20 bold"))
title.pack()

frame = tkinter.Frame(window)
frame.pack()

buyer_frame = tkinter.LabelFrame(frame, text = "Buy Ticket/s")
buyer_frame.grid(row = 0, column = 0, sticky = "news")

choose_label = tkinter.Label(buyer_frame, text = "Choose Cinema")
choose_label.grid(row = 0, column = 0)

cinema1_button = tkinter.Button(buyer_frame, text = "KEME Cinema - Manila", command = manila)
cinema2_button = tkinter.Button(buyer_frame, text = "KEME Cinema - Quezon City", command = quezon)
cinema1_button.grid(row = 1, column = 0, padx = 100, pady = 20)
cinema2_button.grid(row = 2, column = 0, padx = 100, pady = 20)

#Log-in to enter the admin page and see the sales
def login():

    username = un_entry.get()
    password = pw_entry.get()

    if username == "admin":
        if password == "admin":
            admin()
        else:
            messagebox.showerror("Error", "Wrong Credentials!")
    else:
            messagebox.showerror("Error", "Wrong Credentials!")

#Admin Log-in
admin_frame = tkinter.LabelFrame(frame, text = "Admin Log-in")
admin_frame.grid(row = 1, column = 0, sticky = "news", padx = 10, pady = 10)

un_label = tkinter.Label(admin_frame, text = "Username")
un_entry = tkinter.Entry(admin_frame)
pw_label = tkinter.Label(admin_frame, text = "Password")
pw_entry = tkinter.Entry(admin_frame)
un_label.grid(row = 0, column = 0)
un_entry.grid(row = 1, column = 0, padx = 100, pady = 20)
pw_label.grid(row = 2, column = 0)
pw_entry.grid(row = 3, column = 0, padx = 100, pady = 20)

admin_button = tkinter.Button(admin_frame, text = "Log-in", command = login)
admin_button.grid(row = 4, column = 0, pady = 20)

for widget in window.winfo_children():
    widget.pack_configure(padx = 20, pady = 20)

window.mainloop()