import re

def execute(s):
    r = ''
    while len(s) > 0:
        s0 = s[0]
        match = re.search('^{}+'.format(s0), s)
        r += s0 + str(match.span()[1])
        s = s[match.span()[1]:]
    return r


if __name__ == '__main__':
    print(execute(input()))
