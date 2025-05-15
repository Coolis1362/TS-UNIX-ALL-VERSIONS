#!/bin/bash

# Define the root opt directory
OPT_DIR="$HOME/TS-UNIX-ALL-VERSIONS/1.x.x/1.0.x/1.0.0/root/opt"

# List of subdirectories
SUBDIRS=("third-party" "sandbox" "components")

# Create the directories
echo "Initializing TS-UNIX /opt structure..."
mkdir -p "$OPT_DIR"

for dir in "${SUBDIRS[@]}"; do
    mkdir -p "$OPT_DIR/$dir"
    echo "Created: $OPT_DIR/$dir"
done

echo "TS-UNIX /opt setup complete!"

