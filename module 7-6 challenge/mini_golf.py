holes = int(input('How many holes did you play?: '))
hits = 0
holes = range(1, holes + 1)
for hole in holes:
    hit = int(input(f'Enter hits for hole {hole}: '))
    hits += hit
print(f'Total Hits: {hits}')