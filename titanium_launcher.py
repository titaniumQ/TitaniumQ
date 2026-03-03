import sys
import os

def load_rules():
    rules = {}
    # rules.txt ko load karne ke liye
    if os.path.exists("rules.txt"):
        with open("rules.txt", "r", encoding="utf-8") as f:
            for line in f:
                if ":" in line:
                    k, v = line.split(":", 1)
                    rules[k.strip()] = v.strip()
    return rules

def main():
    if len(sys.argv) < 2:
        print("TitaniumQ: tq <file.tq> likho!")
        return
    
    rules = load_rules()
    tq_file = sys.argv[1]
    
    if not os.path.exists(tq_file):
        print(f"Galti: {tq_file} nahi mili!")
        return

    with open(tq_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"): continue
            
            # 1. 'bol' aur 'dikhao' ka logic
            if line.startswith("bol") or line.startswith("dikhao"):
                # Quote ke andar ka maal nikalna
                text = line.split('"', 2)
                if len(text) >= 2:
                    print(text[1])
                else:
                    # Bina quote wala simple text
                    print(line.split(' ', 1)[1])
            
            # 2. 'jama' (Addition) ka logic
            elif line.startswith("jama"):
                numbers = line.split(' ')[1:]
                print(sum(float(n) for n in numbers))
                
            # 3. Baaki rules ke liye basic check
            elif line.split(' ')[0] in rules:
                print(f"[Titanium Force]: {line.split(' ')[0]} command active.")
            
            else:
                print(f"Sawal: '{line}' Titanium database mein nahi hai.")

if __name__ == "__main__":
    main()
