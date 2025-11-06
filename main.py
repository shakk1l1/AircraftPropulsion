import iterationTt2
import FailSafe
import Conversion
import ListOfEquation

on = True

while on:
    command = input(">> ")
    match command:
        case "quit":
            on = False

        case "help":
            print("List of commands:")
            print("- quit: exit the program")
            print("- SLS ISA: set Ta and Pa to standard sea level conditions")
            print("- Tt2 Iteration: perform Tt2 iteration")
            print("- conversion: unit conversion tool")
            print("- define: define a variable value")
            print("- list equations: list all available equations")
            print("- list variables: list all available variables")
            print("- get equation: get the equation for a specific variable")


        case "SLS ISA":
            ListOfEquation.variables_values["Ta"] = 288.15
            ListOfEquation.variables_values["pa"] = 101325

        case "Tt2 Iteration":
            if ListOfEquation.variables_values.get("Pressure Ratio") == None:
                print("Pressure Ratio not defined")
                ListOfEquation.variables_values["pressureRatio"] = FailSafe.inputtofloat("Pressure Ratio: ")

            if ListOfEquation.variables_values.get("isentropic efficiency Compressor") == None:
                print("Isentropic Efficiency of Compressor not defined")
                ListOfEquation.variables_values["isentropic efficiency Compressor"] = FailSafe.inputtofloat("Isentropic Efficiency of Compressor: ")

            if ListOfEquation.variables_values.get("Tt1") == None:
                print("Tt1 not defined")
                ListOfEquation.variables_values["Tt1"] = FailSafe.inputtofloat("Tt1: ")

            ListOfEquation.variables_values["Tt2"], ListOfEquation.variables_values["gamma"] = (
                iterationTt2.iterateT2(ListOfEquation.variables_values["pressureRatio"], ListOfEquation.variables_values["isentropic efficiency Compressor"],
                                       ListOfEquation.variables_values["Tt1"], ListOfEquation.variables_values["r"]))

        case "define":
            var_name = input("Enter variable name to define: ")
            FailSafe.strinlist(var_name, ListOfEquation.variables_dictionary.keys())
            var_value = FailSafe.inputtofloat(f"Enter value for {var_name}: ")
            ListOfEquation.variables_values[var_name] = var_value
            print(f"{var_name} set to {var_value}")

        case "list equations":
            ListOfEquation.list_equations()

        case "list variables":
            ListOfEquation.list_variables()

        case "get equation":
            var_name = input("Enter variable name to get equation for: ")
            FailSafe.strinlist(var_name, ListOfEquation.variables_dictionary.keys())
            ListOfEquation.specific_equation(var_name)

        case "conversion":
            Conversion.main()

        case _:
            print("error")
            print("Unkown command")
            print("Type help for a list of commands")