def clock_solution(config):
    algs={
        "e":"Dn- DURn+ DULn+ ALLn-",
        "c":"DULn- ALLn",
        "m":"URn+ DLn+ URDLn-"
    }
    position_map="cecemececeemee"
    out=""
    for clock in range(int(len(config)/2)):
        out+=format_clock(config[clock*2]+config[clock*2+1],algs[position_map[clock]])
    return out
def format_clock(position,solution):
    out=""
    if "0" in position:
        return out
    for char in solution:
        if char=="n":
            out+=position
        else:
            out+=char
    return out+" "
