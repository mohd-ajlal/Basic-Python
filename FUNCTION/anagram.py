# Python3 program to find
# best meeting point in 2D array
NO_OF_CHARS = 256

# function to check whether two strings
# are anagram of each other
def areAnagram(str1: str, str2: str) -> bool:

	# Create two count arrays and
	# initialize all values as 0
	count = [0] * NO_OF_CHARS
	i = 0

	# For each character in input strings,
	# increment count in the corresponding
	# count array
	while i < len(str1) and i < len(str2):
		count[ord(str1[i])] += 1
		count[ord(str2[i])] -= 1
		i += 1

	# If both strings are of different length.
	# Removing this condition will make the program
	# fail for strings like "aaca" and "aca"
	if len(str1) != len(str2):
		return False

	# See if there is any non-zero value
	# in count array
	for i in range(NO_OF_CHARS):
		if count[i]:
			return False
		return True

# This function prints all anagram pairs
# in a given array of strings
def findAllAnagrams(arr: list, n: int):
	for i in range(n):
		for j in range(i + 1, n):
			if areAnagram(arr[i], arr[j]):
				print(arr[i], "is anagram of", arr[j])

# Driver Code
if __name__ == "__main__":

	arr = ["geeksquiz", "geeksforgeeks",
		"abcd", "forgeeksgeeks", "zuiqkeegs"]
	n = len(arr)
	findAllAnagrams(arr, n)


