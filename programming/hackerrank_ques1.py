import textwrap

def wrap(string, max_width):
    a = 0
    b= max_width
    le = len(string)
    s = ''
    for i in string:
        if len(string[a: b]) == max_width:
            s += string[a: b]
            s+= "\n"
            
        elif len(string[a: b]) != max_width:
            s += string[a:le+1]
        a = a+max_width
        b += max_width
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)