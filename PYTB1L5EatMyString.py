import time

def functievandestring(s):   
    s = s[0:len(s)-1]
    if len(s) != 0:
        print(s)
        functievandestring(s)
    elif len(s) == 0:
        print('')
        return
    
zin = "Mijn naam is Ahmet Asut"
time.sleep(1)
print ("Mijn naam is Ahmet Asut")
time.sleep(0.5)
functievandestring(zin)
print("Ik ben opgegeten :)")