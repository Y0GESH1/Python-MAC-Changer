import argparse
import subprocess
import re

def input_validator(user_specified_mac,user_specified_interface):
    if user_specified_mac and user_specified_interface:
        mac_change(user_specified_mac,user_specified_interface)
    elif not user_specified_mac:
        print("The user did not specify mac address")
    elif not user_specified_interface:
        print("The user did not specify interface")

    
def check_current_mac(interface):
    csm = str(subprocess.check_output(['ifconfig',interface]))
    current_system_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",csm)
    return current_system_mac.group(0)


def check_new_mac(interface):
    csm = str(subprocess.check_output(['ifconfig',interface]))
    new_system_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",csm)
    return new_system_mac.group(0)

def mac_change(newmac,interface):
    mac_addr_spoof = newmac
    network_interface = interface
    
    old_mac = check_current_mac(user_specified_interface)

    # System commands 
    subprocess.call(['ifconfig',network_interface,"down"])
    subprocess.call(['ifconfig',network_interface,"hw","ether",mac_addr_spoof])
    subprocess.call(['ifconfig',network_interface,"up"])

    new_mac = check_new_mac(user_specified_interface)

    print(f'The mac address has been changed from {old_mac} to {new_mac}')

def UI():
    # Display
    banner = "****** Python Mac Changer ******"
    print(banner)

    # user options
    parser = argparse.ArgumentParser(description="Python MAC Changer")
    parser.add_argument('-n',metavar=' New Mac address ',help="Specify the new mac or the mac address you want to spoof")
    parser.add_argument('-i',metavar=' Specify Interface ',help="Specify the interface to be changed")
    args = parser.parse_args()
    
    # getting user input
    global user_specified_mac
    global user_specified_interface
    user_specified_mac =  args.n
    user_specified_interface = args.i

    #Checking for valid inputs  
    input_validator(user_specified_mac,user_specified_interface)

# program start
UI()
