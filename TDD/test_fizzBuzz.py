# -*- coding: utf-8 -*-
"""Unit tests for the fizz_buzz function (TDD FizzBuzz exercise)."""

import unittest

from tdd.fizzbuzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    """Unit tests for the fizz_buzz function."""

    def test_numbers_not_multiples(self):
        """Test numbers that are not multiples of 3 or 5."""
        self.assertEqual(fizz_buzz(1), 1)
        self.assertEqual(fizz_buzz(2), 2)
        self.assertEqual(fizz_buzz(4), 4)
        self.assertEqual(fizz_buzz(7), 7)

    def test_fizz(self):
        """Test multiples of 3."""
        self.assertEqual(fizz_buzz(6), "fizz")
        self.assertEqual(fizz_buzz(33), "fizz")
        self.assertEqual(fizz_buzz(99), "fizz")

    def test_buzz(self):
        """Test multiples of 5."""
        self.assertEqual(fizz_buzz(5), "buzz")
        self.assertEqual(fizz_buzz(100), "buzz")
        self.assertEqual(fizz_buzz(65), "buzz")

    def test_fizzbuzz(self):
        """Test multiples of both 3 and 5."""
        self.assertEqual(fizz_buzz(30), "fizzbuzz")
        self.assertEqual(fizz_buzz(15), "fizzbuzz")
        self.assertEqual(fizz_buzz(45), "fizzbuzz")
