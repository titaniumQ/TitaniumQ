import sys, os, re

# TitaniumQ Engine v4.1 (Regex Patch)
memory = {}
LIB_PATH = "/data/data/com.termux/files/usr/etc/tqlib"

def tq_eval(expr):
    try:
        temp_expr = str(expr)
        # Regex \b ensures we only replace whole words, not letters inside words
        for var in sorted(memory.keys(), key=len, reverse=True):
            temp_expr = re.sub(r'\b' + re.escape(var) + r'\b', str(memory[var]), temp_expr)
        return eval(temp_expr)
    except:
        return str(expr).strip('"')

def load_module(module_name):
    paths = ["./tqlib", LIB_PATH]
    found = False
    for p in paths:
        file_path = os.path.join(p, f"{module_name}.tq")
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                for line in f: process_line(line.strip())
            found = True
            break
    if not found: print(f"Error: Module {module_name} not found.")

def process_line(line):
    if not line or line.startswith("//"): return
    if line.startswith("zarurat "): load_module(line.split(" ")[1])
    elif line.startswith("rakho "):
        parts = line[6:].split("=", 1)
        memory[parts[0].strip()] = tq_eval(parts[1].strip())
    elif line.startswith("bol "): print(tq_eval(line[4:].strip()))
    elif line.startswith("chalao "): os.system(tq_eval(line[7:].strip()))

def run_tq(filename):
    try:
        with open(filename, 'r') as f:
            for line in f: process_line(line.strip())
    except Exception as e: print(f"Runtime Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1: run_tq(sys.argv[1])
