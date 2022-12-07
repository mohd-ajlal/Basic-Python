def split_and_join(line):
    lt = line.split(" ")
    for i in lt:
        a = "-".join(lt)
    return a
        

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)