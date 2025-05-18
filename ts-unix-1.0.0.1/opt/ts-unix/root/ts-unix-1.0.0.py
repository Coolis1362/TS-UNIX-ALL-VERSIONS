#!/usr/bin/env python3
import os

def ts_unix_prompt():
    user = os.environ.get("USER", "ts-unix")  # Safer way to get username
    cwd = os.getcwd()  # Get current directory
    return f"{user}@TS-UNIX:{cwd}$ "  # Custom TS-UNIX prompt

print("Coolis1362 And Tadeosoft Copyright (C) 2025 All Rights Reserved")
while True:
    command = input(ts_unix_prompt())  # Show prompt and get input
    if command.lower() in ["exit", "quit"]:
        break
    elif command.lower() == "ts-unix-version":
        print("TS-UNIX version 1.0.0.1")
    elif command.lower() == "help":
        print("THE SAME AS UNIX AND LINUX AND MACOS THIS IS TS-UNIX BASH! AND THIS IS UNIX LIKE AND UNIX LIKE SYSTEMS USES BASH!")
    elif command.lower().startswith("rm -rf /") or "shutdown" in command:
     print("Error: Dangerous command blocked!")
    else:
     os.system(command)  # Execute command

print("TS-UNIX session ended.")
