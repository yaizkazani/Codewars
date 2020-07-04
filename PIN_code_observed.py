# ┌───┬───┬───┐
# │ 1 │ 2 │ 3 │
# ├───┼───┼───┤
# │ 4 │ 5 │ 6 │
# ├───┼───┼───┤
# │ 7 │ 8 │ 9 │
# └───┼───┼───┘
#     │ 0 │
#     └───┘
# He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.
#
# He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.
#
# * possible in sense of: the observed PIN itself and all variations considering the adjacent digits
#
# Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list in Java and C#) of all variations for an observed PIN with a length of 1 to 8 digits. We could name the function getPINs (get_pins in python, GetPINs in C#). But please note that all PINs, the observed one and also the results, must be strings, because of potentially leading '0's. We already prepared some test cases for you.


def get_pins(observed):
	import itertools
	myset = set()
	f = []
	numpad = [[1, 2, 3],
	          [4, 5, 6],
	          [7, 8, 9],
	          ["*", 11, "*"]
	          ]
	for o in observed:
		s = suggestion(int(o), numpad)
		f.append([s])
		for _ in s:
			myset.add(_)
	result = []
	for pin in list(map("".join, itertools.product(myset, repeat=len(observed)))):  # generate tuples with ALL possible combination
		if pin_sequence_checker(pin, f):  # filter them so like possibilities for 3rd key wont be allowed for 1st press key.
			result.append(pin)
	return result


def pin_sequence_checker(pin, f):
	"""We get pin and filter list,
	function checks if all pin digits are in corresponding sublist.
	 i.e. pin = 123, list = [[123], [456], [789]] ==> False
	 pin = 147, list = [[123], [456], [789]] ==> True"""
	return all([d in "".join(f[i]) for ix, d in enumerate(pin) for i in range(len(f)) if ix == i])


def suggestion(number, numpad):
	""" we get number + 2d numpad list and return all possible adjacent numpad keys"""
	number = 11 if number == 0 else number  # 0 doesnt fit our logic so we have to replace it :)
	ret = []
	row = 0
	for now in range(len(numpad)):  # find row of current number
		if number in numpad[now]:
			row = now
			break
	if number + 1 in numpad[row]:  # we check if adjacent in the same row exist (+1 , -1)
		ret.append(number + 1)
	if number - 1 in numpad[row]:
		ret.append(number - 1)
	if row + 1 < len(numpad) and number + 3 in numpad[row + 1]: # we check if adjacent in top/bottom row exist (+3, -3)
		ret.append(number + 3)
	if row - 1 >= 0 and number - 3 in numpad[row - 1]:
		ret.append(number - 3)
	ret.append(number)
	return "".join(map(str, ret)).replace("11", "0")  # need to change 11 and 0 again :)


print(get_pins("0"))
