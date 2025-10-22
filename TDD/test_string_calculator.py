# -*- coding: utf-8 -*-
"""Unit tests for the string_calculator function (TDD String Calculator exercise)."""

import unittest
from tdd.string_calculator import string_calculator

class TestStringCalculator(unittest.TestCase):
	"""Unit tests for the string_calculator function."""
	def test_empty_string(self):
		"""Test if numbres is empty"""
		self.assertEqual(string_calculator(""),0)
	def test_one_numbrer(self):
		"""Test when in string is one numbrer"""
		self.assertEqual(string_calculator("1"),1)
	def test_two_numbers(self):
		"""Test when in string are two numbers"""
		self.assertEqual(string_calculator("1,2"),3)
