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
    if mycon.is_connected()==False:
        print('Error connecting to MySQL database')
    # else:
    #     print("Connected to MySQL server successfully, You can begin operation now ")
    return mycon

def AddCustomer():
    mycon = ConnectServer()
    cursor=mycon.cursor(buffered=True)
    print("----------Enter New Member Details----------")
    name = input("Enterr Name: ")
    phNum = input("Enter Phone Number: ")
    custID = random.randint(100, 100000)
    comm = "INSERT INTO customer VALUES('{}','{}','{}');".format(name, phNum, custID)
    cursor.execute(comm)
    
    print("Customer ID = ", custID)
    mycon.commit()
    print(cursor)
    mycon.close()

def DeleteCustomer():
    mycon = ConnectServer()
    cursor = mycon.cursor(buffered=True)
    cid = input("Enter Customer ID of the Customer that will be Deleted : ")
    comm = "DELETE FROM customer WHERE Customer_ID = '{}';".format(cid)
    cursor.execute(comm)
    # print(cursor)
    mycon.commit()
    print(cursor)
    mycon.close()
def ViewAllCustomer():
    mycon = ConnectServer()
    cursor = mycon.cursor(buffered=True)
    # cid = input("Enter Customer ID")
    comm = "SELECT * FROM  customer;"
    cursor.execute(comm)
    # print(cursor)
    mycon.commit()
    for row in cursor:
        print(row)
    mycon.close()
AddCustomer()
ViewAllCustomer()
DeleteCustomer()
    
    
    
    
    
    
    
    
    
    
