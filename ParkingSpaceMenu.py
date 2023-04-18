#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 21:09:40 2023

@author: vboxuser
"""

import CustomerManagement as cm
import ParkingSpaceManagement as psm
import ParkingManagement as pm

def menu():
    print(" ---------------- Welcome to Parking Space Management System ----------------")
    print("Type 1 for Adding a Customer")
    print("Type 2 for Deleting a Customer")
    print("Type 3 for Updating a Customer")
    print("Type 4 for Viewing a Specific Customer")
    print("Type 5 for Viewing All Customers")
    
    print("Type 6 for Adding a Parking Slot")
    print("Type 7 for Deleting a Parking Slot")
    print("Type 8 for Updating a Parking Slot")
    print("Type 9 for Viewing a Specific Parking Slot")
    print("Type 10 for Viewing All Parking")
    
    print("Type 11 for Adding a Parking")
    print("Type 12 for Deleting a Parking")
    print("Type 13 for Updating a Parking")
    print("Type 14 for Viewing a Specific Parking")
    print("Type 15 for Viewing All Parking")
    
    print("Type 16 to Exit Program")

while True:
    choice = int(input("Enter Your Choice (Type 0 for options): "))
    match choice:
        case 0:
            menu()
        # CustomerManagement
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
        # Parking Slot Management
        case 6:
            psm.AddParkingSlot()
        case 7:
            psm.DeleteParkingSlot()
        case 8:
            psm.UpdateParkingSlot()
        case 9:
            psm.ViewSpecificParkingSlot()
        case 10:
            psm.ViewAllParkingSlot()
        # Parking Management
        case 11:
            pm.AddParking()
        case 12:
            pm.DeleteParking()
        case 13:
            pm.UpdateParking()
        case 14:
            pm.ViewSpecificParking()
        case 15:
            pm.ViewAllParking()

        case 16:
            quit()
        case _:
            print("Wrong Input! Please Enter a Valid Choice : ")
