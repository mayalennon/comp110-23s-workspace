def zip(keys: list[str],values: list[int]) -> dict[str,int]:
    name_and_number: dict[str,int] = {}
    if (len(keys) != len(values)) or (len(keys) == 0) or (len(values) == 0):
        return name_and_number
    idx: int = 0
    while idx < len(keys) :
        name_and_number[keys[idx]] = values[idx]
        idx += 1
    return name_and_number