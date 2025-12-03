l = [True, True, True, True]

def absListe(liste):
    temp = []
    for l in liste:
        if l == True:
            temp.append(1)
        if l == False:
            temp.append(0)
    if sum(temp) == 0:
        return False
    elif sum(temp) == len(liste):
        return True
    else:
        return None
    
print(absListe(l))