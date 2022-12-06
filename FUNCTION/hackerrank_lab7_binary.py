# Python3 program to Generate all binary string
# without consecutive 1's of size K

# A utility function generate all string without
# consecutive 1'sof size K
def generateAllStringsUtil(K, str, n):
	
	# print binary string without consecutive 1's
	if (n == K):
		
		# terminate binary string
		print(*str[:n], sep = "", end = " ")
		return
	
	# if previous character is '1' then we put
	# only 0 at end of string
	# example str = "01" then new string be "000"
	if (str[n-1] == '1'):
		str[n] = '0'
		generateAllStringsUtil (K, str, n + 1)
		
	# if previous character is '0' than we put
	# both '1' and '0' at end of string
	# example str = "00" then new string "001" and "000"
	if (str[n-1] == '0'):
		str[n] = '0'
		generateAllStringsUtil(K, str, n + 1)
		str[n] = '1'
		generateAllStringsUtil(K, str, n + 1)
		
# function generate all binary string without
# consecutive 1's
def generateAllStrings(K):
	
	# Base case
	if (K <= 0):
		return
	
	# One by one stores every
	# binary string of length K
	str = [0] * K
	
	# Generate all Binary string starts with '0'
	str[0] = '0'
	generateAllStringsUtil (K, str, 1)
	
	# Generate all Binary string starts with '1'
	str[0] = '1'
	generateAllStringsUtil (K, str, 1)

# Driver code
K = int(input())
generateAllStrings (K)
