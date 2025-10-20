import unittest
from TDD.fizzBuzz import fizzBuzz

"""
1. Write a “fizzBuzz” method that accepts a number as input and returns it as a String.

Notes:

    start with the minimal failing solution
	    keep the three rules in mind and always write just sufficient enough code
		    do not forget to refactor your code after each passing test
			    write your assertions relating to the exact requirements

				2. For multiples of three return “Fizz” instead of the number

				3. For the multiples of five return “Buzz”

				4. For numbers that are multiples of both three and five return “FizzBuzz”.

"""


class TestFizzBuzz(unittest.TestCase):
	def test_numbers_not_multiples(self):
		self.assertEqual(fizzBuzz(1), 1)
		self.assertEqual(fizzBuzz(2), 2)
		self.assertEqual(fizzBuzz(4), 4)
		self.assertEqual(fizzBuzz(7), 7)

	def test_fizz(self):
		self.assertEqual(fizzBuzz(6), "Fizz")
		self.assertEqual(fizzBuzz(33), "Fizz")
		self.assertEqual(fizzBuzz(99), "Fizz")

	def test_buzz(self):
		self.assertEqual(fizzBuzz(5), "Buzz")
		self.assertEqual(fizzBuzz(100), "Buzz")
		self.assertEqual(fizzBuzz(65), "Buzz")

	def test_fizzbuzz(self):
		self.assertEqual(fizzBuzz(15), "FizzBuzz")
		self.assertEqual(fizzBuzz(30), "FizzBuzz")
		self.assertEqual(fizzBuzz(45), "FizzBuzz")
