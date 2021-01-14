from tkinter import *
import re
import tkinter as tk
from tkinter.ttk import Combobox
from functools import partial
import numpy as np 


master = Tk()
master.title( "GST to PAN" )
master.geometry('1100x600')

pantype = {"C" : "COMPANY",
"P" : "INDIVIDUAL",
"H" : "HUF",
"F"	: "PARTNERSHIP FIRM",
"A"	: "AOP",
"T"	: "TRUST",
"B"	: "BOI",
"L"	: "LOCAL-AUTHORITY",
"J"	: "Artificial-Juridical-Person",
"G"	: "Government"
}

statecodes=("01 - Jammu & Kashmir",
"02 - Himachal Pradesh",
"03 - Punjab",
"04 - Chandigarh",
"05 - Uttarakhand",
"06 - Haryana",
"07 - Delhi",
"08 - Rajasthan",
"09 - Uttar Pradesh",
"10 - Bihar",
"11 - Sikkim",
"12 - Arunachal Pradesh",
"13 - Nagaland",
"14 - Manipur",
"15 - Mizoram",
"16 - Tripura",
"17 - Meghalaya",
"18 - Assam",
"19 - West Bengal",
"20 - Jharkhand",
"21 - Orissa",
"22 - Chhattisgarh",
"23 - Madhya Pradesh",
"24 - Gujarat",
"25 - Daman & Diu",
"26 - Dadra & Nagar Haveli",
"27 - Maharashtra",
"28 - Andhra Pradesh (Old)",
"29 - Karnataka",
"30 - Goa",
"31 - Lakshadweep",
"32 - Kerala",
"33 - Tamil Nadu",
"34 - Puducherry",
"35 - Andaman & Nicobar Islands",
"36 - Telengana",
"37 - Andhra Pradesh (New)",
"38 - Ladakh")

chararray = {"0" : 0,
"1" : 1,
"2" : 2,
"3" : 3,
"4" : 4,
"5" : 5,
"6" : 6,
"7" : 7,
"8" : 8,
"9" : 9,
"A" : 10,
"B" : 11,
"C" : 12,
"D" : 13,
"E" : 14,
"F" : 15,
"G" : 16,
"H" : 17,
"I" : 18,
"J" : 19,
"K" : 20,
"L" : 21,
"M" : 22,
"N" : 23,
"O" : 24,
"P" : 25,
"Q" : 26,
"R" : 27,
"S" : 28,
"T" : 29,
"U" : 30,
"V" : 31,
"W" : 32,
"X" : 33,
"Y" : 34,
"Z" : 35
}

sequ = {"FIRST":1,"SECOND":2,"THIRD":3}

pannumber = tk.StringVar() 

stcode = tk.StringVar()

rank = tk.StringVar()

H1 = Label(master, text='CHECK YOUR GST NUMBER WITH PAN Number - Without GOVT PORTAL (Even Before Applying it to Govt.)', font=("Helvetica",16))
H1.grid(row=0, column=1, columnspan=10, pady=20)

Q1 = Label(master, text='Please enter your PAN', font=("Helvetica",16))
Q1.grid(row=1, column=0, columnspan=2, pady=20)

A1 = Entry(master, font=("Helvetica",16), textvariable=pannumber)
A1.grid(row=1, column=2, columnspan=5, pady=20)




def valpan(pannum, fe, ie):
    panformat = re.compile("[A-Za-z]{3}[ABCFGHLJPTabcfghljpt]{1}[A-Za-z]{1}[0-9]{4}[A-Za-z]{1}")

    print(pannum.get())

    if (panformat.match(str(pannum.get()))):
        fe.configure(text='OK')
        ie.configure(text=pantype[str(pannum.get()[3]).upper()])
        print('OK')
    else:
        fe.configure(text='PAN is not correct')
        ie.configure(text='PAN is not correct')
        print('PAN is not correct')
    




Q2 = Label(master, text='PAN Status', font=("Helvetica",16))
Q2.grid(row=2, column=0, columnspan=2, pady=20)

A2 = Label(master, font=("Helvetica",16), text="")
A2.grid(row=2, column=2, columnspan=5, pady=20)

Q3 = Label(master, text='Your Income Tax status', font=("Helvetica",16))
Q3.grid(row=3, column=0, columnspan=2, pady=20)

A3 = Label(master, font=("Helvetica",16), text="")
A3.grid(row=3, column=2, columnspan=5, pady=20)

valpan = partial(valpan, pannumber, A2, A3)

B1 = Button(master, text='Validate PAN', command=valpan, font=("Helvetica",12))
B1.grid(row=1, column=6, columnspan=2, pady=20)


Q4 = Label(master, text='Please Enter your State code', font=("Helvetica",16))
Q4.grid(row=4, column=0, columnspan=2, pady=20)


A4 = Combobox(master, values=statecodes, font=("Helvetica",16), textvariable=stcode)
A4.grid(row=4, column=2, columnspan=5, pady=20)

Q5 = Label(master, text='Is this first number in your state', font=("Helvetica",16))
Q5.grid(row=5, column=0, columnspan=2, pady=20)


A5 = Combobox(master, values=('FIRST','SECOND','THIRD'), font=("Helvetica",16), textvariable=rank)
A5.grid(row=5, column=2, columnspan=5, pady=20)


def calculatechecksum(num1):
    arrayn = []

    for i in range(0,len(num1)):
        arrayn.append(chararray[num1[i]])

    print(arrayn)

    array14 = np.array(arrayn) * np.array([1,2,1,2,1,2,1,2,1,2,1,2,1,2])

    print(array14)

    checksum = (36-(sum(array14//36 + array14%36))%36)%36

    print(checksum)

    for  key,value in chararray.items():
        if value == checksum:
            lastdig = key
            break
        
    return lastdig


def getgst():
    if (stcode.get() !='' and rank.get() !='' and pannumber.get() != ''):
        print(stcode.get()[0:2])
        print(pannumber.get().upper())
        print(str(sequ[rank.get()]))
        startw = str(stcode.get()[0:2]) + pannumber.get().upper() + str(sequ[rank.get()]) + 'Z'
        print(startw)
        lastdigit = str(calculatechecksum(startw))
        gst = startw + lastdigit
        print(gst)
    
    

        re = Text(master, height=1, font=("Helvetica",16))
        re.insert(1.0, 'Your GST registration number is '+ gst)
        re.grid(row=7, column=1, columnspan=10, pady=20)
        re.configure(state=DISABLED)


B2 = Button(master, text='Get GST Number', command=getgst, font=("Helvetica",12))
B2.grid(row=6,column=5, columnspan=1, pady=20)

 






'''
Q2 = Label(master, text='Please enter your PAN', font=("Helvetica",16))
Q2.grid(row=1, column=0, columnspan=2, pady=20)

A2 = Entry(master, font=("Helvetica",16))
A2.grid(row=1, column=2, columnspan=5, pady=20)

Q1 = Label(master, text='Please enter your PAN', font=("Helvetica",16))
Q1.grid(row=1, column=0, columnspan=2, pady=20)

A1 = Entry(master, font=("Helvetica",16))
A1.grid(row=1, column=2, columnspan=5, pady=20)

Q1 = Label(master, text='Please enter your PAN', font=("Helvetica",16))
Q1.grid(row=1, column=0, columnspan=2, pady=20)

A1 = Entry(master, font=("Helvetica",16))
A1.grid(row=1, column=2, columnspan=5, pady=20)
'''



mainloop()