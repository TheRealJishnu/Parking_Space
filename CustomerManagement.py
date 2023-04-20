#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 17:29:57 2023

@author: vboxuser
"""

import mysql.connector as sqltor
import random

def InputID():
    while True:
        idn = input("Enter Customer ID : ")
        if CheckID(idn):
            return idn
        else:
            print("Customer ID can only contain numeric digits")
def CheckID(idn):
    for e in idn:
        if not ('0' <= e <= '9'):
            return 0
    return 1

def InputName():
    while True:
        name = input("Enter Name: ")
        if CheckName(name):
            return name
        else:
            print("Name Should only Contain Alphabets and Space, Enter again")
def CheckName(name):
    for e in name:
        if not (('a' <= e <= 'z') or ('A' <= e <= 'Z') or e == ' '):
            return 0
    return 1

def InputPhone():
    while True:
        phNum = input("Enter Phone Number: ")
        if CheckPhone(phNum):
            return phNum
        else:
            print("Phone Number should be of 10 digits and should only consists of numeric digits, Enter again")
def CheckPhone(num):
    if str.len() != 10:
        return 0
    for e in num:
        if not ('0' <= e <= '9'):
            return 0
    return 1

def ConnectServer():
    mycon=sqltor.connect(host="localhost",user="root",passwd="changeme",database="sample")
    if not mycon.is_connected():
        print('Error connecting to MySQL database')
    # else:
    #     print("Connected to MySQL server successfully, You can begin operation now ")
    return mycon

# Before Unit Testing
# def AddCustomer():
#     mycon = ConnectServer()
#     cursor=mycon.cursor(buffered=True)
#     print("----------Enter New Member Details----------")
#     name = input("Enter Name: ")
#     phNum = input("Enter Phone Number: ")
#     custID = random.randint(100, 100000)
#     comm = "INSERT INTO customer VALUES('{}','{}','{}');".format(name, phNum, custID)
#     cursor.execute(comm)
    
#     print("Customer ID = ", custID)
#     mycon.commit()
#     mycon.close()

# After Unit Testing and error correction
def AddCustomer():
    mycon = ConnectServer()
    cursor=mycon.cursor(buffered=True)
    print("----------Enter New Member Details----------")
    
    name = InputName()
    phNum = InputPhone()
    
    custID = random.randint(100, 100000)
    comm = "INSERT INTO customer VALUES('{}','{}','{}');".format(name, phNum, custID)
    cursor.execute(comm)
    
    print("Customer ID = ", custID)
    mycon.commit()
    mycon.close()
    
    
def DeleteCustomer():
    mycon = ConnectServer()
    cursor = mycon.cursor(buffered=True)
    cid = InputID()
    comm = "DELETE FROM customer WHERE Customer_ID = '{}';".format(cid)
    cursor.execute(comm)
    mycon.commit()
    mycon.close()
    
def ViewAllCustomer():
    mycon = ConnectServer()
    cursor = mycon.cursor(buffered=True)
    comm = "SELECT * FROM  customer;"
    cursor.execute(comm)
    mycon.commit()
    for row in cursor:
        print(row)
    mycon.close()
    
def ViewACustomer():
    mycon = ConnectServer()
    cursor = mycon.cursor(buffered=True)
    cid = InputID()
    comm = "SELECT * FROM  customer WHERE Customer_ID = '{}';".format(cid)
    cursor.execute(comm)
    mycon.commit()
    for row in cursor:
        print(row)
    mycon.close()

def UpdateCustomer():
    mycon = ConnectServer()
    cursor = mycon.cursor(buffered=True)
    cid = InputID()
    c1 = input("Do You want to change Name? (y/n) ")
    
    if(c1 == 'y' or c1 == 'Y'):
        name = InputName()
        comm = "UPDATE customer SET Name = '{}' WHERE Customer_ID = '{}';".format(name, cid)
        cursor.execute(comm)
        mycon.commit()
    c1 = input("Do You want to change Phone Number? (y/n) ")
    
    if(c1 == 'y' or c1 == 'Y'):
        num = InputPhone()
        comm = "UPDATE customer SET Phone_No = '{}' WHERE Customer_ID = '{}';".format(num, cid)
        cursor.execute(comm)
        mycon.commit()
    mycon.close()
    
