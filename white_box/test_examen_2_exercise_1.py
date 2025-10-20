# -*- coding: utf-8 -*-
import os
import unittest
from unittest import mock
from unittest.mock import patch

from white_box.examen_2_exercise_1 import (
    generate_salt,
    generate_password_hash,
    load_user_data,
    save_user_data,    
    register,
    login,
    main,
)

class TestUserAuth(unittest.TestCase):
    """Unit tests for user authentication system."""

    def setUp(self):
        """Set up test environment."""
        if os.path.exists("users.json"):
            os.remove("users.json")


    def test_generate_salt(self):
        """Test salt generation."""
        salt1 = generate_salt()
        salt2 = generate_salt()
        self.assertEqual(len(salt1), 32)
        self.assertEqual(len(salt2), 32)
        self.assertNotEqual(salt1, salt2)
    
    def test_generate_password_hash(self):
        """Test password hashing."""
        password = "securepassword"
        salt = generate_salt()
        hash1 = generate_password_hash(password, salt)
        hash2 = generate_password_hash(password, salt)
        self.assertEqual(hash1, hash2)
    
    def test_generate_password_hash_different_salts(self):
        """Test password hashing with different salts."""
        password = "securepassword"
        salt1 = generate_salt()
        salt2 = generate_salt()
        hash1 = generate_password_hash(password, salt1)
        hash2 = generate_password_hash(password, salt2)
        self.assertNotEqual(hash1, hash2)


    def test_load_and_save_user_data(self):
        """Test loading and saving user data."""
        data = {'user1': {'password_hash': 'hash1', 'salt': 'salt1'}}
        save_user_data(data)
        loaded_data = load_user_data()
        self.assertEqual(data, loaded_data)


    @patch("builtins.print")
    @patch("builtins.input", return_value="testpass")
    def test_register_new_user(self, mock_input, mock_print):
        """Test registering a new user."""
        register("testuser")
        user_data = load_user_data()
        self.assertIn("testuser", user_data)
        mock_print.assert_any_call("User registered successfully.")

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["pass1", "pass2"])
    def test_register_existing_user(self, mock_input, mock_print):
        """Test registering an existing user."""
        register("testuser") 
        register("testuser") 
        user_data = load_user_data()
        self.assertIn("testuser", user_data)
        mock_print.assert_any_call("User already exists. Please choose a different username.")


    @patch("builtins.print")
    @patch("builtins.input", return_value="testpass")
    def test_login_correct_password(self, mock_input, mock_print):
        """Test logging in with correct password."""
        register("testuser")
        login("testuser", "testpass")
        mock_print.assert_any_call("Login successful!")

    @patch("builtins.print")
    @patch("builtins.input", return_value="testpass")
    def test_login_wrong_password(self, mock_input, mock_print):
        """Test logging in with wrong password."""
        register("testuser")
        login("testuser", "wrongpass")
        mock_print.assert_any_call("Invalid password. Please try again.")

    @patch("builtins.print")
    def test_login_nonexistent_user(self, mock_print):
        """Test logging in with a non-existent user."""
        login("nonexistent", "nopass")
        mock_print.assert_any_call("User does not exist. Please register first.")
        
    @patch("builtins.print")
    @patch("builtins.input", side_effect=[
        "1", "testuser", "testpass", 
        "2", "testuser", "testpass",  
        "2", "testuser", "wrongpass", 
        "3"                            
    ])
    def test_main_flow(self, mock_input, mock_print):
        """Test main application flow."""
        main()
        mock_print.assert_any_call("User registered successfully.")
        mock_print.assert_any_call("Login successful!")
        mock_print.assert_any_call("Invalid password. Please try again.")
        mock_print.assert_any_call("Exiting...")

    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists("users.json"):
            os.remove("users.json")

