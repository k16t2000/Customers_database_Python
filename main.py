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

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from pandas import ExcelWriter
from pandas import ExcelFile
from pandas import DataFrame
import xlsxwriter

from openpyxl import load_workbook



### datetime ###
date=datetime.datetime.now()#.date()
date=str(date.strftime("%d/%m/%Y %H:%M:%S"))
# FUNCTION TO SAVE BOOK TO FILE
def SaveBook(book):
    f = open("BookCustomers2.csv","a+",encoding="utf-8")
    f.write(book[0] + ',' + book[1] + ',' + book[2] + ',' + book[3] + ',' + book[4] +'\n')
    f.close()

#  FUNCTION TO RETRIEVE A SINGLE BOOK RECORD FROM THE DATABASE
def GetRecord(input_reg):
    with open("BookCustomers2.csv","r",encoding="utf-8") as f:
         for line in f:
             line = line.rstrip()
             reg,name,address,mob,email = line.split(",")
             if (reg == input_reg):
                 return line



###### WIN1 ######
#  FUNCTION TO ADD A CUSTOMER TO THE DATABASE
def AddCustomer():

    with open("BookCustomers2.csv", "r",encoding="utf-8") as file:
        try:
            csv_file = csv.DictReader(file)
            dict=csv_file
            for row in dict:
                values=row.values()
                print(values)
                input_reg=text0_win1.get()
                if input_reg in values:
                    print("here")
                    messagebox.showinfo("Info","Register number is already exists!")
                    break
        except:
            ValueError
        else:
            if not input_reg in values:
                reg=input_reg
                name = text_win1.get()
                address = text2_win1.get()
                mob = text3_win1.get()
                email = text4_win1.get()
                Book = namedtuple("Book", "Reg Name Address Mob Email")
                newBook = Book(reg, name, address, mob, email)
                SaveBook(newBook)
                messagebox.showinfo("Info","New customer was added successfullly")


def erase():
    text0_win1.delete('0',END)
    text_win1.delete('0',END)
    text2_win1.delete('0',END)
    text3_win1.delete('0',END)
    text4_win1.delete('0',END)
#### END WIN1 ####

############## WIN2 ###########
def DisplayCompany(event):
    with open("BookCustomers2.csv","r",encoding="utf-8") as file:
        try:
            csv_file = csv.DictReader(file,delimiter=',')
            my=csv_file
            for row in my:
                values=row.values()
                input_reg=text_win2.get()
                if input_reg in values:
                    print("found")
                    print(values)
                    reg,name,address,mob,email = GetRecord(input_reg).split(",")
                    print("Reg: "'{0: <5}\n'.format(reg) + "Name: " '{0: <5}\n'.format(name) +"Address: " '{0: <5}\n'.format(address) +"Mobile phone: " '{0: <5}\n'.format(mob) + "Email: " '{0: <5}\n'.format(email))
                    out.configure(text="Reg: "'{0: <5}\n'.format(reg) + "Name: " '{0: <5}\n'.format(name) +"Address: " '{0: <5}\n'.format(address) +"Mobile phone: " '{0: <5}\n'.format(mob) + "Email: " '{0: <5}\n'.format(email))
                    break
        except:
            ValueError
        else:
            if not input_reg in values:
                print("No such!")
                messagebox.showerror("Info","No such client!")
                sys.exit()

def speak(word,lang):
    from os import system
    tts=gTTS(text=word,lang=lang)
    tts.save('voice.mp3')
    system('start voice.mp3')

