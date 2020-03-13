from gtts import *
import sys
import os
import string
import re

from tkinter import*
from tkinter import messagebox
import tkinter as tk
import datetime

from collections import namedtuple
import csv
from tkinter import Message
import pandas as pd


### datetime ###
date=datetime.datetime.now()#.date()
date=str(date.strftime("%d/%m/%Y %H:%M:%S"))



########### WIN 5 ###############
def Search(event):
    criteria=text_win5.get()
    with open("BookCustomers2.csv","r",encoding="utf-8") as f:
        try:
            for line in f:
                line = line.rstrip()
                if line.upper().find(criteria.upper()) != -1:
                    reg,name,address,mob,email = line.split(",")
                    print("Reg: "'{0: <5}\n'.format(reg) + "Name: " '{0: <5}\n'.format(name) +"Address: " '{0: <5}\n'.format(address) +"Mobile phone: " '{0: <5}\n'.format(mob) + "Email: " '{0: <5}\n'.format(email))
                    string_to_display="Reg: "'{0: <5}\n'.format(reg) + "Name: " '{0: <5}\n'.format(name) +"Address: " '{0: <5}\n'.format(address) +"Mobile phone: " '{0: <5}\n'.format(mob) + "Email: " '{0: <5}\n'.format(email)
                    label_2=Label(bottomframe3,font='Gupter 13', width=80,bg='gray26',fg='gray90')
                    label_2['text']=string_to_display
                    label_2.pack(side=TOP,anchor=NW)

        except:
            ValueError

        else:
            if line.upper().find(criteria.upper()) == -1:
                print("no such")
                string_to_display2="There is no such criteria in database!"
                label_2=Label(bottomframe3,font='Gupter 15 bold', width=80,bg='gray26',fg='gray90')
                label_2['text']=string_to_display2
                label_2.pack(side=TOP,anchor=NW)
                messagebox.showerror("Info","No such criteria in database!")
                sys.exit()
            #     reg,name,address,mob,email = line.split(",")
            #     print("no such")

        #     if line.upper().find(criteria.upper()) == -1:
        #         print ("There is no such criteria in database!")
        #         string_to_display2="There is no such criteria in database!"
        #         label_2=Label(bottomframe3,font='Gupter 15 bold', width=80,bg='gray26',fg='gray90')
        #         label_2['text']=string_to_display2
        #         label_2.pack(side=TOP,anchor=NW)
        #         messagebox.showerror("Info","No such criteria in database!")
        #         sys.exit()





########## END WIN 5 #############
################# WIN5 #######################
def win5():
    global text_win5,bottomframe3

    root5 = Tk()
    #frames
    topframe2 = Frame(root5,height=50, bg='gray26')
    topframe2.pack(fill=X)
    bottomframe2=Frame(root5,height=150, bg='gray90')
    bottomframe2.pack(fill=X)
    bottomframe3=Frame(root5,height=300, bg='gray26')
    bottomframe3.pack(fill=X)
    #top freim design
    topheading2=Label(topframe2,text='SEARCH FOR CUSTOMERS IN DATABASE', font='Gupter 15 bold',bg='gray26',fg='gray90')
    topheading2.place(x=200,y=20)
#####################################
    #inside window2
    zero_label=Label(bottomframe2,text="Enter a search criteria",width=26,font='Gupter 13',bg='gray90',fg='black')
    zero_label.grid(row=1,column=0,padx=20,pady=30)
    text_win5=Entry(bottomframe2,width=20,bd=6,font='Gupter 13',fg='grey11')
    text_win5.grid(row=1,column=1,padx=1, pady=30)

    but = Button(bottomframe2,text="SEARCH",width=10,height=1,bd=6)
    but.grid(row=2,column=1,padx=10,pady=2)
    but.bind("<Button-1>",Search)

    first_label=Label(bottomframe3,text="Result",width=10,font='Gupter 13',bg='gray26',fg='gray90')
    first_label.place(x=330,y=80)
    #out5=Label(bottomframe3,font='Gupter 13',width=70,height=14,bd=6,fg='grey11',text='',relief=SUNKEN)
    #out5.grid(row=1,column=1,padx=5,pady=30,sticky=W)

    root5.title("Second Window")
    root5.geometry("800x600+700+600")
    root5.resizable(width=False, height=False)
    root5.mainloop()
#######################END WIN 5 ###########################
#### ROOT #############################
root=Tk()

#frames
topframe=Frame(root, height=150, bg='gray90') #tkinter colors> http://www.science.smith.edu/dftwiki/images/3/3d/TkInterColorCharts.png
topframe.pack(fill=X)

bottomframe=Frame(root,height=500, bg='gray26')
bottomframe.pack(fill=X)

#top freim design
top_image=PhotoImage(file='database.png')
top_image_label=Label(topframe, image=top_image, bg='gray90')
top_image_label.place(x=10,y=27)

topheading=Label(topframe,text='CUSTOMERS DATABASE', font='Gupter 15 bold',bg='gray90',fg='gray25')
topheading.place(x=220,y=75)

date_label=Label(topframe, text="CURRENT DATE & TIME: "+date, font='Gupter 10 bold',bg='gray90',fg='gray25')
date_label.place(x=350,y=10)

center_image=PhotoImage(file='puzzle.png')
center_image_label=Label(bottomframe, image=center_image, bg='gray90')
center_image_label.place(x=-30,y=-60)

aboutButton=Button(bottomframe, text='SEARCH',font='Gupter 10 bold',width=25,padx=10,pady=5,borderwidth=7,activebackground="gray33",activeforeground="snow",relief=RAISED,command=win5)
aboutButton.place(x=200,y=260)


root.title("First Window")
root.geometry('650x550+300+200')
root.resizable(width=False, height=False)
root.mainloop()
