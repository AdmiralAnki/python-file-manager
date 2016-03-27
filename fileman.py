from tkinter import *
import os
from tkinter import messagebox as msg				#module for messagebox

#create new window
myMan = Tk()

def fileio():
	try:
		finame=(fname.get())
		fo = open(finame, "r+")
		str = fo.read();
		#file label
		msg.showinfo("FILE READER", "THE CONTENT: \n %s" %(str))
	except IOError:
		msg.showinfo("Error Message", "Sorry File not found!!")
	return

def cud():
	cd = os.getcwd()
	msg.showinfo("CURRENT DIRECTORY!", "The current directory:\n %s " %(cd))
	return

def chd():
	try:
		newna=(dname.get())
		os.chdir(newna)
	except OSError:
		msg.showinfo("Error Message", "Enter a valid dir name")
	except FileNotFoundError:
		msg.showinfo("Error Message", "Sorry directory not found!!")
	return

def filew():
	try:
		nfiname=(nfname.get())
		fi= open(nfiname,"w")
		nfic=(nfcon.get())
		fi.write(" %s " %(nfic));
		msg.showinfo("SUCCESS MESSAGE", "CONTENT WRITTEN" )
	except IOError:
		msg.showinfo("Error Message", "Sorry File not found!!")

	return

#modify root window					
myMan.title("File manager")		

#window dimensions
myMan.geometry("500x500")	

#inputs
dname=StringVar()	
fname=StringVar()
nfname=StringVar()
nfcon=StringVar()

#label heading
lable = Label(myMan, text="Welcome to AK File manager" ,font=("Helvetica", 15,"bold","italic"),fg='red').grid(row=0,column=1)

"""directory stuff"""
# D HEADING
lable0 = Label(myMan, text="DIRECTORY NAVIGATION",font=("Helvetica", 9,"bold")).grid(row=2,column=1)	
#button for detecting directory
button3 = Button(myMan,text ='Check current dir',font=("Helvetica", 7,"bold"),command=cud).grid(row=9,column=1)
#directory change label
lable2 = Label(myMan, text="Enter directory name",font=("Helvetica", 9,"bold")).grid(row=8,column=0)			
#direcotry chNGE ENTRY
dnam = Entry(myMan,textvariable=dname).grid(row=8,column=1)
#button for directory
button2 = Button(myMan,text ='Choose Directory',font=("Helvetica", 7,"bold"),command=chd).grid(row=9,column=0) 	

"""file stuff"""
#FILE HEADIN
able3 = Label(myMan, text="READ FILE",font=("Helvetica", 9,"bold")).grid(row=10,column=1)
#file label
lable3 = Label(myMan, text="Enter file name",font=("Helvetica", 9,"bold")).grid(row=12,column=0)
#file entry
fnam = Entry(myMan,textvariable=fname).grid(row=12,column=1)
#button for files
button1 = Button(myMan,text ='show file content',font=("Helvetica", 7,"bold"),command=fileio).grid(row=13,column=0)

"""writing to files"""
lable8 = Label(myMan, text="WRITING TO FILE",font=("Helvetica", 9,"bold")).grid(row=17,column=1)

#file op label
lable9 = Label(myMan, text="Enter file name to write ",font=("Helvetica", 9,"bold")).grid(row=18,column=0)

#file entry
nfnam = Entry(myMan, textvariable=nfname).grid(row=18,column=1)

lable10 = Label(myMan, text="Enter content",font=("Helvetica", 9,"bold")).grid(row=20,column=0)
nfc = Entry(myMan, textvariable=nfcon).grid(row=20,column=1)

#button for files
button4 = Button(myMan,text ='go!!',font=("Helvetica", 7,"bold"),command=filew).grid(row=21,column=0)


#kick off the event loop
myMan.mainloop()
