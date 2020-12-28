import math
import time

def passord(tid):
    A = [0]
    for i in range(1, tid):
        A.append(0)
    ledende = tid - 4
    if ledende >= 10:
        tier = math.floor(ledende/10)
        ener = ledende % 10
        A[0] = tier
        A[1] = ener
        A[2] = 2
        A[3] = 1
        A[ledende] = 1
    else:
        A[0] = ledende
        A[1] = 2
        A[2] = 1
        A[ledende] = 1
    return A

t = time.localtime()
svar = passord(t.tm_min)
print("Tast inn passord")
tekst = input()
arr = list(tekst)
for i in range(0, len(arr)-1):
    arr[i] = int(arr[i])
x = True
if len(arr) == len(svar):
    for i in range(0, len(svar)-1):
        if arr[i] != svar[i]:
            x = False
else: x = False
if x:
    print("Riktig passord")
else: print("Feil passord")