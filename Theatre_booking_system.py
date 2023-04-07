'''
For the code to work properly:-
A database name theatre (blank or filled) should be made with
a table name theatre (blank or filled) should be present.
code for database and table :- 
drop database theatre;
create database theatre;
use theatre;
create table theatre (
	Movie_Code char(4) NOT NULL PRIMARY KEY,
	Movie_Name varchar(30) NOT NULL,
	Date char(12),
	Time char(20),
	Hall_No int(1),
	Price float(5,2)
);
'''
# Importing required modules
import mysql.connector as sqltor
import tkinter as tk
import time
# Choice for console
console = None
# starting introduction
def start():
    global console
    print("\n"*100)
    console = input("Press Enter")
    
    
    
# function for introduction
def intro():
	# for printing text below
    print("""
 __      __          ___                                        
/\\ \\  __/\\ \\        /\\_ \\                                       
\\ \\ \\/\\ \\ \\ \\     __\\//\\ \\     ___    ___     ___ ___      __   
 \\ \\ \\ \\ \\ \\ \\  /'__`\\\\ \\ \\   /'___\\ / __`\\ /' __` __`\\  /'__`\\ 
  \\ \\ \\_/ \\_\\ \\/\\  __/ \\_\\ \\_/\\ \\__//\\ \\L\\ \\/\\ \\/\\ \\/\\ \\/\\  __/ 
   \\ `\\___x___/\\ \\____\\/\\____\\ \\____\\ \\____/\\ \\_\\ \\_\\ \\_\\ \\____\\
    '\\/__//__/  \\/____/\\/____/\\/____/\\/___/  \\/_/\\/_/\\/_/\\/____/
                                                                
                                                                
                           __                                   
                          /\\ \\__                                
                          \\ \\ ,_\\   ___                         
                           \\ \\ \\/  / __`\\                       
                            \\ \\ \\_/\\ \\L\\ \\                      
                             \\ \\__\\ \\____/                      
                              \\/__/\\/___/                       
                                                                
                                                                
__/\\\\\\\\\\\\\\\\\\\\\\\\\\____/\\\\\\________________________________________________________________________                                      
 _\\/\\\\\\/////////\\\\\\_\\/\\\\\\________________________________________________________________________                                     
  _\\/\\\\\\_______\\/\\\\\\_\\/\\\\\\_____________________________________________________/\\\\\\_______________                                    
   _\\/\\\\\\\\\\\\\\\\\\\\\\\\\\/__\\/\\\\\\_____________/\\\\\\\\\\________/\\\\\\\\\\\\\\\\___/\\\\/\\\\\\\\\\\\___\\///___/\\\\\\____/\\\\\\_                                   
    _\\/\\\\\\/////////____\\/\\\\\\\\\\\\\\\\\\\\____/\\\\\\///\\\\\\____/\\\\\\/////\\\\\\_\\/\\\\\\////\\\\\\___/\\\\\\_\\///\\\\\\/\\\\\\/__                                  
     _\\/\\\\\\_____________\\/\\\\\\/////\\\\\\__/\\\\\\__\\//\\\\\\__/\\\\\\\\\\\\\\\\\\\\\\__\\/\\\\\\__\\//\\\\\\_\\/\\\\\\___\\///\\\\\\/____                                 
      _\\/\\\\\\_____________\\/\\\\\\___\\/\\\\\\_\\//\\\\\\__/\\\\\\__\\//\\\\///////___\\/\\\\\\___\\/\\\\\\_\\/\\\\\\____/\\\\\\/\\\\\\___                                
       _\\/\\\\\\_____________\\/\\\\\\___\\/\\\\\\__\\///\\\\\\\\\\/____\\//\\\\\\\\\\\\\\\\\\\\_\\/\\\\\\___\\/\\\\\\_\\/\\\\\\__/\\\\\\/\\///\\\\\\_                               
        _\\///______________\\///____\\///_____\\/////_______\\//////////__\\///____\\///__\\///__\\///____\\///__                              
__/\\\\\\\\____________/\\\\\\\\________________/\\\\\\\\\\\\_______________________________________/\\\\\\\\\\\\_________________________________        
 _\\/\\\\\\\\\\\\________/\\\\\\\\\\\\_______________\\////\\\\\\______________________________________\\////\\\\\\_________________________________       
  _\\/\\\\\\//\\\\\\____/\\\\\\//\\\\\\__________________\\/\\\\\\________/\\\\\\_______/\\\\\\___/\\\\\\\\\\\\\\\\\_____\\/\\\\\\_________________________________      
   _\\/\\\\\\\\///\\\\\\/\\\\\\/_\\/\\\\\\__/\\\\\\____/\\\\\\____\\/\\\\\\_____/\\\\\\\\\\\\\\\\\\\\\\_\\///___/\\\\\\/////\\\\\\____\\/\\\\\\________/\\\\\\\\\\\\\\\\___/\\\\\\____/\\\\\\_     
    _\\/\\\\\\__\\///\\\\\\/___\\/\\\\\\_\\/\\\\\\___\\/\\\\\\____\\/\\\\\\____\\////\\\\\\////___/\\\\\\_\\/\\\\\\\\\\\\\\\\\\\\_____\\/\\\\\\______/\\\\\\/////\\\\\\_\\///\\\\\\/\\\\\\/__    
     _\\/\\\\\\____\\///_____\\/\\\\\\_\\/\\\\\\___\\/\\\\\\____\\/\\\\\\_______\\/\\\\\\______\\/\\\\\\_\\/\\\\\\//////______\\/\\\\\\_____/\\\\\\\\\\\\\\\\\\\\\\____\\///\\\\\\/____   
      _\\/\\\\\\_____________\\/\\\\\\_\\/\\\\\\___\\/\\\\\\____\\/\\\\\\_______\\/\\\\\\_/\\\\__\\/\\\\\\_\\/\\\\\\____________\\/\\\\\\____\\//\\\\///////______/\\\\\\/\\\\\\___  
       _\\/\\\\\\_____________\\/\\\\\\_\\//\\\\\\\\\\\\\\\\\\___/\\\\\\\\\\\\\\\\\\____\\//\\\\\\\\\\___\\/\\\\\\_\\/\\\\\\__________/\\\\\\\\\\\\\\\\\\__\\//\\\\\\\\\\\\\\\\\\\\__/\\\\\\/\\///\\\\\\_ 
        _\\///______________\\///___\\/////////___\\/////////______\\/////____\\///__\\///__________\\/////////____\\//////////__\\///____\\///__
""")
    time.sleep(3)
    print("\n\nSelect the movie which you would like to book :-\n\n")
	# fetching distinct movie names from database theatre table theatre
    cursor.execute("select distinct Movie_Name,Movie_Code from theatre group by Movie_Name")
    # movies names will be stored in this variable in form of tuples inside list
    movies = cursor.fetchall()
    
    if movies:
    # displaying movies names in a tidy format
        for i in range(len(movies)):
            print("\t\t" + movies[i][0] + "  (" + movies[i][1][0:3] + ")" + "\n")
    
    else:
        error("\n\t\tNo Movie data has been found from the database")
