def score(game):
    '''
    This function counts the score.
    '''
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
        else:
            result += get_value(game[i])
        if frame < 10  and get_value(game[i]) == 10:
            result = check_spare_or_strike(game, result, i)
        last = get_value(game[i])
        if not in_first_half:
            frame += 1
        if in_first_half is True:
            in_first_half = False
        else:
            in_first_half = True
        if game[i] == 'X' or game[i] == 'x':
            in_first_half = True
            frame += 1
    return result


def check_spare_or_strike(game, result, i):
    '''
    This function checks that tha last roll was spare/strike or not.
    If you rolled /, it adds your roll to the score.
    If you rolled X, it adds your roll to the score.
        If you rolled X and the next roll is /, than it adds 10 points to the score and substracts the previous roll, else it gives your roll to the score.
    '''
    if game[i] == '/':
        result += get_value(game[i+1])
    elif game[i] == 'X' or game[i] == 'x':
        result += get_value(game[i+1])
        if game[i+2] == '/':
            result += 10 - get_value(game[i+1])
        else:
            result += get_value(game[i+2])
    return result


def get_value(char):
    '''
    This function checks the inputs.
    '''
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
