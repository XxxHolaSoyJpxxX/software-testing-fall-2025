# -*- coding: utf-8 -*-

import unittest

from tdd.password import pass_validator
'''
Kata 3 Password input field validation

Create a function that can be used as a validator for the password field of a user registration form.
 The validation function takes a string as an input and returns a validation result. The validation result 
 should contain a boolean indicating if the password is valid or not, and also a field with the possible 
 validation errors.
Requirements

1. The password must be at least 8 characters long. If it is not met, then the following error message 
should be returned: “Password must be at least 8 characters”

2. The password must contain at least 2 numbers. If it is not met, then the following error message should be 
returned: “The password must contain at least 2 numbers”

3. The validation function should handle multiple validation errors.
For example, “somepassword” should an error message: 
“Password must be at least 8 characters\nThe password must contain at least 2 numbers”

4. The password must contain at least one capital letter. If it is not met, then the following error message 
should be returned: “password must contain at least one capital letter”

5. The password must contain at least one special character. If it is not met, then the following error message 
should be returned: “password must contain at least one special character”
'''

class TestPasswordValidator(unittest.TestCase):
	'''
	Test clas for pass validator
	'''
	def test_pass_len_less_than_8(self):
		'''test when pasword lenght is less than 8'''
		self.assertEqual(pass_validator('Pas$12'),"Password must be at least 8 characters")
	def test_pass_one_number(self):
		'''test when pass has only one number'''
		self.assertEqual(pass_validator('Pas$word1'),"Password must contain at least 2 numbers")
	def test_two_error(self):
		'''test ehen are two erros'''
		self.assertEqual(pass_validator('Pas$1'),"Password must be at least 8 characters\nPassword must contain at least 2 numbers")
	def test_no_caps(self):
		'''test when are no caps'''
		self.assertEqual(pass_validator('pas$word123'),"Password must contain at least one capital letter")
	def test_spc_char(self):
		'''when is non spc char'''
		self.assertEqual(pass_validator('PassWord123'),"Password must contain at least one special character")