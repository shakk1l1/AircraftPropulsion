# Aircraft Propulsion course helper

An interactive Python helper for the Aircraft Propulsion course at ULB.
It combines equation lookup, in-session variables, unit conversions, and a
compressor-temperature iteration using manually supplied heat-capacity values.

## Run

Python 3.10 or newer is required for the command dispatcher. This version uses
the Python standard library and local modules; no third-party installation is
needed.

```sh
git clone https://github.com/shakk1l1/AircraftPropulsion.git
cd AircraftPropulsion
python3 main.py
```

Type `help` at the `>>` prompt. Commands and variable names are case-sensitive.

## Commands

| Command | Action |
| --- | --- |
| `help` | List the commands |
| `list equations` | Display the stored equation notes |
| `list variables` | Display recognised variable names and descriptions |
| `get equation` | Find notes containing a selected variable name |
| `define` | Set a recognised variable for the current session |
| `SLS ISA` | Set ambient temperature to 288.15 K and pressure to 101325 Pa |
| `conversion` | Open the unit-conversion prompts |
| `Tt2 Iteration` | Run the compressor outlet-temperature iteration |
| `quit` | Exit |

## Small example

Start the program and enter:

```text
>> conversion
Enter the unit you want to convert from: ft
Enter the value in ft: 10
The converted value is: 3.048 in SI units.
>> quit
```

The program also prints its available units before the conversion prompts.

## Compressor-temperature iteration

Use `define` to set `pressureRatio`, `isentropic efficiency Compressor`, and
`Tt1`, or enter them when `Tt2 Iteration` prompts for missing values. Use absolute
temperature in kelvin and compatible SI units for `Cp` and the gas constant `r`.

The iteration asks for an initial `gamma`, computes an outlet temperature and a
mean temperature, then asks you to read `Cp` from the relevant course graph.
It updates `gamma = Cp / (Cp - r)` and repeats until the change in gamma is no
greater than 0.001. This is a manual property-lookup workflow, not an automatic
gas-property model. The default `r` is 287 J/(kg K).

`SLS ISA` sets ambient variables only; inlet total temperature `Tt1` still needs
to be supplied for the iteration. Session variables are not saved after exit.

## Files

- `main.py`: command interface.
- `ListOfEquation.py`: equation notes, variable descriptions, and session values.
- `Conversion.py`: unit-conversion functions and prompts.
- `iterationTt2.py`: compressor-temperature iteration.
- `FailSafe.py`: input helpers.

## Scope and checks

This is a teaching aid. Equation lookup displays notes rather than solving
arbitrary equations. The calculation routines and conversion factors have not
received a comprehensive numerical validation, and physical input constraints
are not fully enforced.

Run the command-interface regression tests with:

```sh
python3 -m unittest discover -s tests -v
```
