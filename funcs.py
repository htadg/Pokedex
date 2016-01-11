

def format_name(name):
    index = len(name) + 1
    for a in range(1, len(name)):
        if name[a].isupper():
            index = a
            break
    return name[:index]


def format_type(pok_type):
    nature = []
    indices = []
    for a in range(1,len(pok_type)):
        if pok_type[a].isupper():
            indices.append(a)
    if len(indices) < 1 :
        return pok_type

    start = 0
    end = 0

    for b in indices:
        # print b
        start = end
        end = b
        nature.append(pok_type[start:end])
    nature.append(pok_type[end:len(pok_type)])

    return nature
