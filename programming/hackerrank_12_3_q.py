colors = eval(input())

while len(colors) > 1:

  for i in range(len(colors)):
    if i == len(colors) - 1:
      break
    if colors[i] != colors[i+1]:

      third_color = "R" if colors[i] != "R" and colors[i+1] != "R" else "G" if colors[i] != "G" and colors[i+1] != "G" else "B"
      colors = colors[:i] + [third_color] + colors[i+2:]
      break


print(f'"{colors[0]}"')