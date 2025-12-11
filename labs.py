l = [False, False, False, False]

def absListe(liste):
    temp = 0
    for l in liste:
        if l == True:
            temp += 1
        
    if temp == 0:
        return False
    elif temp == len(liste):
        return True
    else:
        return None
    
print(absListe(l))