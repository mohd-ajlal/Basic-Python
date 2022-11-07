pie = 3.14
r = 5
h = 10
f = 15
t = int(input("Enter the time: "))
vol = pie * (r**2) * h

vwater = f * t

if vwater<vol:
    print("Underflow")
    ht = vwater / (3.14 * r ** 2) 
    hr = h - ht
    print(f"Filled height {ht}")
    print(f"Remaining height {hr}")
elif vwater>vol:
    print("Overflow")
    print("Volume of", vwater-vol)
else:
    print("Full")