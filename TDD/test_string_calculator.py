# -*- coding: utf-8 -*-
"""Unit tests for the string_calculator function (TDD String Calculator exercise)."""

import unittest

from tdd.string_calculator import add


class TestStringCalculator(unittest.TestCase):
    """Unit tests for the string_calculator function."""

    def test_empty_string(self):
        """Test if numbres is empty"""
        self.assertEqual(add(""), 0)

    def test_one_numbrer(self):
        """Test when in string is one numbrer"""
        self.assertEqual(add("1"), 1)

    def test_two_numbers(self):
        """Test when in string are two numbers"""
        self.assertEqual(add("1,2"), 3)

    def test_unknown_number(self):
        """Test if string has a unknown number"""
        self.assertEqual(add("a"), 0)

    def test_try_other_separetors(self):
        """Test if the separetor is /n"""
        self.assertEqual(add("1,2\n3"), 6)

    def test_separator_after_separator(self):
        """Test if a comma is befor a break line ==> ,\n"""
        self.assertEqual(add("1,\n2"), 0)

    def test_separator_in_end(self):
        """Test if separator in the end raises an error"""
        with self.assertRaises(ValueError) as context:
            add("1,2,")
        self.assertIn("Invalid input: ends with a separator", str(context.exception))

    def test_unic_delimiter(self):
        """Test if the string has a custom delimiter"""
        self.assertEqual(add("//^%\n1^%2"), 3)

    def test_negative_number(self):
        """Test if the string has a negative number"""
        with self.assertRaises(ValueError) as context:
            add("1,-2,3")
        self.assertIn("Negative number(s) are not allowed: -2", str(context.exception))

    def test_multiple_negative_numbers(self):
        """Test if the string has multiple negative numbers"""
        with self.assertRaises(ValueError) as context:
            add("1,-2,3,-4")
        self.assertIn(
            "Negative number(s) are not allowed: -2 -4", str(context.exception)
        )

    def test_multiple_errors(self):
        """Test if the string has multiple errors"""
        with self.assertRaises(ValueError) as context:
            add("1,-2,\n3,-4,")
        self.assertIn("Invalid input: ends with a separator", str(context.exception))
        self.assertIn(
            "Negative number(s) are not allowed: -2 -4", str(context.exception)
        )

    def test_numbers_greater_than_1000(self):
        """Test if the string has numbers greater than 1000"""
        self.assertEqual(add("2,1001,6"), 8)
