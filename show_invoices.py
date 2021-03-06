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

### datetime ###
# date=datetime.datetime.now()#.date()
# date=str(date.strftime("%d/%m/%Y %H:%M:%S"))

from openpyxl import load_workbook

matplotlib.style.use('ggplot') #for beautiful graphics




########### WIN 6 ###############
def sales(event):
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
    df2=pd.DataFrame({"invoice":[text0_win_invoice.get()],
                      "date":[text_win_invoice.get()],
                      "company":[text2_win_invoice.get()],
                      "summa":[text3_win_invoice.get()]
                      })
    print("DataFrame 2")
    print(df2)
    df1.fillna(0, inplace=True)
    df=df1.append(df2,ignore_index=True,sort=False)
    df.to_excel(r'C:\Users\37255\Desktop\algoritmi, python\kliendi_baas\Invoices.xlsx', sheet_name='sales',index = None, header=True)
    print("Saved")
    print(df)
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

########## END WIN 6 #############
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
    topheading2=Label(topframe2,text='SEE TABLE OF INVOICES', font='Gupter 15 bold',bg='gray26',fg='gray90')
    topheading2.place(x=200,y=20)
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

# date_label=Label(topframe, text="CURRENT DATE & TIME: "+date, font='Gupter 10 bold',bg='gray90',fg='gray25')
# date_label.place(x=350,y=10)

center_image=PhotoImage(file='puzzle.png')
center_image_label=Label(bottomframe, image=center_image, bg='gray90')
center_image_label.place(x=-30,y=-60)

aboutButton=Button(bottomframe, text='INVOICES',font='Gupter 10 bold',width=25,padx=10,pady=5,borderwidth=7,activebackground="gray33",activeforeground="snow",relief=RAISED,command=win6)
aboutButton.place(x=200,y=260)


root.title("First Window")
root.geometry('650x550+300+200')
root.resizable(width=False, height=False)
root.mainloop()
