input = "aaabbbbaaac"
o = ""
for ch in input:
    if ch not in o:
        o += ch
        
print(o)