# for displaying details of all movies
def singlemoviedetails():
    for i in smov:
    
        print("\n\tMovie Name : ", i[1],
              "\n\tMovie Code : ", i[0],
              "\n\tDate : ", i[2],
              "\n\tTime : ", i[3],
              "\n\tHall No. : ", i[4],
              "\n\tPrice : Rs." + str(i[5]))
# for displaying details for the chosen movie
def chosenmoviedetails(seat="Not Validated Yet"):
    print("\n\n\tMovie Name :", choice[1],
          "\n\tMovie Code :", choice[0],
          "\n\tDate :", choice[2],
          "\n\tTime :", choice[3],
          "\n\tHall No. :", choice[4],
          "\n\tPrice : Rs." + str(choice[5]),
    	  "\n\tSeat :", seat)
# if any error is occurred, this function will ask to restart the program
def error(text):
	# printing the message for which the error has occurred
    print(text)
   # asking to restart program
    x = input("\n\tWould you like to restart/book another ticket? (y/n) : ")
    # if user agrees or disagrees, it raises different types of errors which would help us in 
    # continuing or breaking the program accordingly
    if x=='y' or x=='Y':
    
        raise EOFError
        
    else:
    
        raise TypeError
# this function is for showing gui of the seats
def seats():
	# asking for user's choice
    x = input("\nWould you like to check reserved seats? : ")
    
    if (x == "Y" or x == "y"):
    	# using tkinter module for gui
    	# setting tkinter variable
        seat = tk.Tk()
        # setting geometry, title of the window
        seat.geometry("900x950")
        seat.title("Choose your seat")
        # for the text at top of the buttons (seats)
        tk.Label(seat, text="White = Not Reserved, Red = Reserved", font=("Ariel Bold", 15)).grid(columnspan=14,ipady=25, column=0,row=0)
        tk.Label(seat, text="----------Consider the screen to be on Top------------", font=("Times", 20),).grid(columnspan=14, column=0, row=2)
        # fetching seats from the requested table
        cursor.execute("select * from {}".format(choice[0]))
        # this variable stores seats
        cmovie = cursor.fetchall()
        # loop for arranging buttons in a grid format
        for i in range(0, 15):
            for j in range(0, 14):
            	# checking if the seat is reserved.
            	# if it is, colour bg of that button as red
            	# else colour bg of that button as white
                if cmovie[i][j][0] == "R":
                    tk.Button(seat, text=cmovie[i][j][1:], font=("Tahoma", 15), bg="red").grid(row=i + 3, column=j + 3)
                else:
                    tk.Button(seat, text=cmovie[i][j], font=("Tahoma", 15), bg="white").grid(row=i + 3, column=j + 3)
        # tkinter mainloop
        tk.mainloop()
