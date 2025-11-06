def inputtoint(text):
    inp = None
    while(type(inp) != int):
        inp = input(text)
        try:
            inp = int(inp)
        except ValueError:
            print("error")
            print("Please enter an integer: ")
    return inp

def inputtofloat(text):
    inp = None
    while (type(inp) != float):
        inp = input(text)
        try:
            inp = float(inp)
        except ValueError:
            print("error")
            print("Please enter an flaot: ")
    return inp

def inputtostr(text):
    inp = None
    while (type(inp) != str):
        inp = input(text)
        try:
            inp = str(inp)
        except ValueError:
            print("error")
            print("Please enter a string: ")
    return inp

def strinlist(string, lst):
    while string not in lst:
        print("Not in list")
        string = input("Enter again: ")
    return string
