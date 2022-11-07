#input section

a = int(input("Enter No of days: "))

#Logic Section

years = a // 365
month = (a - ( years * 365 )) // 30
week = (a - (years * 365 + month * 30 )) // 7
days = (a- (years * 365 + month * 30 + week * 7)) % 7

#Output Section

print(f"Years = {years} Month = {month} Week = {week} Days = {days}")