import sys
def OneToOne (): 
    if len(sys.argv)<3:
        return (str(False) + " Please enter 2 strings")  
    S1 = sys.argv[1]
    S2 = sys.argv[2]       
    if len(S1)!=len(S2):
        return False
    
    Dict1={}
    for i in range(len(S1)):
        if  S1[i] not in Dict1.keys():
            Dict1[S1[i]]=S2[i]
        else:
            if Dict1[S1[i]]!=S2[i]:
                return False
    return True
print(OneToOne())