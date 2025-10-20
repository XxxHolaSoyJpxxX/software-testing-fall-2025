# -*- coding: utf-8 -*-

"""Module for testing FizzBuzz functionality."""


def fizz_buzz(n):
    """Devuelve 'Fizz', 'Buzz' o 'FizzBuzz' según el valor de n."""
    var = ""
    if n % 3 == 0:
        var.join("fizz")
    if n % 5 == 0:
        var.join("buzz")
    return var
