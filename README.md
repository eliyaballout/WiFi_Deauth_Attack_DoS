# ***Welcome to WiFi DoS***



## Introduction

Welcome to WiFi DoS program, this program is written in python. <br>
This python code demonstrate a deauthentication attack on client devices that are connected to a wireless network. So instead of doing it manually and type each command separately and to make it more interesting and a lot simpler, I've made a script that automates this process and speed things up. <br><br>


**Important Note: Before you proceed, it's crucial to understand and acknowledge the following:**

1. ***Purpose of the Script:*** This script is developed strictly for educational purposes. It aims to demonstrate the vulnerabilities present in wireless networks and how they can be exploited. By understanding these vulnerabilities, users can take proactive measures to enhance the security of their networks.
   
2. ***Legal Implications:*** Unauthorized access or disruption of computer networks, including wireless networks, is illegal in many jurisdictions. ***This script should only be used on networks that you own or have explicit permission to test***. Do not use this script against networks that you do not own or do not have authorization to test. Any misuse of this script is entirely the responsibility of the user.

3. ***Ethical Considerations:*** It is essential to use this script responsibly and ethically. Always respect the privacy and rights of others. Avoid causing harm or disruption to network users. The primary goal is to learn and understand network security, not to cause harm or engage in malicious activities.

4. ***Disclaimer:*** I do not endorse or encourage any illegal or malicious activities. The script is provided as-is, without any warranties or guarantees. Users are solely responsible for their actions and should use this script responsibly. <br><br>


**By accessing and using this script, you acknowledge and agree to the terms and guidelines mentioned above. Always prioritize ethical considerations, safety, and legal compliance.**
<br><br>




## Requirements

**Before installing and start using the program, you will have to know some of the requirements that it needs:**

1. **Kali Linux:** The most used OS for hacking and penetration testing is Kali linux. So you need to have kali linux, or any linux distro you want as long as `aircrack-ng` tool is installed on it, installed in your computer using VirtualBox or VMware. <br>
The advantage of Kali that there are many many tools comes pre-installed. but as I said the main thing is to be `aircrack-ng` installed.


2. **WiFi Adapter:** For all the attacks that proceed on WiFi networks, we have to work with external WiFi adapter that supports monitor and injection mode, because the build in WiFi cards in the computer doesn't have this ability. And we need this monitor and injection mode in order to do any kind of attacks on a WiFi network. <br><br>
So i will help you to pick up your adapter. There are many kinds of frequencies or bands that the router use, the most known are: **2.4 GHz** and **5 GHz**.
   1. **Alfa-AWUS036NHA:** This is one of the best adapters at all, it supports both monitor and injection mode, and Kali Linux automatically picks it up, it comes pre-configued. The only disadvantage of this one is it only supports 2.4 GHz wifi frequency.
   
   2. **Alfa-AWUS036ACH:** This is also one of the best adapters, it supports both monitor and injection mode. The benefit of this adapter that is supports both 2.4 GHz and 5 GHz, and Kali Linux automatically picks it up, it also comes pre-configued.

<br><br>




## Installation

**In order for the program to work properly make sure that your target is connected to a WiFi network and not to Ethernet cable.** <br>
**This program will only work on linux, not Windows.** <br>
To download the program for all Linux distributions, you have to clone the repo from GitHub:
```
git clone https://github.com/eliyaballout/WiFi_DoS
cd WiFi_DoS
```

run the app:
```
python3 Wifi_Dos.py
```
<br>

<u>***Important Note:***</u> Make sure you have **git** and **python3** installed on your Linux OS.
<br><br>




## Features

The currently supported functionalities are:

* Displaying all the WiFi networks that the adapter captures.
* Displaying the devices by its MAC addresses that is connected to a specific network of your choice.
* Attacking the network by a deauthentication attack.
* Ability to do the attack on specific devices by selecting them, and also for all the devices.
* Selecting what frequency/bands that the adapter will capture.
* Selecting which adapter do you want to use (if you have more than one connected).
<br><br>




## Technologies Used
<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" title="python" alt="python" width="40" height="40"/>&nbsp;
<br><br><br>




## Some screenshots from our app
