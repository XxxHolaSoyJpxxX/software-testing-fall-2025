# -*- coding: utf-8 -*-


"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    TrafficLight,
    VendingMachine,
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_number_status,
    divide,
    get_grade,
    is_even,
    is_triangle,
    validate_email,
    validate_login,
    validate_password,
    verify_age,
)


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_is_even_with_even_number(self):
        """
        Checks if a number is even.
        """
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """
        Checks if a number is not even.
        """
        self.assertFalse(is_even(7))

    def test_divide_by_non_zero(self):
        """
        Checks the divide function works as expected.
        """
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        Checks the divide function returns 0 when dividing by 0.
        """
        self.assertEqual(divide(10, 0), 0)

    def test_get_grade_a(self):
        """
        Checks A grade.
        """
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """
        Checks B grade.
        """
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """
        Checks C grade.
        """
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """
        Checks F grade.
        """
        self.assertEqual(get_grade(65), "F")

    def test_is_triangle_yes(self):
        """
        Checks the three inputs can form a triangle.
        """
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """
        Checks the three inputs can't form a triangle when C is greater or equal than A + B.
        """
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """
        Checks the three inputs can't form a triangle when B is greater or equal than A + C.
        """
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """
        Checks the three inputs can't form a triangle when A is greater or equal than B + C.
        """
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")


class TestWhiteBoxFrom1To3(unittest.TestCase):
    """
    White-box unittest class from 1 to 3.
    """

    def test_is_num_status_positive(self):
        """
        Checks the number status function returns 'Positive' for positive input.
        """
        self.assertEqual(check_number_status(1), "Positive")

    def test_is_num_status_negative(self):
        """
        Checks the number status function returns 'Negative' for negative input.
        """
        self.assertEqual(check_number_status(-1), "Negative")

    def test_is_num_status_zero(self):
        """
        Checks the number status function returns 'Zero' for zero input.
        """
        self.assertEqual(check_number_status(0), "Zero")

    def test_password_length_lower_than_8(self):
        """
        Checks password validation fails if it's shorter than 8 characters.
        """
        self.assertFalse(validate_password("Ab1!"))

    def test_password_missing_upper_case(self):
        """
        Checks password validation fails if it has no uppercase letters.
        """
        self.assertFalse(validate_password("abcdefg1!"))

    def test_password_missing_lower_case(self):
        """
        Checks password validation fails if it has no lowercase letters.
        """
        self.assertFalse(validate_password("ABCDEFG1!"))

    def test_password_missing_digit(self):
        """
        Checks password validation fails if it has no digits.
        """
        self.assertFalse(validate_password("Abcdefghi!"))

    def test_password_missing_special_char(self):
        """
        Checks password validation fails if it has no special characters.
        """
        self.assertFalse(validate_password("Abcdefghi1"))

    def test_password_valid(self):
        """
        Checks password validation passes with a valid password.
        """
        self.assertTrue(validate_password("Abcd1234!"))

    def test_calculate_total_discount_no_discount(self):
        """
        Checks total discount is 0 when price < 100.
        """
        self.assertEqual(calculate_total_discount(50), 0)

    def test_calculate_total_discount_10_percent(self):
        """
        Checks total discount is 10% when 100 <= price < 500.
        """
        self.assertEqual(calculate_total_discount(150), 15)

    def test_calculate_total_discount_20_percent(self):
        """
        Checks total discount is 20% when price >= 500.
        """
        self.assertEqual(calculate_total_discount(600), 120)


class TestWhiteBoxFrom4To6(unittest.TestCase):
    """
    White-box unittest class from 4 to 6.
    """

    def test_calculate_order_total_no_discount(self):
        """
        Checks order total without discounts (quantity <= 5).
        """
        items = [{"quantity": 2, "price": 10}]
        self.assertEqual(calculate_order_total(items), 20)

    def test_calculate_order_total_5_percent_discount(self):
        """
        Checks order total with 5% discount (quantity 6–10).
        """
        items = [{"quantity": 6, "price": 10}]
        self.assertEqual(calculate_order_total(items), 57)

    def test_calculate_order_total_10_percent_discount(self):
        """
        Checks order total with 10% discount (quantity > 10).
        """
        items = [{"quantity": 11, "price": 10}]
        self.assertEqual(calculate_order_total(items), 99)

    def test_calculate_order_total_multiple_items(self):
        """
        Checks order total with multiple items and mixed discounts.
        """
        items = [
            {"quantity": 3, "price": 10},
            {"quantity": 8, "price": 5},
            {"quantity": 12, "price": 2},
        ]
        expected = (3 * 10) + (0.95 * 8 * 5) + (0.9 * 12 * 2)
        self.assertEqual(calculate_order_total(items), expected)

    def test_shipping_standard_low_weight(self):
        """
        Checks standard shipping cost when weight <= 5.
        """
        items = [{"weight": 2}, {"weight": 3}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_shipping_standard_mid_weight(self):
        """
        Checks standard shipping cost when 5 < weight <= 10.
        """
        items = [{"weight": 6}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_shipping_standard_high_weight(self):
        """
        Checks standard shipping cost when weight > 10.
        """
        items = [{"weight": 12}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_shipping_express_low_weight(self):
        """
        Checks express shipping cost when weight <= 5.
        """
        items = [{"weight": 4}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_shipping_express_mid_weight(self):
        """
        Checks express shipping cost when 5 < weight <= 10.
        """
        items = [{"weight": 7}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_shipping_express_high_weight(self):
        """
        Checks express shipping cost when weight > 10.
        """
        items = [{"weight": 15}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_shipping_invalid_method(self):
        """
        Checks invalid shipping method raises ValueError.
        """
        items = [{"weight": 5}]
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost(items, "fast")

    def test_validate_login_successful(self):
        """
        Checks login is successful with valid username and password.
        """
        self.assertEqual(validate_login("validUser", "strongPass1"), "Login Successful")

    def test_validate_login_short_username(self):
        """
        Checks login fails with username shorter than 5 characters.
        """
        self.assertEqual(validate_login("usr", "strongPass1"), "Login Failed")

    def test_validate_login_long_username(self):
        """
        Checks login fails with username longer than 20 characters.
        """
        self.assertEqual(validate_login("u" * 21, "strongPass1"), "Login Failed")

    def test_validate_login_short_password(self):
        """
        Checks login fails with password shorter than 8 characters.
        """
        self.assertEqual(validate_login("validUser", "short"), "Login Failed")

    def test_validate_login_long_password(self):
        """
        Checks login fails with password longer than 15 characters.
        """
        self.assertEqual(validate_login("validUser", "p" * 16), "Login Failed")


class TestWhiteBoxFrom7To10(unittest.TestCase):
    """
    White-box unittest class from 7 to 10.
    """

    def test_verify_age_lower_bound(self):
        """
        Checks eligibility at age 18 (lower bound).
        """
        self.assertEqual(verify_age(18), "Eligible")

    def test_verify_age_upper_bound(self):
        """
        Checks eligibility at age 65 (upper bound).
        """
        self.assertEqual(verify_age(65), "Eligible")

    def test_verify_age_below_limit(self):
        """
        Checks not eligible when age < 18.
        """
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_verify_age_above_limit(self):
        """
        Checks not eligible when age > 65.
        """
        self.assertEqual(verify_age(70), "Not Eligible")

    def test_categorize_product_category_a(self):
        """
        Checks product price is in Category A.
        """
        self.assertEqual(categorize_product(30), "Category A")

    def test_categorize_product_category_b(self):
        """
        Checks product price is in Category B.
        """
        self.assertEqual(categorize_product(80), "Category B")

    def test_categorize_product_category_c(self):
        """
        Checks product price is in Category C.
        """
        self.assertEqual(categorize_product(150), "Category C")

    def test_categorize_product_category_d_low(self):
        """
        Checks product price below 10 is Category D.
        """
        self.assertEqual(categorize_product(5), "Category D")

    def test_categorize_product_category_d_high(self):
        """
        Checks product price above 200 is Category D.
        """
        self.assertEqual(categorize_product(300), "Category D")

    def test_validate_email_valid(self):
        """
        Checks valid email passes validation.
        """
        self.assertEqual(validate_email("user@example.com"), "Valid Email")

    def test_validate_email_missing_at(self):
        """
        Checks email without '@' is invalid.
        """
        self.assertEqual(validate_email("userexample.com"), "Invalid Email")

    def test_validate_email_missing_dot(self):
        """
        Checks email without '.' is invalid.
        """
        self.assertEqual(validate_email("user@examplecom"), "Invalid Email")

    def test_validate_email_too_short(self):
        """
        Checks email shorter than 5 characters is invalid.
        """
        self.assertEqual(validate_email("a@b"), "Invalid Email")

    def test_validate_email_too_long(self):
        """
        Checks email longer than 50 characters is invalid.
        """
        long_email = "u" * 45 + "@test.com"
        self.assertEqual(validate_email(long_email), "Invalid Email")

    def test_celsius_to_fahrenheit_zero(self):
        """
        Checks conversion of 0 Celsius to Fahrenheit.
        """
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_celsius_to_fahrenheit_positive(self):
        """
        Checks conversion of 100 Celsius to Fahrenheit.
        """
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_celsius_to_fahrenheit_negative(self):
        """
        Checks conversion of -40 Celsius to Fahrenheit.
        """
        self.assertEqual(celsius_to_fahrenheit(-40), -40)

    def test_celsius_to_fahrenheit_below_range(self):
        """
        Checks temperature below -100 returns invalid.
        """
        self.assertEqual(celsius_to_fahrenheit(-150), "Invalid Temperature")

    def test_celsius_to_fahrenheit_above_range(self):
        """
        Checks temperature above 100 returns invalid.
        """
        self.assertEqual(celsius_to_fahrenheit(150), "Invalid Temperature")


class TestWhiteBoxVendingMachine(unittest.TestCase):
    """
    Vending Machine unit tests.
    """

    def setUp(self):
        """
        Sets up a vending machine instance before each test.
        """
        self.vending_machine = VendingMachine()
        self.assertEqual(self.vending_machine.state, "Ready")

    def test_vending_machine_insert_coin_error(self):
        """
        Checks the vending machine rejects coins when in 'Dispensing' state.
        """
        self.vending_machine.state = "Dispensing"

        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Invalid operation in current state.")

    def test_vending_machine_insert_coin_success(self):
        """
        Checks the vending machine accepts coins when in 'Ready' state.
        """
        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Coin Inserted. Select your drink.")


class TestTrafficLight(unittest.TestCase):
    """
    Traffic Light unit tests.
    """

    def setUp(self):
        """
        Sets up a traffic light instance before each test.
        """
        self.traffic_light = TrafficLight()
        self.assertEqual(self.traffic_light.state, "Red")

    def test_traffic_light_change_from_red(self):
        """
        Checks transition from Red to Green.
        """
        self.traffic_light.change_state()
        output = self.traffic_light.get_current_state()

        self.assertEqual(self.traffic_light.state, "Green")
        self.assertEqual(output, "Green")

    def test_traffic_light_change_from_green(self):
        """
        Checks transition from Green to Yellow.
        """
        self.traffic_light.state = "Green"

        self.traffic_light.change_state()
        output = self.traffic_light.get_current_state()

        self.assertEqual(self.traffic_light.state, "Yellow")
        self.assertEqual(output, "Yellow")

    def test_traffic_light_change_from_yellow(self):
        """
        Checks transition from Yellow to Red.
        """
        self.traffic_light.state = "Yellow"

        self.traffic_light.change_state()
        output = self.traffic_light.get_current_state()

        self.assertEqual(self.traffic_light.state, "Red")
        self.assertEqual(output, "Red")

    def test_traffic_light_invalid_change_ry(self):
        """
        Ensures transition from Red skips Yellow directly.
        """
        self.traffic_light.state = "Red"
        self.traffic_light.change_state()
        output = self.traffic_light.get_current_state()

        self.assertNotEqual(self.traffic_light.state, "Yellow")
        self.assertNotEqual(output, "Yellow")

    def test_traffic_light_invalid_change_gr(self):
        """
        Ensures transition from Green skips Red directly.
        """
        self.traffic_light.state = "Green"
        self.traffic_light.change_state()
        output = self.traffic_light.get_current_state()

        self.assertNotEqual(self.traffic_light.state, "Red")
        self.assertNotEqual(output, "Red")

    def test_traffic_light_invalid_change_yg(self):
        """
        Ensures transition from Yellow skips Green directly.
        """
        self.traffic_light.state = "Yellow"
        self.traffic_light.change_state()
        output = self.traffic_light.get_current_state()

        self.assertNotEqual(self.traffic_light.state, "Green")
        self.assertNotEqual(output, "Green")
