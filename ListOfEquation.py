equations = [
    "Pt = Pc + Pl + Pfa",
    "Pt = mdottot * Cp34 * (Tt3 - Tt4)",
    "Pc = mdota * Cp12 * (Tt2 - Tt1)",
    "mdottot = mdota + mdotf",
    "isentropic efficiency Compressor = (Tt2i - Tt1) / (Tt2 - Tt1)",
    "gamma = Cp / (Cp - r)",
    "HR = Qdot / Pl",
    "mdota (ht2 - hR) + mdotf (htf - hR) + etacc * qc1 * mdotf = mdottot (ht3 - hR)",
    "delta h = Cp * delta T",
    "mdota Cp2r (Tt2 - TR) + etacc * qc1 * mdotf = mdottot Cp3r (Tt3 - TR)",
    "Cpxy is Cp at Ttc = (Ttx + Tty) / 2",
    "SFC = mdotf / Pl",
    "mdotf = SHP * SFC",
    "FAR obtained from graph with CP and Tt4",
    "Ta = Tt",
    "pa = pt if velocity negligible",
    "EGT = Tt4",
    "Tt2i / Tt1 = (pressureRatio) ** ((gamma - 1) / gamma)",
    "Tt2 = ((Tt2i - Tt1) / isentropic efficiency Compressor) + Tt1"
    "gamma = obtain by iteration using Cp from graph at Ttc = (Tt1 + Tt2) / 2",
    "Tt obtained by FAR and Cp guess and graph (iteration of Cp and Tt)",
    "Pta = Pa * (1 + (gamma - 1) / 2 * Ma^2)^(gamma / (gamma - 1))",
    "Tta = Ta * (1 + (gamma - 1) / 2 * Ma^2)",
    "va = Ma * sqrt(gamma * r * Ta)",
    "Pt1 = RR * Pta if nozzle",
    "Tt1 = Tta if adiabatic inlet",
    "T = ((mdota + mdotf) * vj - mdota * va)) + (P5 - Pa) * A5 mdotf might be negligible",
    "P5 = Pa if fully expanded nozzle"
]

variables_dictionary = {
    "Pt": "Turbine Power",
    "Pc": "Compressor Power",
    "Pl": "Load Power",
    "Pfa": "Loss Power due to Friction and Accessories",
    "mdottot": "Total Mass Flow Rate",
    "Cp34": "Specific Heat Capacity between Tt3 and Tt4",
    "Tt3": "Total Temperature at Station 3",
    "Tt4": "Total Temperature at Station 4",
    "mdota": "Mass Flow Rate of Air",
    "Cp12": "Specific Heat Capacity between Tt1 and Tt2",
    "Tt2": "Total Temperature at Station 2",
    "Tt1": "Total Temperature at Station 1",
    "mdotf": "Mass Flow Rate of Fuel",
    "Tt2i": "Isentropic Total Temperature at Station 2",
    "isentropic efficiency Compressor": "Isentropic Efficiency of the Compressor",
    "gamma": "Ratio of Specific Heats",
    "Cp": "Specific Heat Capacity at Constant Pressure",
    "r": "Specific Gas Constant",
    "HR": "Heat Rate",
    "Qdot": "Rate of Heat Addition",
    "hR": "Reference Enthalpy",
    "ht2": "Total Enthalpy at Station 2",
    "htf": "Total Enthalpy of Fuel",
    "etacc": "Combustion Efficiency",
    "qc1": "Heating Value of Fuel",
    "ht3": "Total Enthalpy at Station 3",
    "delta h": "Change in Enthalpy",
    "Cp2r": "Specific Heat Capacity at Ttc between Tt2 and TR",
    "TR": "Reference Temperature",
    "Cp3r": "Specific Heat Capacity at Ttc between Tt3 and TR",
    "SFC": "Specific Fuel Consumption",
    "FAR": "Fuel-Air Ratio",
    "Ta": "Ambient Temperature",
    "pa": "Ambient Pressure",
    "EGT": "Exhaust Gas Temperature",
    "pressureRatio": "Pressure Ratio across the Compressor",
    "SHP": "Shaft Horsepower",
    "Tta": "Total Temperature at Ambient",
    "Pta": "Total Pressure at Ambient",
    "Ma": "Mach Number",
    "RR": "Ram Recovery Factor",
    "Tt": "Total Temperature",
    "T": "Thrust",
    "P5": "Pressure at Nozzle Exit",
    "va": "Ambient Velocity",
    "vj": "Jet Velocity",
    "A5": "Nozzle Exit Area"
}

variables_values = {
    "Pt": None,
    "Pc": None,
    "Pl": None,
    "Pfa": None,
    "mdottot": None,
    "Cp34": None,
    "Tt3": None,
    "Tt4": None,
    "mdota": None,
    "Cp12": None,
    "Tt2": None,
    "Tt1": None,
    "mdotf": None,
    "Tt2i": None,
    "isentropic efficiency Compressor": None,
    "gamma": None,
    "Cp": None,
    "r": 287,
    "HR": None,
    "Qdot": None,
    "hR": None,
    "ht2": None,
    "htf": None,
    "etacc": None,
    "qc1": None,
    "ht3": None,
    "delta h": None,
    "Cp2r": None,
    "TR": None,
    "Cp3r": None,
    "SFC": None,
    "FAR": None,
    "Ta": None,
    "pa": None,
    "EGT": None,
    "pressureRatio": None,
    "SHP": None,
    "Tta": None,
    "Pta": None,
    "Ma": None,
    "RR": None,
    "Tt": None,
    "T": None,
    "P5": None,
    "va": None,
    "vj": None,
    "A5": None
}

def list_equations():
    print("List of Equations:")
    for eq in equations:
        print("- " + eq)

def list_variables():
    print("List of Variables:")
    # print variables with their descriptions
    for var in variables_dictionary:
        print(f"- {var}: {variables_dictionary.get(var, 'No description available')}")

def specific_equation(unknown_variable):
    specific_eq = []
    for eq in equations:
        if unknown_variable in eq:
            specific_eq.append(eq)
    if specific_eq == []:
        print("No equation found involving " + unknown_variable)
    else:
        print("Equation involving " + unknown_variable + ":")
        for eq in specific_eq:
            print("- " + eq)