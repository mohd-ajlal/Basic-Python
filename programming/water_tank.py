# Given a water tank (cylindrical shape) with height = 10 and radius = 5. Consider a water pump having a flow rate of 15 m/min . 
#  WAP in python to find whether it is underflow ir ovwerflow 
pie = 3.14
r = int(input("Enter radius of water tank: "))
h = int(input("Enter height of water tank: "))
f = int(input("Enter flow rate of water:"))
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