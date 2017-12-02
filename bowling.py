def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
        else:
            result += get_value(game[i])
        if frame < 10  and get_value(game[i]) == 10:
            if game[i] == '/':
                result += get_value(game[i+1])
            elif game[i] == 'X' or game[i] == 'x':
                result += get_value(game[i+1])  # ha x-et gurított, akkor hozzáadom az eredményhez a kövi gurítást
                if game[i+2] == '/':    # ha x után a 2. gurításommal tarolok, akkor +10pont jár (-amit legutóbb adtam hozzá)
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])  # ha nem tarolok, akkor hozzáadom a második gurítást is
        last = get_value(game[i])   # last = utolsó gurítás
        if not in_first_half:   # ha a körön belül nem az 1. gurításnál tartunk, akkor a körök sorszámát növeljük eggyel
            frame += 1
        if in_first_half is True:   # ha az 1. gurításnál tartottunk, akkor ezt módosítjuk, mert ugye utána már a 2. gurítás jön
            in_first_half = False
        else:
            in_first_half = True    # ha a 2. gurításnál tartottunk, akkor ezt az 1. gurításra változtatjuk
        if game[i] == 'X' or game[i] == 'x':    # ha x-et gurítok, akkor nem lesz 2. gurításom, így a körök számát növelem eggyel
            in_first_half = True
            frame += 1
    return result


def get_value(char):
    if char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9':
        return int(char)
    elif char == 'X' or char == 'x':
        return 10
    elif char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
