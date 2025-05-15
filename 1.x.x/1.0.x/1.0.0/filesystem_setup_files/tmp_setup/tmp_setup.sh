#!/bin/bash

# Define the `/tmp` setup directory
TMP_DIR="$HOME/TS-UNIX-ALL-VERSIONS/1.x.x/1.0.x/1.0.0/root/tmp"

# List of subdirectories within `/tmp`
SUBDIRS=("session" "logs" "cache" "swap" "sandbox")

# Create the main `/tmp` directory
echo "Initializing TS-UNIX /tmp structure..."
mkdir -p "$TMP_DIR"

# Create subdirectories
for dir in "${SUBDIRS[@]}"; do
    mkdir -p "$TMP_DIR/$dir"
    echo "Created: $TMP_DIR/$dir"
done

echo "TS-UNIX /tmp setup complete!"
