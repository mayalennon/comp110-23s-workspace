"""Practice with Dictionaries."""

ice_cream: dict[str,int] = {"chocolate": 12, "vanilla" : 8, "strawberry" : 5}
ice_cream["mint"] = 3
ice_cream.pop("mint")
print(ice_cream)


#accessing
print(f"The number of vanilla orders is {ice_cream['vanilla']}.")
ice_cream["vanilla"] += 1
print(f"The number of vanilla orders is {ice_cream['vanilla']}.")
print(len(ice_cream))
print("mint" in ice_cream)
print("chocolate" in ice_cream)

def zip(keys: list[str],values: list[int]) -> dict[str,int]:
    name_and_number: dict[str,int] = {}
    if (len(keys) != len(values)) or (len(keys) == 0) or (len(values) == 0):
        return name_and_number
    for elem in keys:
        name_and_number[keys] = values[elem]
    return name_and_number