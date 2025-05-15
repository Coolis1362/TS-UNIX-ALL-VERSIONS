#!/bin/bash

# Say this is TS-UNIX Filesystem Setup
echo "Welcome To TS-UNIX Filesystem /home Folder Setup!"

# Define The Folder Loction Of /home
HOME_DIR="$HOME/TS-UNIX-ALL-VERSIONS/1.x.x/1.0.x/1.0.0/root/home"

# Define The Subfolders Of /home
HOME_SUBFOLDERS=("ADMIN_USER" "USER")

# Define The Subfolders Of /home/ADMIN_USER & /home/USER
USER_FOLDERS_SUBFOLDERS=("devscripts" "devprojects")

# Make The main /home Folder
echo "Initializing TS-UNIX /home structure..."
mkdir -p "$HOME_DIR"

# Make Subfolders 1
for dir1 in "${HOME_SUBFOLDERS[@]}"; do
    mkdir -p "$HOME_DIR/$dir1"
    echo "Created: $HOME_DIR/$dir1"
done
# Make Subfolders 2
for dir2 in "${USER_FOLDERS_SUBFOLDERS[@]}"; do
    mkdir -p "$HOME_DIR/$dir1/$dir2"
    echo "Created: $HOME_DIR/$dir1/$dir2"
done

echo "TS-UNIX /home setup complete!"
