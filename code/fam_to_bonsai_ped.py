filename = "/Users/dangtrang/Library/CloudStorage/OneDrive-brynmawr.edu/2022 - 2023/Spring 23/Senior Conference/endogamous-bonsai/code/toy.txt"
with open(filename, 'r') as file:
    print("{")
    for i, line in enumerate(file):
        if i == 0:
            continue
        line = line.split()

        res = "\'{0}\': [{1}, {2}, \'{3}\', \'{4}\'],".format(line[0], line[3], None, line[1], line[2])
        print(res)
    print("}")
        
"""
TOY DICT
    toy_dict1 = {
                    '1': [2, None, 'b', 'a'],
                    '2': [1, None, 'b', 'a'],
                    '3': [1, None, 'b', 'a'],
                    '4': [1, None, 'd', 'e'],
                    '5': [2, None, 'd', 'e'],
                    '6': [2, None, 'f', 'c'],
                    '7': [1, None, 'f', 'c'],
                    '8': [2, None, 'f', 'c'],
                    'a': [2, None, '0', '0'],
                    'b': [1, None, 'h', 'g'],
                    'c': [2, None, 'h', 'g'],
                    'd': [1, None, 'h', 'g'],
                    'e': [2, None, 'l', 'm'],
                    'f': [1, None, 'j', 'i'],
                    'g': [2, None, '0', '0'],
                    'h': [1, None, 'l', 'k'],
                    'i': [2, None, 'n', 'o'],
                    'j': [1, None, '0', '0'],
                    'k': [2, None, '0', '0'],
                    'l': [1, None, 'p', 'q'],
                    'm': [2, None, '0', '0'],
                    'n': [1, None, 'p', 'q'],
                    'o': [2, None, '0', '0'],
                    'p': [1, None, '0', '0'],
                    'q': [2, None, '0', '0'],
                }
"""