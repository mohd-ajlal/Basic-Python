a = int(input())

years = a // 365
week = (a - (years * 365 )) // 7
days = (a- (years * 365 + week * 7)) % 7

print(years)
print(week)
print(days)
