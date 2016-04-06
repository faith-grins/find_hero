from pickle import dump, load
from re import findall

if __name__ == '__main__':
    with open('test_data', 'r') as file_in:
        data = file_in.read().split('\n\n')
    database = {}
    current_objects = []
    for block in data:
        if '[or]' not in block:
            current_objects = [block.split('  ')[0]]
        else:
            current_objects = findall('[A-Z]* ?[A-Z]{2,} ?[A-Z]{2,}', block)
        for o in current_objects:
            block = block.replace(o, '')
        block = block.replace('[or]', '')
        block = block.split('\n')
        print(current_objects, '\n')
        for line in block:
            line = [i for i in line.split('  ') if i != '']
            if len(line) < 2:
                continue
            obs = (line[0], line[1])
            for o in current_objects:
                if o not in database:
                    database[o] = ['+'.join(obs)]
                else:
                    database[o].append('+'.join(obs))
    pair = ['WERECAT', 'LYCANTHROPE']
    if all(p in database for p in pair) and len(set(database[pair[0]]).intersection(database[pair[1]])) > 0:
        print(set(database[pair[0]]).intersection(database[pair[1]]))
        with open('monster_combine.dct', 'wb') as file_out:
            dump(database, file_out)
    else:
        print('Failure')
