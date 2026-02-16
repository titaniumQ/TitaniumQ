#!/usr/bin/python3
import sys, re

# TitaniumQ Power Engine v1.5 - Titanium Force Laboratory
# Created by: Anshik Pathak
memory = {}

def tq_eval(expr):
    try:
        # Variables ko unki value se replace karna
        temp_expr = str(expr)
        for var in sorted(memory.keys(), key=len, reverse=True):
            if var in temp_expr:
                temp_expr = temp_expr.replace(var, str(memory[var]))
        # Math calculation
        return eval(temp_expr)
    except:
        return str(expr).strip('"')

def run_tq(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                if not line or line.startswith("//"):
                    i += 1
                    continue
                
                # BOL Command (Dot Logic)
                if line.startswith("bol "):
                    val = line[4:].strip()
                    if val.startswith('"') and val.endswith('"'):
                        print(val[1:-1].replace(".", " "))
                    else:
                        print(tq_eval(val))

                # RAKHO Command (Memory)
                elif line.startswith("rakho "):
                    parts = line[6:].split("=")
                    var_name = parts[0].strip()
                    memory[var_name] = tq_eval(parts[1].strip())

                # INPUT (Pucho) Logic
                elif "pucho" in line and "=" in line:
                    parts = line.replace("rakho ", "").split("=")
                    var_name = parts[0].strip()
                    prompt = re.findall(r'"(.*?)"', line)
                    memory[var_name] = input(prompt[0] if prompt else "")

                # BAS (Finish)
                elif line == "bas":
                    break
                i += 1
    except Exception as e:
        print(f"TitaniumQ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_tq(sys.argv[1])
