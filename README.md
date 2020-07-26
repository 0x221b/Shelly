# Shelly
Script lets you input your IP and programming language and prints out one liner reverse shells to use. all option available if you aren't sure. Then gives option of reverse shell using nc. 

usage:
python3 shelly.py -ip 127.0.0.1 -lang php

Options

-i --ip: IP address for the rev shell to connect back to

-l --lang: language of shell wanted

Currently available languages:
bash, python, perl, ruby, telnet, nc, wget, php

If lang is set to all it will print all available options

The port for the reverse shell to connect to is set to 53 as this is commonly allowed past rules etc. If you wish to change it you will need to edit revshells.txt and shelly.py in the listener section.

Disclaimer - You should only ever attempt to get a reverse shell on your own system or one you have express permission to do so.


To do:
add details of how to upgrade a poor reverse shell so tab etc work
add metasploit rev shell and custom shellcode reverse shell payload 
