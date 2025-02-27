"""
This implements the posibility to read color codes for certain output and then print 
the colors that way

usage: print(colored_output("input"))

f strings etc, obv supported since this only changes the text color
"""

import json

# TODO: Not sure how to implement multiple colors to return from the function maybe an array ?

def hex_to_rbg():
    hex_code = "000000"
    try:
        with open("config.json", "r") as file:
            config = json.load(file)
            session_timer = config.get("general", {}).get("session_timer", "#ffffff") # the last value is the default value if there is none found
            hex_code = session_timer.lstrip("#")
    except (FileNotFoundError, json.JSONDecodeError):
        hex_code = ("ffffff")
    return tuple(int(hex_code[i:i+2], 16) for i in (0,2,4))

def colored_output(input):
    r, g, b = hex_to_rbg()
    return f"\033[38;2;{r};{g};{b}m{input}\033[0m"