def but_speak():
    with open('BookCustomers2.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            input_reg=text_win2.get()
            text="Register number is"+input_reg
            reg,name,address,mob,email = GetRecord(input_reg).split(",")
            if (reg == input_reg):
                speak(text,'en')
            else:
                result=('There is not such word')
                speak(result,'en')

def but_speak2():
    with open('BookCustomers2.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            input_reg = text_win2.get()
            reg,name,address,mob,email = GetRecord(input_reg).split(",")
            if (reg == input_reg):
                out.configure(text="Registration number is: "'{0: <5}\n'.format(reg) + "Company name is: " '{0: <5}\n'.format(name) +"Address is: " '{0: <5}\n'.format(address) +"Mobile phone is: " '{0: <5}\n'.format(mob) + "Email is: " '{0: <5}\n'.format(email))
                slova=out.cget('text')
                speak(slova,'en')
            else:
                result=('There is not such word')
                speak(result,'en')
############# END WIN2 ##############
############# WIN 3 ##########
def DeleteCustomer(event):
    input_reg2 = text_win3.get()
    f = open("BookCustomers2.csv","r+",encoding="utf-8")
    d = f.readlines()
    f.seek(0)

    for line in d:
        record = line.rstrip()
        reg,name,address,mob,email = record.split(",")
        if reg != input_reg2:
            f.write(line)
    f.truncate()
    f.close()
    print("The customer was successfully deleted from the database!")
    out2.configure(text="The customer was successfully deleted from the database!")

############ END WIN 3 ###########

############ WIN 4 ###########
def GetTotal(event):
    df = pd.read_csv('BookCustomers2.csv',sep=',', index_col=0)
    p=len(df.index)
    print("The total number of companies is: ", p)
    out3.configure(text="The total number of companies is: "+ str(p))

def ViewCustomers(event):
    df = pd.read_csv('BookCustomers2.csv',sep=',', index_col=0)
    print(df)
    out3.configure(text=df)
############ END WIN 4 ###########
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
########## END WIN 5 #############
############ WIN 6 ############
def sales(event):
    matplotlib.style.use('ggplot') #for beautiful graphics
    # reading excel
    df=pd.read_excel(r'C:\Users\37255\Desktop\algoritmi, python\kliendi_baas\Invoices.xlsx', sheet_name='sales')
    print(df.head())
    table=df[['date','company','summa','date_p','company_p','summa_p']]
    m = table.pivot_table(index=['date','date_p'])
    print("table",m.head(len(table)))#prints without indexes

    # string_to_display="Invoices in database",m.head(len(table)
    # label_2=Label(bottomframe3,font='Gupter 13', width=80,bg='gray26',fg='gray90')
    # label_2['text']=string_to_display
    # label_2.pack(side=TOP,anchor=NW)

    m.plot.bar(title='Review of sales and purchases',color=['orange','blue'],width=0.3)
    plt.xlabel('Date')
    plt.ylabel('Euro')
    plt.legend(['sales','purchases']) #add legend
    plt.xticks(rotation=-10)
    plt.show()


    # sheets=pd.read_excel(r'C:\Users\37255\Desktop\algoritmi, python\kliendi_baas\Invoices.xlsx', sheet_name=['sales','purchase'])
    # print(sheets)
    # df=pd.concat(sheets[frame] for frame in sheets.keys()) #merged 2 dataframes
    # print(df)#prints 2 tables in one
    # t=df[['date','summa']]
    # m=t.pivot_table(index=['date'])
    # m.plot.bar(title='xx',color='orange',width=0.3)
    # plt.show()
def SaveBook2(book):
    f = open("Invoices.xlsx","a+",encoding="utf-8")
    f.write(book[0] + ',' + book[1] + ',' + book[2] + ',' + book[3] + '\n')
    f.close()

def AddPurchaseInvoice():
    df1=pd.read_excel(r'C:\Users\37255\Desktop\algoritmi, python\kliendi_baas\Invoices.xlsx', sheet_name='sales')
    table=df1[['invoice_p','date_p','company_p','summa_p']]
    m = table.pivot_table(index=['invoice_p','date_p','company_p'])
    print("table",m.head(len(table)))#prints without indexes
    df=pd.DataFrame(m)
    print("Dataframe 3")
    print(df)
    invoice=text0_win_invoice2.get()
    date=text_win_invoice2.get()
    company=text2_win_invoice2.get()
    summa=text3_win_invoice2.get()
    df2=pd.DataFrame({"invoice_p":[text0_win_invoice2.get()],
                      "date_p":[text_win_invoice2.get()],
                      "company_p":[text2_win_invoice2.get()],
                      "summa_p":[text3_win_invoice2.get()]
                      })
    print("DataFrame 2")
    print(df2)
    if invoice in df1.values:
        print("Already exists")
        messagebox.showinfo("Error","Already exists!")
    else:
        df1.fillna(0, inplace=True)
        df=df1.append(df2,ignore_index=True,sort=False)
        df.to_excel(r'C:\Users\37255\Desktop\algoritmi, python\kliendi_baas\Invoices.xlsx', sheet_name='sales',index =[4], header=True)
        table2=df[['invoice','date','company','summa','invoice_p','date_p','company_p','summa_p']]
        m2=table2.pivot_table(index=['invoice'])
        print("Saved")
        print(m2.head(len(table2)))
        messagebox.showinfo("Info","Purchase invoice is added!")


##########sales invoices
def AddSalesInvoice():
    df1=pd.read_excel(r'C:\Users\37255\Desktop\algoritmi, python\kliendi_baas\Invoices.xlsx', sheet_name='sales')
    table=df1[['invoice','date','company','summa']]
    m = table.pivot_table(index=['invoice','date','company'])
    print("table",m.head(len(table)))#prints without indexes
    df=pd.DataFrame(m)
    print("Dataframe ")
    print(df)
    invoice=text0_win_invoice.get()
    date=text_win_invoice.get()
    company=text2_win_invoice.get()
    summa=text3_win_invoice.get()
    df2=pd.DataFrame({"invoice":[text0_win_invoice.get()], "date":[text_win_invoice.get()], "company":[text2_win_invoice.get()], "summa":[text3_win_invoice.get()]})
    print("DataFrame 2")
    print(df2)

    if invoice in df1.values:
        print("Already exists")
        messagebox.showinfo("Error","Already exists!")
    else:

        df1.fillna(0, inplace=True)
        df=df1.append(df2,ignore_index=True,sort=False)
        df.to_excel(r'C:\Users\37255\Desktop\algoritmi, python\kliendi_baas\Invoices.xlsx', sheet_name='sales',index = None, header=True)
        print(df)
        print("added")
        messagebox.showinfo("Info","Sales invoice is added!")


def erase2():
    text0_win_invoice.delete('0',END)
    text_win_invoice.delete('0',END)
    text2_win_invoice.delete('0',END)
    text3_win_invoice.delete('0',END)
#### win_invoice2
def win_invoice2(event):
    global text0_win_invoice2,text_win_invoice2,text2_win_invoice2,text3_win_invoice2,bottomframe

    root8 = Tk()
    #frames
    topframe2 = Frame(root8,height=80, bg='gray90')
    topframe2.pack(fill=X)
    bottomframe=Frame(root8,height=500, bg='gray26')
    bottomframe.pack(fill=X)
    bottomframe7=Frame(root8,height=120, bg='gray37')
    bottomframe7.pack(fill=X)
    #top freim design
    topheading2=Label(topframe2,text='Add purchase invoice', font='Gupter 15 bold',bg='gray90',fg='gray25')
    topheading2.place(x=220,y=40)
#####################################
    #inside win
    zero_label=Label(bottomframe,text="Invoice nr",width=20,font='Gupter 13',bg='gray26',fg='white')
    zero_label.grid(row=0,column=0,padx=10,pady=10)

    text0_win_invoice2=Entry(bottomframe,width=20,bd=6,font='Gupter 13',fg='grey11')
    text0_win_invoice2.grid(row=0,column=1,padx=20,pady=10)

    first_label=Label(bottomframe,text="Date",width=20,font='Gupter 13',bg='gray26',fg='white')
    first_label.grid(row=1,column=0,padx=10,pady=10)

    text_win_invoice2=Entry(bottomframe,width=20,bd=6,font='Gupter 13',fg='grey11')
    text_win_invoice2.grid(row=1,column=1,padx=20,pady=10)

    second_label=Label(bottomframe,text="Company name",width=20,font='Gupter 13',bg='gray26',fg='white')
    second_label.grid(row=2,column=0,padx=10,pady=10)

    text2_win_invoice2=Entry(bottomframe,width=20,bd=6,font='Gupter 13',fg='grey11')
    text2_win_invoice2.grid(row=2,column=1,padx=20,pady=10)

    third_label=Label(bottomframe,text="Summa",width=20,font='Gupter 13',bg='gray26',fg='white')
    third_label.grid(row=3,column=0,padx=10,pady=10)

    text3_win_invoice2=Entry(bottomframe,width=20,bd=6,font='Gupter 13',fg='grey11')
    text3_win_invoice2.grid(row=3,column=1,padx=20,pady=10)


    but = Button(bottomframe7,text="Add",bd=3,relief=RAISED,font='Gupter 10',command=AddPurchaseInvoice)
    but.place(x=220,y=30,width=70,height=30)
    but.bind("<Button-1>")  ##

    bt = Button(bottomframe7,text="Clear entry",bd=3,relief=RAISED,font='Gupter 10',command=erase2)
    bt.place(x=340,y=30,width=80,height=30)
    bt.bind("<Button-1>")  ##
###############
    root8.title("Second Window")
    root8.geometry("700x600+700+300")
    root8.resizable(width=False, height=False)
    root8.mainloop()
#########end win_invoice2########

########### win_invoice ##########
def win_invoice(event):
    global text0_win_invoice,text_win_invoice,text2_win_invoice,text3_win_invoice,bottomframe

    root7 = Tk()
    #frames
    topframe2 = Frame(root7,height=80, bg='gray90')
    topframe2.pack(fill=X)
    bottomframe=Frame(root7,height=500, bg='gray26')
    bottomframe.pack(fill=X)
    bottomframe7=Frame(root7,height=120, bg='gray37')
    bottomframe7.pack(fill=X)
    #top freim design
    topheading2=Label(topframe2,text='Add sales invoice', font='Gupter 15 bold',bg='gray90',fg='gray25')
    topheading2.place(x=220,y=40)
#####################################
    #inside win
    zero_label=Label(bottomframe,text="Invoice nr",width=20,font='Gupter 13',bg='gray26',fg='white')
    zero_label.grid(row=0,column=0,padx=10,pady=10)

    text0_win_invoice=Entry(bottomframe,width=20,bd=6,font='Gupter 13',fg='grey11')
    text0_win_invoice.grid(row=0,column=1,padx=20,pady=10)

    first_label=Label(bottomframe,text="Date",width=20,font='Gupter 13',bg='gray26',fg='white')
    first_label.grid(row=1,column=0,padx=10,pady=10)

    text_win_invoice=Entry(bottomframe,width=20,bd=6,font='Gupter 13',fg='grey11')
    text_win_invoice.grid(row=1,column=1,padx=20,pady=10)

    second_label=Label(bottomframe,text="Company name",width=20,font='Gupter 13',bg='gray26',fg='white')
    second_label.grid(row=2,column=0,padx=10,pady=10)

    text2_win_invoice=Entry(bottomframe,width=20,bd=6,font='Gupter 13',fg='grey11')
    text2_win_invoice.grid(row=2,column=1,padx=20,pady=10)

    third_label=Label(bottomframe,text="Summa",width=20,font='Gupter 13',bg='gray26',fg='white')
    third_label.grid(row=3,column=0,padx=10,pady=10)

    text3_win_invoice=Entry(bottomframe,width=20,bd=6,font='Gupter 13',fg='grey11')
    text3_win_invoice.grid(row=3,column=1,padx=20,pady=10)


    but = Button(bottomframe7,text="Add",bd=3,relief=RAISED,font='Gupter 10',command=AddSalesInvoice)
    but.place(x=220,y=30,width=70,height=30)
    but.bind("<Button-1>")  ##

    bt = Button(bottomframe7,text="Clear entry",bd=3,relief=RAISED,font='Gupter 10',command=erase2)
    bt.place(x=340,y=30,width=80,height=30)
    bt.bind("<Button-1>")  ##
###############
    root7.title("Second Window")
    root7.geometry("700x600+700+300")
    root7.resizable(width=False, height=False)
    root7.mainloop()
####### end win6 ############
################# WIN6 #######################
def win6():
    global text_win5,bottomframe3

    root6 = Tk()
    #frames
    topframe2 = Frame(root6,height=200, bg='gray26')
    topframe2.pack(fill=X)

    bottomframe3=Frame(root6,height=500, bg='gray26')
    bottomframe3.pack(fill=X)
    #top freim design
    topheading2=Label(topframe2,text='INVOICES', font='Gupter 15 bold',bg='gray26',fg='gray90')
    topheading2.place(x=350,y=20)
#####################################
    #inside window2

    but = Button(topframe2,text="SHOW SALES & PURCHASES",width=25,height=1,bd=6)
    but.place(x=100,y=80)
    but.bind("<Button-1>",sales)

    but2 = Button(topframe2,text="ADD SALES INVOICE",width=20,height=1,bd=6)
    but2.place(x=350,y=80)
    but2.bind("<Button-1>",win_invoice)

    but3 = Button(topframe2,text="ADD PURCHASE INVOICE",width=20,height=1,bd=6)
    but3.place(x=550,y=80)
    but3.bind("<Button-1>",win_invoice2)

    #first_label=Label(topframe2,text="Result",width=10,font='Gupter 13',bg='gray26',fg='gray90')
    #first_label.place(x=330,y=120)
    #out5=Label(bottomframe3,font='Gupter 13',width=70,height=14,bd=6,fg='grey11',text='',relief=SUNKEN)
    #out5.grid(row=1,column=1,padx=5,pady=30,sticky=W)

    root6.title("Second Window")
    root6.geometry("800x600+700+600")
    root6.resizable(width=False, height=False)
    root6.mainloop()
#######################END WIN 6 ###########################

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
####################### WIN 4 #################################################
def win4():
    global out3,bottomframe6

    root4 = Tk()

    #frames
    topframe4 = Frame(root4,height=70, bg='gray26')
    topframe4.pack(fill=X)

    bottomframe6=Frame(root4,height=500, bg='gray60')
    bottomframe6.pack(fill=X)
    bottomframe7=Frame(root4,height=80, bg='gray26')
    bottomframe7.pack(fill=X)
    #top freim design
    topheading3=Label(topframe4,text='VIEW ALL CUSTOMERS', font='Gupter 15 bold',bg='gray26',fg='gray90')
    topheading3.place(x=260,y=20)
#####################################
    #inside window2
    but = Button(bottomframe6,text="SHOW CUSTOMERS",width=15,height=1,bd=6)
    but.grid(row=1,column=2,padx=100,pady=80)
    but.bind("<Button-1>",ViewCustomers)

    but2 = Button(bottomframe6,text="GET THE TOTAL NUMBER OF CLIENTS",width=30,height=1,bd=6)
    but2.place(x=260,y=20)
    but2.bind("<Button-1>",GetTotal)

    first_label=Label(bottomframe6,text="Result",width=10,font='Gupter 13',bg='gray60',fg='white')
    first_label.grid(row=3,column=1,padx=8,pady=20)
    out3=Label(bottomframe6,font='Gupter 13',width=50,height=15,bd=6,fg='grey11',text='',relief=SUNKEN)
    out3.grid(row=3,column=2,padx=35,pady=2,sticky=W)

    root4.title("Second Window")
    root4.geometry("800x650+700+650")
    root4.resizable(width=False, height=False)
    root4.mainloop()
#######################END WIN 4 #################################################

####################### WIN 3 #################################################
def win3():
    global text_win3,out2

    root3 = Tk()
    #frames
    topframe3 = Frame(root3,height=50, bg='gray26')
    topframe3.pack(fill=X)
    bottomframe4=Frame(root3,height=300, bg='gray90')
    bottomframe4.pack(fill=X)
    bottomframe5=Frame(root3,height=50, bg='gray26')
    bottomframe5.pack(fill=X)
    #top freim design
    topheading3=Label(topframe3,text='DELETE CUSTOMER FROM DATABASE', font='Gupter 15 bold',bg='gray26',fg='gray90')
    topheading3.place(x=260,y=20)
#####################################
    #inside window2
    zero_label=Label(bottomframe4,text="Registration number of company",width=26,font='Gupter 13',bg='gray90',fg='black')
    zero_label.grid(row=1,column=0,padx=20,pady=30)
    text_win3=Entry(bottomframe4,width=20,bd=6,font='Gupter 13',fg='grey11')
    text_win3.grid(row=1,column=1,padx=1, pady=30)

    but = Button(bottomframe4,text="Delete",width=10,height=1,bd=6)
    but.grid(row=2,column=1,padx=10,pady=2)
    but.bind("<Button-1>",DeleteCustomer)


    first_label=Label(bottomframe5,text="Result",width=10,font='Gupter 13',bg='gray26',fg='gray90')
    first_label.grid(row=1,column=0,padx=1,pady=20)
    out2=Label(bottomframe5,font='Gupter 13',width=60,height=6,bd=6,fg='grey11',text='',relief=SUNKEN)
    out2.grid(row=1,column=1,padx=1,pady=50)

    root3.title("Second Window")
    root3.geometry("800x400+600+300")
    root3.resizable(width=False, height=False)
    root3.mainloop()

######################### END WIN 3 ########################################

################## WIN2 ###################################################################
def win2():
    global text_win2,out

    root2 = Tk()
    #frames
    topframe2 = Frame(root2,height=50, bg='gray26')
    topframe2.pack(fill=X)
    bottomframe2=Frame(root2,height=150, bg='gray90')
    bottomframe2.pack(fill=X)
    bottomframe3=Frame(root2,height=300, bg='gray26')
    bottomframe3.pack(fill=X)
    #top freim design
    topheading2=Label(topframe2,text='DISPLAY CUSTOMER DETAILS', font='Gupter 15 bold',bg='gray26',fg='gray90')
    topheading2.place(x=260,y=20)
#####################################
    #inside window2
    zero_label=Label(bottomframe2,text="Registration number of company",width=26,font='Gupter 13',bg='gray90',fg='black')
    zero_label.grid(row=1,column=0,padx=20,pady=30)
    text_win2=Entry(bottomframe2,width=20,bd=6,font='Gupter 13',fg='grey11')
    text_win2.grid(row=1,column=1,padx=1, pady=30)

    but = Button(bottomframe2,text="Show",width=10,height=1,bd=6)
    but.grid(row=2,column=1,padx=10,pady=2)
    but.bind("<Button-1>",DisplayCompany)

    but31 = Button(bottomframe2,text="Speak",command=but_speak)
    but31.place(x=500,y=34)

    but32 = Button(bottomframe3,text="Speak",command=but_speak2)
    but32.place(x=600,y=55)

    first_label=Label(bottomframe3,text="Result",width=10,font='Gupter 13',bg='gray26',fg='gray90')
    first_label.grid(row=1,column=0,padx=1,pady=20)
    out=Label(bottomframe3,font='Gupter 13',width=50,height=14,bd=6,fg='grey11',text='',relief=SUNKEN)
    out.grid(row=1,column=1,padx=1,pady=30,sticky=W)

    root2.title("Second Window")
    root2.geometry("800x500+600+400")
    root2.resizable(width=False, height=False)
    root2.mainloop()

################## END WIN2 ###################################################################

################## WIN1 ###################################################################
def win1():
    global text0_win1,text_win1,text2_win1,text3_win1,text4_win1,bottomframe

    root1 = Tk()
    #frames
    topframe2 = Frame(root1,height=80, bg='gray90')
    topframe2.pack(fill=X)
    bottomframe=Frame(root1,height=500, bg='gray26')
    bottomframe.pack(fill=X)
    bottomframe3=Frame(root1,height=120, bg='gray37')
    bottomframe3.pack(fill=X)
    #top freim design
    topheading2=Label(topframe2,text='Add customers', font='Gupter 15 bold',bg='gray90',fg='gray25')
    topheading2.place(x=220,y=40)
#####################################
    #inside win
    zero_label=Label(bottomframe,text="Register number",width=20,font='Gupter 13',bg='gray26',fg='white')
    zero_label.grid(row=0,column=0,padx=10,pady=10)

    text0_win1=Entry(bottomframe,width=20,bd=6,font='Gupter 13',fg='grey11')
    text0_win1.grid(row=0,column=1,padx=20,pady=10)

    first_label=Label(bottomframe,text="Company name",width=20,font='Gupter 13',bg='gray26',fg='white')
    first_label.grid(row=1,column=0,padx=10,pady=10)

    text_win1=Entry(bottomframe,width=20,bd=6,font='Gupter 13',fg='grey11')
    text_win1.grid(row=1,column=1,padx=20,pady=10)

    second_label=Label(bottomframe,text="Company address",width=20,font='Gupter 13',bg='gray26',fg='white')
    second_label.grid(row=2,column=0,padx=10,pady=10)

    text2_win1=Entry(bottomframe,width=20,bd=6,font='Gupter 13',fg='grey11')
    text2_win1.grid(row=2,column=1,padx=20,pady=10)

    third_label=Label(bottomframe,text="Mobile phone",width=20,font='Gupter 13',bg='gray26',fg='white')
    third_label.grid(row=3,column=0,padx=10,pady=10)

    text3_win1=Entry(bottomframe,width=20,bd=6,font='Gupter 13',fg='grey11')
    text3_win1.grid(row=3,column=1,padx=20,pady=10)

    fouth_label=Label(bottomframe,text="Email address",width=20,font='Gupter 13',bg='gray26',fg='white')
    fouth_label.grid(row=4,column=0,padx=10,pady=10)

    text4_win1=Entry(bottomframe,width=20,bd=6,font='Gupter 13',fg='grey11')
    text4_win1.grid(row=4,column=1,padx=20,pady=10)

    but = Button(bottomframe3,text="Add",bd=3,relief=RAISED,font='Gupter 10',command=AddCustomer)
    but.place(x=220,y=30,width=70,height=30)
    but.bind("<Button-1>")  ##

    bt = Button(bottomframe3,text="Clear entry",bd=3,relief=RAISED,font='Gupter 10',command=erase)
    bt.place(x=340,y=30,width=80,height=30)
    bt.bind("<Button-1>")  ##
###############
    root1.title("Second Window")
    root1.geometry("700x600+700+300")
    root1.resizable(width=False, height=False)
    root1.mainloop()
#########end win1 ####################

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
#button1 view
viewButton=Button(bottomframe, text='ADD CUSTOMERS',font='Gupter 10 bold',\
width=25,padx=10,pady=5,borderwidth=7,activebackground="gray33",activeforeground="snow",relief=RAISED,command=win1)
viewButton.place(x=200,y=80)
#button2 display customer
addButton=Button(bottomframe, text='DISPLAY CUSTOMER DETAILS',font='Gupter 10 bold',width=25,padx=10,pady=5,borderwidth=7,activebackground="gray33",activeforeground="snow",relief=RAISED,command=win2)
addButton.place(x=200,y=140)
#button3 delete
aboutButton=Button(bottomframe, text='DELETE A CUSTOMER',font='Gupter 10 bold',width=25,padx=10,pady=5,borderwidth=7,activebackground="gray33",activeforeground="snow",relief=RAISED,command=win3)
aboutButton.place(x=200,y=200)
#button4 view customers
aboutButton=Button(bottomframe, text='VIEW ALL CUSTOMERS',font='Gupter 10 bold',width=25,padx=10,pady=5,borderwidth=7,activebackground="gray33",activeforeground="snow",relief=RAISED,command=win4)
aboutButton.place(x=200,y=260)

aboutButton=Button(bottomframe, text='SEARCH',font='Gupter 10 bold',width=25,padx=10,pady=5,borderwidth=7,activebackground="gray33",activeforeground="snow",relief=RAISED,command=win5)
aboutButton.place(x=200,y=320)

aboutButton=Button(bottomframe, text='INVOICES',font='Gupter 10 bold',width=25,padx=10,pady=5,borderwidth=7,activebackground="gray33",activeforeground="snow",relief=RAISED,command=win6)
aboutButton.place(x=200,y=380)

root.title("First Window")
root.geometry('650x600+300+200')
root.resizable(width=False, height=False)
root.mainloop()
