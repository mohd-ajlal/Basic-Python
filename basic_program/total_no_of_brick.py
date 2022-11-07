blen  = eval(input("Enter brick len: "))
bbre  = eval(input("Enter brick breadth: "))
bhei  = eval(input("Enter brick height: "))
wlen  = eval(input("Enter wall len: "))
wbri  = eval(input("Enter wall breadth: "))
whei  = eval(input("Enter wall height: "))

volbr = blen *bbre * bhei 

volw = wlen * wbri * whei

no_of_bricks = volw / volbr

print(f"Total number of bricks is {no_of_bricks}")