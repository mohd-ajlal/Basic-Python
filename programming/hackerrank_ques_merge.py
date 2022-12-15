def merge_the_tools(string, k):
    # your code goes here
    lt = []
    s = 0
    for item in string:
        s += 1
        if item not in lt:
            lt.append(item)
        if s == k:
            print (''.join(lt))
            lt = []
            s = 0

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)