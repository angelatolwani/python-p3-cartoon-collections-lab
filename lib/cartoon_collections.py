def roll_call_dwarves(dwarves):
    for i in range(0, len(dwarves)):
        print(f"{i+1}. {dwarves[i]}")

def summon_captain_planet(calls):
    # newList = []
    # for call in calls:
        # newList.append(f"{call.capitalize()}!")
    new_list = [f"{call.capitalize()}!" for call in calls]
    # print(newList)
    return new_list


def long_planeteer_calls(word_list):
    for word in word_list:
        if len(word) > 4:
            return True
    return False
            

def find_the_cheese(ingredients):
    cheeses = ["cheddar", "gouda", "camembert"]
    for food in ingredients:
        if food in cheeses:
            return food



soup = ["tomato soup", "cheddar", "oyster crackers", "gouda"]
find_the_cheese(soup)