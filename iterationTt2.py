from FailSafe import *

def iterateT(pressureRatio, isentEffCompr, Tt1, r):
    gammaprev = 0
    gamma = inputtofloat("First Guess of Gamma: ")
    Tt2 = 0
    Tt2i = 0
    Cp = 0
    while abs(gamma- gammaprev) > 0.001:
        gammaprev = gamma
        Tt2i = Tt1*((pressureRatio)**((gamma-1) / gamma))
        print("Tt2i: ", Tt2i)
        Tt2 = ((Tt2i-Tt1)/ isentEffCompr) + Tt1
        print("Tt2: ", Tt2)
        Ttc = (Tt1 + Tt2)/2
        print("Ttc: ", Ttc)
        Cp = inputtofloat("Cp from Graph with Ttc: ")
        gamma = Cp / (Cp - r)
        print("New gamma: ", gamma)
    print("Final Gamma: ", gamma)
    print("Final Tt2i: ", Tt2i)
    print("Final Tt2: ", Tt2)
    print("Final Cp: ", Cp)
    return Tt2, gamma, Cp