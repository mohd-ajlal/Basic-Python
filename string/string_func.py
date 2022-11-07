story = "once upon a time there was a boy"

# to find the length of a string]
a = len(story)
print(f"The length of a story is {a}")


# when the string ends with the given text.
print(story.endswith("boy"))

# to count any alphabet or text in given string.
b = story.count("a")
print(f"No. of alphabet a in given story is {b}")

# tp capitalize teh first letter of the given string

cap = story.capitalize()
print(cap)

# to find any text or alphabet in given string
# if there is more than one finded text then it will print the first letter.
find = story.find("a")
print(find)


# replace
# use to replace the given text by the given text.
# it will replace all the text.

s = story.replace("a", "b")
print(s)

# escape sequence characters
# sequence of characters after /
# escape sequence characters compares of more than one character but represent one character when used within the string
# Some sequence characters are /n -> Used for new line, 
# /t  -> use to give one tab space
# / -> Single quotes
# // -> Backslash