# for ending
def end():
	# printing the below text
	print("""
                                                                                           
_/_/_/_/_/  _/    _/    _/_/    _/      _/  _/    _/      _/      _/    _/_/    _/    _/   
   _/      _/    _/  _/    _/  _/_/    _/  _/  _/          _/  _/    _/    _/  _/    _/    
  _/      _/_/_/_/  _/_/_/_/  _/  _/  _/  _/_/              _/      _/    _/  _/    _/     
 _/      _/    _/  _/    _/  _/    _/_/  _/  _/            _/      _/    _/  _/    _/      
_/      _/    _/  _/    _/  _/      _/  _/    _/          _/        _/_/      _/_/         
		                    *****************
		               ******               ******
		           ****                           ****
		        ****                                 ***
		      ***                                       ***
		     **           ***               ***           **
		   **           *******           *******          ***
		  **            *******           *******            **
		 **             *******           *******             **
		 **               ***               ***               **
		**                                                     **
		**       *                                     *       **
		**      **                                     **      **
		 **   ****                                     ****   **
		 **      **                                   **      **
		  **       ***                             ***       **
		   ***       ****                       ****       ***
		     **         ******             ******         **
		      ***            ***************            ***
		        ****                                 ****
		           ****                           ****
		               ******               ******
		                    *****************
\t*************** Thanks for using our service ******************
""")
	time.sleep(5)
def exit():
    # for exiting admin console
    print("\n\nexiting...")
    time.sleep(2)
    raise TypeError
def help():
    # for help in admin console
    print("""
    
      -:Phoenix admin console help page :-
    
    
    show : show the contents of theatre table
    insert : insert a row for movie details
    delete : delete a row from table
    help : show this help message
    exit : exit the console
    
    
    """)
