#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 17:29:57 2023

@author: vboxuser
"""

import mysql.connector as sqltor
import random

def ConnectServer():
    mycon=sqltor.connect(host="localhost",user="root",passwd="changeme",database="sample")
    if not mycon.is_connected():
        print('Error connecting to MySQL database')
    # else:
    #     print("Connected to MySQL server successfully, You can begin operation now ")
    return mycon

def AddCustomer():
    mycon = ConnectServer()
    cursor=mycon.cursor(buffered=True)
    print("----------Enter New Member Details----------")
    name = input("Enter Name: ")
    phNum = input("Enter Phone Number: ")
    custID = random.randint(100, 100000)
    comm = "INSERT INTO customer VALUES('{}','{}','{}');".format(name, phNum, custID)
    cursor.execute(comm)
    
    print("Customer ID = ", custID)
    mycon.commit()
    mycon.close()

def DeleteCustomer():
    mycon = ConnectServer()
    cursor = mycon.cursor(buffered=True)
    cid = input("Enter Customer ID of the Customer that will be Deleted : ")
    comm = "DELETE FROM customer WHERE Customer_ID = '{}';".format(cid)
    cursor.execute(comm)
    mycon.commit()
    mycon.close()
def ViewAllCustomer():
    mycon = ConnectServer()
    cursor = mycon.cursor(buffered=True)
    # cid = input("Enter Customer ID")
    comm = "SELECT * FROM  customer;"
    cursor.execute(comm)
    mycon.commit()
    for row in cursor:
        print(row)
    mycon.close()
    
def ViewACustomer():
    mycon = ConnectServer()
    cursor = mycon.cursor(buffered=True)
    cid = input("Enter Customer ID : ")
    comm = "SELECT * FROM  customer WHERE Customer_ID = '{}';".format(cid)
    cursor.execute(comm)
    mycon.commit()
    for row in cursor:
        print(row)
    mycon.close()

def UpdateCustomer():
    mycon = ConnectServer()
    cursor = mycon.cursor(buffered=True)
    cid = input("Enter Customer ID : ")
    c1 = input("Do You want to change Name? (y/n) ")
    
    if(c1 == 'y' or c1 == 'Y'):
        name = input("Enter New Name: ")
        comm = "UPDATE customer SET Name = '{}' WHERE Customer_ID = '{}';".format(name, cid)
        cursor.execute(comm)
        mycon.commit()
    c1 = input("Do You want to change Phone Number? (y/n) ")
    
    if(c1 == 'y' or c1 == 'Y'):
        num = input("Enter New Phone No: ")
        comm = "UPDATE customer SET Phone_No = '{}' WHERE Customer_ID = '{}';".format(num, cid)
        cursor.execute(comm)
        mycon.commit()
    mycon.close()
    
