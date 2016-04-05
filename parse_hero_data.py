with open('hero_data.txt', 'rb') as file_in:
    hero_data = [line.strip() for line in file_in if line.strip() != '']
gen = range(6)
for i in range(len(hero_data)):
    for j in range(1, 6):
        if hero_data[i].endswith(str(j).join(['<GEN', '>'])):
            gen[j] = i
    if hero_data[i].endswith('<WPR>'):
        gen[6] = i
leon = hero_data[gen[1]:gen[2]]
ladius = hero_data[gen[2]:gen[3]]
thoma = hero_data[gen[3]:gen[4]]
duran = hero_data[gen[4]:gen[5]]
rex = hero_data[gen[5]:gen[6]]

print('\n'.join(leon))