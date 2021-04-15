import re

no_match = 0
regex, _string = input().split("|")
list_regex, list_string = [i for i in regex], [x for x in _string]

if '\\' in list_regex and '?' in list_regex:
    if list_regex[1] == '?':
        print('True')
    else:
        match = re.match(regex, _string)
        if match is not None:
            print('True')
        else:
            print('False')

elif '+' in list_regex:
    match = re.match(regex, _string)
    if match is not None:
        print('True')
    else:
        print('False')

elif '*' in list_regex:
    match = re.match(regex, _string)
    if match is not None:
        print('True')
    else:
        print('False')

elif '?' in list_regex:
    match = re.match(regex, _string)
    if match is not None:
        print('True')
    else:
        print('False')

elif '^' in list_regex and '$' in list_regex and ' ' in list_string:
    if ' ' not in list_string:
        match = re.match(list_regex[1], list_string[0])
        if match is not None:
            print('True')
        else:
            print('False')
    else:
        print('False')

elif '^' in list_regex:
    match = re.match(list_regex[1], list_string[0])
    if match is not None:
        print('True')
    else:
        print('False')

elif '$' in list_regex:
    match = re.match(list_regex[-2], list_string[-1])
    if match is not None:
        print('True')
    else:
        print('False')

else:
    if len(list_regex) == len(list_string):
        try:
            for t in range(len(list_regex)):
                match = re.match(list_regex[t], list_string[t])
                if match is None:
                    no_match += 1
                else:
                    no_match += 0
            if no_match == 0:
                print('True')
            else:
                print('False')
        except IndexError:
            print('False')
    else:
        if len(_string) == 0:
            print('False')
        else:
            if regex in _string or regex == '.' or '\\':
                print('True')
            else:
                print('False')
