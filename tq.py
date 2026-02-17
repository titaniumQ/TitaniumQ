#!/usr/bin/python3
import sys, os, re

# TitaniumQ Engine v4.1 (Regex Patch + Absolute Path)
# Developed by Anshik Pathak | Titanium Force Laboratory

memory = {}
# Termux standard library path
LIB_PATH = "/data/data/com.termux/files/usr/etc/tqlib"

def tq_eval(expr):
    try:
        temp_expr = str(expr).strip()
        # Word boundary \b prevents replacing letters inside words (e.g., 'E' in 'SYSTEM')
        for var in sorted(memory.keys(), key=len, reverse=True):
            temp_expr = re.sub(r'\b' + re.escape(var) + r'\b', str(memory[var]), temp_expr)
        
        # Safe evaluation for math and strings
        return eval(temp_expr, {"__builtins__": None}, {})
    except:
        return str(expr).strip('"')

def load_module(module_name):
    # Search in local folder first, then system etc folder
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
        print(f"TitaniumQ Error: Module '{module_name}' not found.")

def process_line(line):
    if not line or line.startswith("//"):
        return
    
    # Keyword: ZARURAT (Import)
    if line.startswith("zarurat "):
        load_module(line.split(" ")[1])
    
    # Keyword: RAKHO (Variable)
    elif line.startswith("rakho "):
        if "=" in line:
            parts = line[6:].split("=", 1)
            var_name = parts[0].strip()
            memory[var_name] = tq_eval(parts[1].strip())
    
    # Keyword: BOL (Print)
    elif line.startswith("bol "):
        val = line[4:].strip()
        print(tq_eval(val))
    
    # Keyword: CHALAO (System Command)
    elif line.startswith("chalao "):
        cmd = tq_eval(line[7:].strip())
        os.system(cmd)

def run_tq(filename):
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' nahi mili.")
        return
    try:
        with open(filename, 'r') as f:
            for line in f:
                process_line(line.strip())
    except Exception as e:
        print(f"TitaniumQ Runtime Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_tq(sys.argv[1])
    else:
        print("Uso: tq <filename.tq>")
