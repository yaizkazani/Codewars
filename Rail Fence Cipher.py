# Create two functions to encode and then decode a string using the Rail Fence Cipher.
# This cipher is used to encode a string by placing each character successively in a diagonal along a set of "rails".
# First start off moving diagonally and down. When you reach the bottom, reverse direction and move diagonally and up until you reach the top rail.
# Continue until you reach the end of the string. Each "rail" is then read left to right to derive the encoded string.
#
# For example, the string "WEAREDISCOVEREDFLEEATONCE" could be represented in a three rail system as follows:
#
# W       E       C       R       L       T       E
#   E   R   D   S   O   E   E   F   E   A   O   C
#     A       I       V       D       E       N
#
# The encoded string would be:
#
# WECRLTEERDSOEEFEAOCAIVDEN


def matrix_filler(string, n, filler=""):
	"""  Function to build a matrix and to place string's letters into it using rail pattern"""
	row, col = 0, 0
	down = 1  # movement direction determinator
	matrix = [["%" for i in range(2 * len(string))] for j in range(n)]  # matrix creation
	for letter in string:
		matrix[row][col] = letter if not filler else filler  # if we just want to mark items that should be used for deciphering - we use filler, otherwise we put string elements to prepare for encryption
		col += 1
		row += down
		down = down * -1 if row == 0 or row == n - 1 else down  # if we're at 1st or last row - we need to invert our movement direction
	return matrix


def encode_rail_fence_cipher(string, n):
	ret = ""
	matrix = matrix_filler(string, n)  # build matrix with string's items placed in rail pattern
	for s in matrix:
		ret += "".join(s).replace("%", "")  # get row lists, make them strings, add them one by one to result
	return ret


def decode_rail_fence_cipher(string, n):
	ret = ""
	s = list(reversed(string))
	matrix = matrix_filler(string, n, "#")  # we fill matrix with symbols marking proper rail placement (since we know n), otherwise we'd just run 1 to ? n-size trying to decipher(bruteforce attack)
	for rows in range(len(matrix)):
		for columns in range(len(matrix[0])):
			if matrix[rows][columns] == "#":  # if matrix element is in proper place, we replace it with string's symbol
				tmp = s.pop()
				matrix[rows][columns] = tmp
	row, col = 0, 0
	down = 1
	for _ in range(len(string)):  # we read the matrix using given n in hope that we will decipher. Since we know n - we do decipher right away :)
		ret += matrix[row][col]
		col += 1
		row += down
		down = down * -1 if row == 0 or row == n - 1 else down
	return ret


print(encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3))
print(decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3))
