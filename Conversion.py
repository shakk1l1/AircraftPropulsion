import FailSafe

def ftTom(x):
    return x*0.3048

def ktTomps(x):
    return x*0.5144

def lbfTokg(x):
    return x*0.45359

def lbfTon(x):
    return x*4.4482

def kcalToj(x):
    return x*4187

def btuToj(x):
    return x*1055

def rToK(x):
    return x*(5/9)

def psiToPa(x):
    return x*6.89*1000

def kgfpcm2ToPa(x):
    return x*9.81*(10**4)

def barToPa(x):
    return x*(10**5)

def dinhpToW(x):
    return x*736

def fToK(x):
    return ((x - 32) * (5/9))+ 273.15

def hpimperialToW(x):
    return x*745.7

def lbphrTokgps(x):
    return x*0.0001259979

def lbpsTokgps(x):
    return x*0.4627586207

def lbtodaN(x):
    return x*0.455

unit = ["ft", "kt", "lb", "lbf", "kcal", "BTU", "R", "psi", "kgf/cm2", "bar", "DINhp", "°F", "hp(imperial)", "lbph"]

def convert(value, from_unit):
    match from_unit:
        case "ft":
            return ftTom(value)
        case "kt":
            return ktTomps(value)
        case "lb":
            return lbfTokg(value)
        case "lbf":
            return lbfTon(value)
        case "kcal":
            return kcalToj(value)
        case "BTU":
            return btuToj(value)
        case "R":
            return rToK(value)
        case "psi":
            return psiToPa(value)
        case "kgf/cm2":
            return kgfpcm2ToPa(value)
        case "bar":
            return barToPa(value)
        case "DINhp":
            return dinhpToW(value)
        case "°F":
            return fToK(value)
        case "hp(imperial)":
            return hpimperialToW(value)
        case "lbph":
            return lbphrTokgps(value)
        case "lb/s":
            return lbpsTokgps(value)
        case "lb (to daN)":
            return lbtodaN(value)
        case _:
            return "Invalid unit"

def main():
    print("Available units for conversion to SI:")
    for u in unit:
        print(f"- {u}")
    from_unit = input("Enter the unit you want to convert from: ")
    from_unit = FailSafe.strinlist(from_unit, unit)
    value = FailSafe.inputtofloat(f"Enter the value in {from_unit}: ")
    result = convert(value, from_unit)
    print(f"The converted value is: {result} in SI units.")