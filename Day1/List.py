people : list[str] = ['Mario','Luigi', 'Peach','Peach','Toad']
people2: list[str] = ['Mario', 'Luigi']
people.extend(people2)
people.sort()
print(people)