# -*- coding: utf-8 -*-
"""the string_calculator function"""

import re

def string_calculator(numbers):
	"""Calculates the sum of numbers in a string."""
	if not numbers or numbers == "":
		return 0
	numbers_list = re.split(',', numbers)
	total = 0
	for num in numbers_list:
		total += int(num)
	return total