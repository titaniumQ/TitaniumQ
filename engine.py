#!/usr/bin/python3
import sys, os, re

# TitaniumQ Power Engine v4.0 (Standardized)
memory = {}
# Termux path for libraries
LIB_PATH = "/data/data/com.termux/files/usr/etc/tqlib" 

def tq_eval(expr):
    try:
        # Variables support including dot-logic in names if needed
        temp_expr = str(expr)
        for var in sorted(memory.keys(), key=len, reverse=True):
            if var in temp_expr:
                temp_expr = temp_expr.replace(var, str(memory[var]))
        return eval(temp_expr)
    except:
        return str(expr).strip('"')

def load_module(module_name):
    # Pehle local folder check karega, phir system folder
    paths = ["./tqlib", LIB_PATH]
    found = False
    for p in paths:
        file_path = os.path.join(p, f"{module_name}.tq")
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                for line in f:
                    process_line(line.strip())
            found = True
            break
    if not found:
        print(f"TitaniumQ Error: Module '{module_name}' not found in system paths.")

def process_line(line):
    if not line or line.startswith("//"): return
    
    if line.startswith("zarurat "):
        load_module(line.split(" ")[1])
    elif line.startswith("rakho "):
        parts = line[6:].split("=", 1)
        memory[parts[0].strip()] = tq_eval(parts[1].strip())
    elif line.startswith("bol "):
        print(tq_eval(line[4:].strip()))
    elif line.startswith("chalao "):
        os.system(tq_eval(line[7:].strip()))

def run_tq(filename):
    try:
        with open(filename, 'r') as f:
            for line in f:
                process_line(line.strip())
    except Exception as e:
        print(f"Runtime Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1: run_tq(sys.argv[1])
