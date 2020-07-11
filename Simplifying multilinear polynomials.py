# When we attended middle school were asked to simplify mathematical expressions like "3x-yx+2xy-x" (or usually bigger), and that was easy-peasy ("2x+xy"). But tell that to your pc and we'll see!
#
# Write a function: simplify, that takes a string in input, representing a multilinear non-constant polynomial in integers coefficients (like "3x-zx+2xy-x"), and returns another string as output where the same expression has been simplified in the following way ( -> means application of simplify):
#
#     All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, e.g.:
#
#     "cb+cba" -> "bc+abc", "2xy-yx" -> "xy", "-a+5ab+3a-c-2a" -> "-c+5ab"
#
#     All monomials appears in order of increasing number of variables, e.g.:
#
#     "-abc+3a+2ac" -> "3a+2ac-abc", "xyz-xz" -> "-xz+xyz"
#
#     If two monomials have the same number of variables, they appears in lexicographic order, e.g.:
#
#     "a+ca-ab" -> "a-ab+ac", "xzy+zby" ->"byz+xyz"
#
#     There is no leading + sign if the first coefficient is positive, e.g.:
#
#     "-y+x" -> "x-y", but no restrictions for -: "y-x" ->"-x+y"


def sort_letters(mononom):
	"""Get mononomial, throw away invalid symbols, sort, join, return"""
	return "".join(sorted(map(str, [i for i in str(mononom) if i.isalpha()])))


def split_polynomial(polynom):
	"""Splitting polynom to mononoms. We add leading "+" if first mononom is positive since im noob at regex """
	import re
	polynom = "+" + str(polynom) if str(polynom)[:1].isalnum() else polynom
	return re.findall("[+|-][\d]*[A-Z]*[a-z]*", polynom)


def simplify(poly):
	import re
	from collections import namedtuple
	Mono = namedtuple("mononomial", "value, multiplier")  # we use namedtuple for easier reading, not necessary though
	tmp = split_polynomial(poly)
	count = dict()  # dict for counting

	for item in tmp:
		multiplier = [i for i in item if i.isdigit()]  # we find multiplier of mononom if it exist
		if re.findall("[-]", str(item)) and len(multiplier):  # if mononom was negative and had multiplier, multiplier become negative
			multiplier = int(multiplier[0]) * -1
		elif len(multiplier):  # we have positive multiplier
			multiplier = int(multiplier[0])
		elif re.findall("[-]", str(item)):  # we have -1 multiplier
			multiplier = -1
		else:  # we have 1 multiplier
			multiplier = 1
		s_poly = sort_letters(item)  # sorting mononom so we could add/substract it later using dict
		count[s_poly] = count.get(s_poly, 0) + multiplier  # we add mononom to dict that many times as multiplier value
	mytuple = sorted(tuple(count.items()), key=lambda x: (len(x[0]), x[0]))  # sorting our former dictionary that is tuple now 2 times - mononom len then mononom alphabetical
	ntlist = []
	ret = ""
	for i in range(len(mytuple)):
		m = Mono(mytuple[i][0], mytuple[i][1])  # we put values into namedtuple list
		ntlist.append(m)
	for i in ntlist:  # all of this ↓ could be replaced with "+".join().replace("+-", "-"), but its not my solution :)
		print(i)
		if i.multiplier == 0:
			continue
		elif i.multiplier == 1:
			ret += ("+" + str(i.value))
		elif i.multiplier == -1:
			ret += ("-" + str(i.value))
		else:
			ret += ("+" + str(i.multiplier) + str(i.value)) if int(i.multiplier) > 0 else (str(i.multiplier) + str(i.value))

	ret = ret[1:] if ret[:1] == "+" else ret  # we process first symbol and remove it if its "+"
	return ret

print(simplify("-y+x"))
