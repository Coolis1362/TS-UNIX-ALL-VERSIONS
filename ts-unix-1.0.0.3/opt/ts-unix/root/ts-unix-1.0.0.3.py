#!/usr/bin/env python3
import os
import sys
import time

def ts_unix_prompt():
    user = os.environ.get("USER", "ts-unix")  # Safer way to get username
    cwd = os.getcwd()  # Get current directory
    return f"{user}@TS-UNIX:{cwd}$ "  # Custom TS-UNIX prompt


time.sleep(1)
print("TTTTTT  SSS      U   U N   N III X   X      11      000      000     333  ")
time.sleep(1)
print("  TT   S         U   U NN  N  I   X X      111     0  00    0  00       3 ")
time.sleep(1)
print("  TT    SSS  --- U   U N N N  I    X        11     0 0 0    0 0 0     33  ")
time.sleep(1)
print("  TT       S     U   U N  NN  I   X X       11  .. 00  0 .. 00  0 ..    3 ")
time.sleep(1)
print("  TT   SSSS       UUU  N   N III X   X     11l1 ..  000  ..  000  .. 333  ")
time.sleep(1)
print("Non-ASCII art If Can't Read ASCII Art: TS-UNIX 1.0.0.3")
time.sleep(1)
print("Coolis1362 And Tadeosoft Copyright (C) 2025 All Rights Reserved")
while True:
    command = input(ts_unix_prompt())  # Show prompt and get input
    if command.lower() in ["exit", "quit"]:
        break
    elif command.lower() == "ts-unix-version":
        print("TS-UNIX version 1.0.0.3")
    elif command.lower() == "help":
        print("THE SAME AS UNIX AND LINUX AND MACOS THIS IS TS-UNIX BASH! AND THIS IS UNIX LIKE AND UNIX LIKE SYSTEMS USES BASH!")
    elif command.lower().startswith("rm -rf /") or "shutdown" in command:
     print("Error: Dangerous command blocked!")
    elif command.lower() == "remove":
       print("Goodbye! You have removed the TS-UNIX system.")
       os.system("sudo apt remove ts-unix")
    elif command.lower() == "features":
       os.system("/usr/bin/ts-unix --features")  # Execute features command
    else:
     os.system(command)  # Execute command

print("TS-UNIX session ended.")
