"""Practice with for loops."""

pets: list[str] = ["Louie","Bo","Bear"]

for pet in pets:
    print(f"Good boy, {pet}!")

d_coordinate: tuple[float,float,float] = (1.0,1.0,1.0)
Player = tuple[str, int]
lebron: Player = ("James",6)
mj: Player = ("Jordan", 23)

#thenameoftherange_range= range(start,end, step = 1) 

names: list[str] = ["Alyssa","Janet","Vrinda"]
for idx in range(0,3):
    print(f"{idx}: {names[idx]}")
    
    
def sum(xs: list[float]) -> float:
    """return sum off all elements in xs"""
    sum_total: float = 0.0
    idx: int = 0
    while idx < len(xs):
        sum_total += xs[idx]
        idx += 1
    return sum_total