while True:
    # Main program starts here
    start()
    mycon = sqltor.connect(host='localhost', user='root', passwd='login', database='theatre')
    cursor = mycon.cursor()
    # condition for entering into admin console
    if console == "admin":
        while True:
            # checking for password
            password = input("Enter admin password : ")
            if password == "loginn":
                break
            print("\n\n\n\t\t!!!!!!!!!! INCORRECT PASSWORD !!!!!!!!!!!!!\n\n\n\n")
            continue
        while True:
            try:
                # Taking some time to give the user message for admin console
                print("\n"*100)
                print("You are being redirected to admin console\nthis feature should not be operated by customers")
                print("\n"*10)
                
                time.sleep(5)
                
                print("\n"*100)
                print("""
                
                
       _____       .___      .__         _________                            .__          
      /  _  \\    __| _/_____ |__| ____   \\_   ___ \\  ____   ____   __________ |  |   ____  
     /  /_\\  \\  / __ |/     \\|  |/    \\  /    \\  \\/ /  _ \\ /    \\ /  ___/  _ \\|  | _/ __ \\ 
    /    |    \\/ /_/ |  Y Y  \\  |   |  \\ \\     \\___(  <_> )   |  \\\\___ (  <_> )  |_\\  ___/ 
    \\____|__  /\\____ |__|_|  /__|___|  /  \\______  /\\____/|___|  /____  >____/|____/\\___  >
            \\/      \\/     \\/        \\/          \\/            \\/     \\/                \\/ 
                
                
                
                
                
                
                
                
                
                
                
                
                
                """)
                print("\n\n")
                # Main program for admin console starts in this loop
                while True:
                    # prompt
                    inp = input("admin@phoenix:>>> ")
                    
                    # directing input to correct block
                    if inp == 'help':
                        help()
                        
                    elif inp == 'show':
                        print("\n\n")
                        cursor.execute("select * from theatre")
                        shows = cursor.fetchall()
                        for show in shows:
                            print(show)
                        print("\n\n")
                        
                    elif inp == 'delete':
                        found = False
                        err = ""
                        cursor.execute("show tables")
                        codes = cursor.fetchall()
                        code = input("\n\nEnter code of show to delete : ")
                        print("\n\n\n")
                        # incase the entered code does not exist
                        if code != 'theatre':
                            for i in codes:
                                if i[0] == code:
                                    found = True
                        # if code not found
                        if found == False:
                            print("Code not Found\n\n")
                            continue
                        cursor.execute("delete from theatre where Movie_Code = '{}'".format(code))
                        cursor.execute("drop table {}".format(code))
                        print("Tuple with code",code,"has been deleted\n\n")
                    elif inp == 'insert':
                        # process for insertion starts
                        cont = True
                        cursor.execute("show tables")
                        codes = cursor.fetchall()
                        # syntax for code
                        print("""
                        
                        FOLLOW THE FOLLOWING SYNTAX FOR INSERTION:-
                        
                        for code:-
                        
                        abcx
                        
                        a,b,c and x should be a combination of unique characters
                        
                        note for same movies first three character should be same
                        
                        example: - avg1
                                   avg2
                        """)

                        # enter codes simutaneously checking for conditions             
                        code = input("Enter your show code : ")
                        if len(code) > 4:
                            cont = False
                            err = code+' - length exceeded'
                            print("\n\n\t\t***ERROR*** ",err,"\n\n")
                            continue
                        name = input("Enter Movie Name : ")
                        if len(name) > 30:
                            cont = False
                            err = name+' - length exceeded'
                            print("\n\n\t\t***ERROR*** ",err,"\n\n")
                            continue
                        date = input("Enter Movie Date (Ex - '28 Feb 2002') : ")
                        if len(date) > 12:
                            cont = False
                            err = date+' - length exceeded'
                            print("\n\n\t\t***ERROR*** ",err,"\n\n")
                            continue
                        Time = input("Enter Movie Time (Ex - '10:30 AM - 12:00 PM') : ")
                        if len(Time) > 20:
                            cont = False
                            err = Time+' - length exceeded'
                            print("\n\n\t\t***ERROR*** ",err,"\n\n")
                            continue
                        try:
                            hall = int(input("Enter Hall No. : "))
                            price = float(input("Enter Price : "))
                        except TypeError:
                            print("\n\n\t\tError Occurred - Enter numerical values in Hall No. and Price\n\n")
                        for i in codes:
                            if i[0] == code:
                                print("Length Exceeded")
                                err = 'Code Already Exists'
                                cont = False
                        if cont == True:
                            # After everything is correct, finally entering and committing the insertion
                            cursor.execute("insert into theatre values('{}','{}','{}','{}',{},{})".format(code,name,date,Time,hall,price))
                            mycon.commit()
                            cursor.execute("create table {} (A char(4), B char(4), C char(4), D char(4), E char(4), F char(4), G char(4), H char(4), I char(4),J char(4), K char(4),L char(4), M char(4), N char(4))".format(code))
                            # Entering seats
                            for i in range(1,19):
                                cursor.execute("insert into {code} values ('A{i}','B{i}','C{i}','D{i}','E{i}','F{i}','G{i}','H{i}','I{i}','J{i}','K{i}','L{i}','M{i}','N{i}')".format(code=code,i=i))
                                mycon.commit()
                        
                        elif cont == False:
                            print("\n\n\tERROR OCCURRED\n\t"+err) 
                    elif inp == 'exit':
                        
                        exit()
                    else:
                        print("\n\nUnrecognized command",inp,"\nType 'help' to show available commands\n\n")
            except EOFError:
                continue
            except TypeError:
                break
            except ValueError:
                    print("\n\n\t\tERROR : PLEASE ENTER CORRECT DATA TYPE")
                    time.sleep(5)
                    continue
    else:
        # For Customers, the main program starts here
        while True:
            try:
                intro()
                # Single movie choice
                n = input("\nEnter your choice : ")
                cursor.execute("select * from theatre where Movie_Code like '{}_'".format(n))
                smov = cursor.fetchall()
                if not smov:
                    # if movie with code is not found
                    error("\n\tNo Movie with code '"+n+"' has been found\n")
                print("\n"*50,"\tYou Entered :",n,"\n\n")
                print("\nChoose your desired show : \n")
                singlemoviedetails()
                # single movie code
                c = input("\nEnter your desired movie code : ")
                print("\n"*50)
                print("\tYou Entered :",c)
                choice = ""
                # finding selected movie in database
                for i in smov:
                    if i[0] == c:
                        choice = i
                if not choice:
                    error("\n\tSorry, no movie has been found")
                chosenmoviedetails()
                # Gui for choosing seats
                seats()
                seat = input("Enter your desired seat : ")
                seat = seat.upper()
                print("\tValidating Seat",end="")
                for i in range(5):
                    time.sleep(0.5)
                    print(".",end="")
                print()
                status = 'invalid'
                # validating seats
                cursor.execute("select * from {}".format(choice[0]))
                allseats = cursor.fetchall()
                for i in allseats:
                    for j in i:
                        if j == seat:
                            status = 'valid'
                        elif j == "R"+seat:
                            status = 'reserved'
                if status == 'invalid':
                    error("\n\tNo seat found. Please enter correct seat code")
                elif status == 'reserved':
                    error("\n\tSorry, The requested seat is already reserved.")
                else:
                    print("\n\t****Seat Validated*****")
                # final confirmation
                chosenmoviedetails(seat)
                
                z = input("\nPress 'y' to confirm : ")
                
                if z == "y" or z == "Y":
                    cursor.execute("update {table} set {c} = 'R{c}{r}' where {c} = '{c}{r}'".format(table=choice[0], c=seat[0], r=seat[1]))
                    mycon.commit()
                    
                    print("\n\tYour ticket has been booked.\
                          \n\n\t\tBooking ID : ", time.time(),
                          "\n\t\tMovie Name :",choice[1],
                          "\n\t\tDate :", choice[2],
                          "\n\t\tTime", choice[3],
                          "\n\t\tHall No :", choice[4],
                          "\n\t\tPrice : Rs." + str(choice[5]),
                          "\n\t\tSeat :", seat)
                          
                else:
                
                    error("\n\n\t********* BOOKING HAS BEEN CANCELED BY USER ***********")
                error("\n\n\t********* YOUR SHOW HAS BEEN BOOKED SUCCESSFULLY **********")

            # Error Handling
            except EOFError:
                continue
            except TypeError:
                break
            except ValueError:
                print("\n\n\t\tERROR : PLEASE ENTER CORRECT DATA TYPE")
                time.sleep(5)
                continue
        # Ending message    
        end()
