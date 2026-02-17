#!/usr/bin/python3
import sys, os, re

# TitaniumQ Independent Engine v4.0
# Developed by: Anshik Pathak | Titanium Force Laboratory

memory = {}
LIB_PATH = "./tqlib"

def tq_eval(expr):
    try:
        # Pure math logic without external libraries
        temp_expr = str(expr)
        for var in sorted(memory.keys(), key=len, reverse=True):
            if var in temp_expr:
                temp_expr = temp_expr.replace(var, str(memory[var]))
        return eval(temp_expr)
    except:
        return str(expr).strip('"')

def load_module(module_name):
    file_path = os.path.join(LIB_PATH, f"{module_name}.tq")
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                if "rakho" in line:
                    process_line(line.strip())
    else:
        print(f"TitaniumQ Error: Module '{module_name}' nahi mila.")

def process_line(line):
    if not line or line.startswith("//"): return
    
    # ZARURAT - Load Native Library
    if line.startswith("zarurat "):
        load_module(line.split(" ")[1])
    
    # RAKHO - Store in Memory
    elif line.startswith("rakho "):
        parts = line[6:].split("=")
        memory[parts[0].strip()] = tq_eval(parts[1].strip())
    
    # BOL - Print
    elif line.startswith("bol "):
        print(tq_eval(line[4:].strip()))

def run_tq(filename):
    try:
        with open(filename, 'r') as f:
            for line in f:
                process_line(line.strip())
    except Exception as e:
        print(f"Runtime Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1: run_tq(sys.argv[1])
