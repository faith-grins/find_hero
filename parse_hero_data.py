from pickle import load, dump

HERO_NAMES = ['Leonhardt', 'Ladius', 'Thoma', 'Duran', 'Rex']
with open('hero_data.txt', 'r') as file_in:
    hero_data = [line.strip() for line in file_in if line.strip() != '']
gen = [i for i in range(7)]
for i in range(len(hero_data)):
    for j in range(1, 6):
        if hero_data[i].endswith(str(j).join(['<GEN', '>'])):
            gen[j] = i
    if hero_data[i].endswith('<WPR>'):
        gen[6] = i
hero_strings = [hero_data[gen[i]:gen[i+1]] for i in range(1, 6)]
for h in hero_strings:
    for i in range(len(h)):
        line = [j for j in h[i].split(' ') if j != '']
        h[i] = ' '.join(line)
hero_data = {HERO_NAMES[i]: hero_strings[i] for i in range(5)}
for name in hero_data:
    hero_data[name] = [line for line in hero_data[name] if not line.startswith(name)]
    breaks = [0]
    breaks.extend([hero_data[name].index(line) for line in hero_data[name] if line.endswith('>')])
    breaks.append(-1)
    hero_data[name] = [hero_data[name][breaks[i]:breaks[i+1]] for i in range(len(breaks))
                       if i != len(breaks)-1 and
                       hero_data[name][breaks[i]:breaks[i+1]]]
    l = []
    for lineage in hero_data[name]:
        stats = {line.split(' ')[0]: line.split(' ')[1:] for line in lineage}
        for st in stats:
            split = stats[st][0].split('-')
            if len(split) > 1:
                stats[st][0] = split[0]
                stats[st].insert(1, split[1])
        l.append(stats)
    hero_data[name] = l


with open('proficiency_costs', 'rb') as file_in:
    prof_costs = load(file_in)

print(len(hero_data[HERO_NAMES[2]]))

