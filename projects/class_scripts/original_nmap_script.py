#!/usr/bin/python3

import os

scan_type = input('Choose NMAP scan type:\n\tTCP SYN[1]\n\tTCP Connect[2]\n\tUDP Scan[3]\n\tVersion Detection[4]\n\tOS Detection[5]\n\tAggressive Scan[6]\n\tPing Scan[7]\n\tTCP NULL[8]\n\tTCP FIN[9]\n\tTCP Xmas[10]\n')

timing_option = input('Choose timing option:\n\tParanoid[1]\n\tSneaky[2]\n\tPolite[3]\n\tNormal[4]\n\tAggressive[5]\n\tInsane[6]\n')

target = input('Enter target ip/range ex: 192.168.20.1-20 : ')

match int(scan_type):
    case 1:
        st = '-sS'
    case 2:
        st = '-sT'
    case 3:
        st = '-sU'
    case 4:
        st = '-sV'
    case 5:
        st = '-O'
    case 6:
        st = '-A'
    case 7:
        st = '-sn'
    case 8:
        st = '-sN'
    case 9:
        st = '-sF'
    case 10:
        st = '-sX'
    case _:
        print('Invalid scan option')
match int(timing_option):
    case 1:
        to = '-T0'
    case 2:
        to = '-T1'
    case 3:
        to = '-T2'
    case 4:
        to = '-T3'
    case 5:
        to = '-T4'
    case 6:
        to = '-T5'
    case _:
        print('Invalid timing option')

os.system(f"nmap {target} {st} {to}")