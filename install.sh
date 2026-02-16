#!/bin/bash
# TitaniumQ Universal Installer
# Developed by Anshik Pathak | Titanium Force Laboratory

echo "[*] Initializing TitaniumQ Engine Setup..."

# Step 1: Checking and Installing Dependencies
echo "[*] Checking system dependencies..."
pkg install python -y

# Step 2: Downloading the Core Engine
echo "[*] Fetching TitaniumQ Core from official repository..."
# Using the URL provided: https://raw.githubusercontent.com/TitaniumQ/TitaniumQ/main/tq.py
curl -O https://raw.githubusercontent.com/TitaniumQ/TitaniumQ/main/tq.py

# Step 3: Configuring Permissions and Global Access
echo "[*] Configuring system binaries..."
chmod +x tq.py

# Moving the engine to the system bin directory
mv tq.py $PREFIX/bin/tq

# Final Output
echo "------------------------------------------------"
echo "  TitaniumQ Framework Successfully Installed!   "
echo "  Version: 1.5 (Stable)                         "
echo "  Status: System Ready                          "
echo "------------------------------------------------"
echo "[+] Titanium Force Laboratory - Mission Accomplished"
