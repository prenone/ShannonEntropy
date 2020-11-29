#       Shannon Entropy Calculator
#       Achille Merendino (@prenone)
#       29 November 2020

#       Utilizzo
#       1. Stringa inserita tramite standard input
#          >python3 entropy.py
#          X[i]: This is my message!
# 
#       2. Stringa letta da file
#          >python3 entropy.py ./my_file.txt                   

import sys
import math

if len(sys.argv) < 2:
    xis = input("X[i]: ")
else:
    fr = open(sys.argv[1], "r")
    xis = fr.read()
    fr.close()

symb = len(xis)

#Misura la probabilità associata a ogni carattere presente nella poesia
p = {}
for char in xis.lower():
    if char not in p:
        p[char] = 0
    p[char] += 1

for x, t_x in p.items():
    p[x] = t_x / symb

#Mostra le probabilità delle variabili misurate in ordine decrescente
for x, p_x in sorted(p.items()):
    print("P('{}'): {}".format(x, p_x))

#Calcola l'entropia di Shannon
h = 0
for p_x in p.values():
    h += p_x * math.log(p_x, 2)
h = -h

print("H(X) = {}".format(h))