import os

def ts_unix_prompt():
    user = os.environ.get("USER", "ts-unix")  # Safer way to get username
    cwd = os.getcwd()  # Get current directory
    return f"{user}@TS-UNIX:{cwd}$ "  # Custom TS-UNIX prompt

while True:
    command = input(ts_unix_prompt())  # Show prompt and get input
    if command.lower() in ["exit", "quit"]:
        break
    os.system(command)  # Execute command

print("TS-UNIX session ended.")

