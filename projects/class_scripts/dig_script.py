#!/usr/bin/python3

import os

domain = input("Which Domain do you want to Dig?: ")

Digtype = input("\nWhat type of Dig command to you want to run?\n" "SOA (enter 1)\n"
"MX (enter 2)\n" "hostname (enter 3)\n" "TTL (enter 4)\n")

if Digtype == "1":
    dg = "soa" 
elif Digtype == "2":
    dg = "mx" 
elif Digtype == "3":
    dg= "hostname" 
elif Digtype == "4":
    dg = "ttl"
else:
    print("Error")
os.system("dig "+ domain + " " + dg)