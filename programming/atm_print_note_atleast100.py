#input_section

amount = int(input("Enter amount: "))

#logical section

newam = amount-100

twot = newam // 2000
fiveh = (newam - ( twot * 2000 )) // 500
twoh = (newam - (twot * 2000 + fiveh * 500 )) // 200
hundred = ((newam - (twot * 2000 + twoh * 200 + fiveh * 500)) // 100) + 1

#Display Section

print(f"2000 notes = {twot} 500 notes = {fiveh} 200 notes = {twoh} 100 notes = {hundred}")
