#!/bin/bash

# Define The root/etc directory
ETC_DIR="$HOME/TS-UNIX-ALL-VERSIONS/1.x.x/1.0.x/1.0.0/root/etc"

# List The hostname File
HOSTNAME_FILE=("hostname")

# Create the directories
echo "Initializing TS-UNIX /etc structure..."
mkdir -p "$ETC_DIR"

for file in "${HOSTNAME_FILE[@]}"; do
    touch "$ETC_DIR/$file"
    echo "Created: $ETC_DIR/$file"
done

echo "TS-UNIX /opt setup complete!"
