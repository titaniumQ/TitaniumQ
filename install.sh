#!/bin/bash
# TitaniumQ Universal Installer v4.0
# Developed by Anshik Pathak | Titanium Force Laboratory

echo "[*] Initializing TitaniumQ Setup..."

# Step 1: Dependencies
pkg install python git -y

# Step 2: Download TitaniumQ and Libraries
echo "[*] Downloading Core Engine and Native Libraries..."
# Pura folder structure download karne ke liye hum git clone ka use karenge
git clone https://github.com/TitaniumQ/TitaniumQ.git $HOME/TitaniumQ_Temp

# Step 3: Setup Binaries
echo "[*] Configuring system binaries..."
chmod +x $HOME/TitaniumQ_Temp/tq.py
cp $HOME/TitaniumQ_Temp/tq.py $PREFIX/bin/tq

# Move Libraries to a safe place
mkdir -p $PREFIX/etc/tqlib
cp -r $HOME/TitaniumQ_Temp/tqlib/* $PREFIX/etc/tqlib/

# Cleanup
rm -rf $HOME/TitaniumQ_Temp

echo "------------------------------------------------"
echo "  TitaniumQ v4.0 Installed Successfully!        "
echo "  Native Libraries: Ganit, Vigyan, Tantra Loaded"
echo "------------------------------------------------"
