#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 21:09:40 2023

@author: vboxuser
"""

import CustomerManagement as cm

while True:
    print(" ---------------- Welcome to Parking Space Management System ----------------")
    print("Type 1 for Adding a Customer")
    print("Type 2 for Deleting a Customer")
    print("Type 3 for Updating a Customer")
    print("Type 4 for View a Specific Customer")
    print("Type 5 for View All Customers")
    print("Type 6 to Exit Program")
    choice = int(input("Enter Your Choice : "))
    match choice:
        case 1:
            cm.AddCustomer()
        case 2:
            cm.DeleteCustomer()
        case 3:
            cm.UpdateCustomer()
        case 4:
            cm.ViewACustomer()
        case 5:
            cm.ViewAllCustomer()
        case 6:
            quit()
        case _:
            print("Wrong Input! Please Enter a Valid Choice : ")
