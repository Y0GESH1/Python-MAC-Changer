#!/bin/python3

import subprocess
import argparse
# import pyfiglet as pfg

# UI code
def UI():
    # banner = pfg.figlet_format("Mac Changer",font="slant")
    # print(banner)

    parser = argparse.ArgumentParser(description="Python MAC Changer")
    parser.add_argument('-nm',metavar='New Macaddress',help="Specify the new mac or the spoofed mac")
    parser.add_argument('-int',metavar='Specify Interface ',help="Specify the interface to be changed")
    args = parser.parse_args()
    global nm
    nm = args.nm
    global intr 
    intr = args.int
    if not nm:
        print("no mac was specified")
    elif not intr:
        print("no interface was specified")
    
    mac_change(nm,intr)

def mac_change(newmac,interface):
    mac_to_spoof = newmac
    network_interface = interface

    subprocess.call(['ifconfig',network_interface,"down"])
    subprocess.call(['ifconfig',network_interface,"hw","ether",mac_to_spoof])
    subprocess.call(['ifconfig',network_interface,"up"])
# function call
UI()
