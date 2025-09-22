# -*- coding: utf-8 -*-


"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    TrafficLight,
    VendingMachine,
    calculate_total_discount,
    check_number_status,
    divide,
    get_grade,
    is_even,
    is_triangle,
    validate_password,
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
