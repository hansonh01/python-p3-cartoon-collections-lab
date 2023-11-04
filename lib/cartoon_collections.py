def roll_call_dwarves(dwarves):
    for index,dwarve in enumerate(dwarves,start=1):
        print(f"{index}. {dwarve}")

def summon_captain_planet(planeteer_calls):
    calls = []
    for element in planeteer_calls:
        calls.append(element.capitalize() + "!")
    return calls

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(lst):
    cheese_types = ["cheddar", "gouda", "camembert"]
    for items in lst:
        if items in cheese_types:
            return items
    return None