# -*- coding: utf-8 -*-


"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    DocumentEditingSystem,
    ElevatorSystem,
    TrafficLight,
    UserAuthentication,
    VendingMachine,
    authenticate_user,
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_quantity_discount,
    calculate_shipping_cost,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_file_size,
    check_flight_eligibility,
    check_loan_eligibility,
    check_number_status,
    divide,
    get_grade,
    get_weather_advisory,
    grade_quiz,
    is_even,
    is_triangle,
    validate_credit_card,
    validate_date,
    validate_email,
    validate_login,
    validate_password,
    validate_url,
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
        self.assertAlmostEqual(calculate_order_total(items), 57, places=2)

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


class TestFrom11To14(unittest.TestCase):
    """
    Tests functions 11 to 14 (credit card, date, flight eligibility, URL validation).
    """

    def test_validate_credit_card_min_length(self):
        """Valid credit card with minimum length."""
        self.assertEqual(validate_credit_card("1" * 13), "Valid Card")

    def test_validate_credit_card_max_length(self):
        """Valid credit card with maximum length."""
        self.assertEqual(validate_credit_card("2" * 16), "Valid Card")

    def test_validate_credit_card_too_short(self):
        """Credit card shorter than 13 digits is invalid."""
        self.assertEqual(validate_credit_card("1234567890"), "Invalid Card")

    def test_validate_credit_card_non_digit(self):
        """Credit card with non-digit characters is invalid."""
        self.assertEqual(validate_credit_card("1234abcd5678"), "Invalid Card")

    def test_validate_date_valid_mid(self):
        """Valid date in middle range."""
        self.assertEqual(validate_date(2000, 6, 15), "Valid Date")

    def test_validate_date_year_too_low(self):
        """Year below 1900 is invalid."""
        self.assertEqual(validate_date(1800, 6, 15), "Invalid Date")

    def test_validate_date_month_invalid(self):
        """Month outside 1-12 is invalid."""
        self.assertEqual(validate_date(2000, 13, 1), "Invalid Date")

    def test_validate_date_day_invalid(self):
        """Day outside valid range is invalid."""
        self.assertEqual(validate_date(2000, 12, 32), "Invalid Date")

    def test_check_flight_eligibility_age_in_range(self):
        """Passenger within eligible age range can book."""
        self.assertEqual(check_flight_eligibility(30, False), "Eligible to Book")

    def test_check_flight_eligibility_age_too_young_but_ff(self):
        """Underage but frequent flyer can book."""
        self.assertEqual(check_flight_eligibility(16, True), "Eligible to Book")

    def test_check_flight_eligibility_not_eligible(self):
        """Passenger underage and not frequent flyer cannot book."""
        self.assertEqual(check_flight_eligibility(17, False), "Not Eligible to Book")

    def test_check_flight_eligibility_age_upper_bound(self):
        """Passenger at upper age limit can book."""
        self.assertEqual(check_flight_eligibility(65, False), "Eligible to Book")

    def test_validate_url_http(self):
        """Valid HTTP URL."""
        self.assertEqual(validate_url("http://example.com"), "Valid URL")

    def test_validate_url_https(self):
        """Valid HTTPS URL."""
        self.assertEqual(validate_url("https://example.com"), "Valid URL")

    def test_validate_url_invalid_scheme(self):
        """URL with unsupported scheme is invalid."""
        self.assertEqual(validate_url("ftp://example.com"), "Invalid URL")

    def test_validate_url_long_https_but_over_length(self):
        """Test documenting current behavior of long HTTPS URL."""
        long_https = "https://" + "a" * 300
        self.assertEqual(validate_url(long_https), "Valid URL")


class TestFrom15To17(unittest.TestCase):
    """
    Tests functions 15 to 17 (quantity discount, file size, loan eligibility).
    """

    def test_calculate_quantity_discount_no_discount(self):
        """No discount for quantities <= 5."""
        self.assertEqual(calculate_quantity_discount(1), "No Discount")
        self.assertEqual(calculate_quantity_discount(5), "No Discount")

    def test_calculate_quantity_discount_5_percent(self):
        """5% discount for quantities 6–10."""
        self.assertEqual(calculate_quantity_discount(6), "5% Discount")
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")

    def test_calculate_quantity_discount_10_percent(self):
        """10% discount for quantities > 10."""
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")
        self.assertEqual(calculate_quantity_discount(100), "10% Discount")

    def test_check_file_size_zero(self):
        """File size of 0 is valid."""
        self.assertEqual(check_file_size(0), "Valid File Size")

    def test_check_file_size_one_mb(self):
        """File size of 1MB is valid."""
        self.assertEqual(check_file_size(1048576), "Valid File Size")

    def test_check_file_size_negative(self):
        """Negative file size is invalid."""
        self.assertEqual(check_file_size(-1), "Invalid File Size")

    def test_check_file_size_above_one_mb(self):
        """File size above 1MB is invalid."""
        self.assertEqual(check_file_size(1048577), "Invalid File Size")

    def test_check_loan_eligibility_not_eligible_low_income(self):
        """Loan not eligible for low income and poor credit."""
        self.assertEqual(check_loan_eligibility(20000, 800), "Not Eligible")

    def test_check_loan_eligibility_standard_loan_mid_income_high_score(self):
        """Eligible for standard loan."""
        self.assertEqual(check_loan_eligibility(40000, 710), "Standard Loan")

    def test_check_loan_eligibility_secured_low_score(self):
        """Eligible for secured loan."""
        self.assertEqual(check_loan_eligibility(40000, 650), "Secured Loan")

    def test_check_loan_eligibility_premium_high_income_high_score(self):
        """Eligible for premium loan."""
        self.assertEqual(check_loan_eligibility(80000, 760), "Premium Loan")

    def test_check_loan_eligibility_mid_income_low_score(self):
        """Income > 60000 but credit score <= 750 results in standard loan."""
        self.assertEqual(check_loan_eligibility(70000, 740), "Standard Loan")


class TestFrom18To21(unittest.TestCase):
    """Tests for functions 18 to 21."""

    # 18 calculate_shipping_cost
    def test_calculate_shipping_cost_small_box(self):
        """Shipping cost for small box."""
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)

    def test_calculate_shipping_cost_mid_box(self):
        """Shipping cost for medium box."""
        self.assertEqual(calculate_shipping_cost(3, 20, 20, 20), 10)

    def test_calculate_shipping_cost_large_box(self):
        """Shipping cost for large box."""
        self.assertEqual(calculate_shipping_cost(6, 40, 40, 40), 20)

    def test_calculate_shipping_cost_weight_edge(self):
        """Shipping cost for weight at lower boundary."""
        self.assertEqual(calculate_shipping_cost(1, 9, 9, 9), 5)

    # 19 grade_quiz
    def test_grade_quiz_pass(self):
        """Quiz grade passes."""
        self.assertEqual(grade_quiz(7, 2), "Pass")
        self.assertEqual(grade_quiz(10, 0), "Pass")

    def test_grade_quiz_conditional_pass(self):
        """Quiz grade conditional pass."""
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")
        self.assertEqual(grade_quiz(6, 3), "Conditional Pass")

    def test_grade_quiz_fail(self):
        """Quiz grade fails."""
        self.assertEqual(grade_quiz(4, 4), "Fail")
        self.assertEqual(grade_quiz(5, 4), "Fail")

    # 20 authenticate_user
    def test_authenticate_user_admin(self):
        """Admin login successful."""
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_authenticate_user_regular_user(self):
        """Regular user login successful."""
        self.assertEqual(authenticate_user("juanp", "password1"), "User")

    def test_authenticate_user_invalid(self):
        """Invalid login fails."""
        self.assertEqual(authenticate_user("usr", "pwd"), "Invalid")

    # 21 get_weather_advisory
    def test_get_weather_advisory_high_temp_humidity(self):
        """Advisory for high temp & humidity."""
        self.assertEqual(
            get_weather_advisory(32, 75),
            "High Temperature and Humidity. Stay Hydrated.",
        )

    def test_get_weather_advisory_low_temp(self):
        """Advisory for low temperature."""
        self.assertEqual(get_weather_advisory(-5, 30), "Low Temperature. Bundle Up!")

    def test_get_weather_advisory_none(self):
        """No specific advisory."""
        self.assertEqual(get_weather_advisory(20, 50), "No Specific Advisory")


class TestFrom22To26Classes(unittest.TestCase):
    """Tests for classes 22 to 26 (state machines and systems)."""

    # 24 UserAuthentication
    def test_user_authentication_login_logout(self):
        """Login and logout transitions."""
        ua = UserAuthentication()
        self.assertEqual(ua.state, "Logged Out")
        login_msg = ua.login()
        self.assertEqual(login_msg, "Login successful")
        self.assertEqual(ua.state, "Logged In")
        logout_msg = ua.logout()
        self.assertEqual(logout_msg, "Logout successful")
        self.assertEqual(ua.state, "Logged Out")

    def test_user_authentication_invalid_ops(self):
        """Invalid operations in user auth system."""
        ua = UserAuthentication()
        self.assertEqual(ua.logout(), "Invalid operation in current state")
        ua.login()
        self.assertEqual(ua.login(), "Invalid operation in current state")

    # 25 DocumentEditingSystem
    def test_document_editing_save_and_resume(self):
        """Save and resume document editing."""
        doc = DocumentEditingSystem()
        self.assertEqual(doc.state, "Editing")
        save_msg = doc.save_document()
        self.assertEqual(save_msg, "Document saved successfully")
        self.assertEqual(doc.state, "Saved")
        resume_msg = doc.edit_document()
        self.assertEqual(resume_msg, "Editing resumed")
        self.assertEqual(doc.state, "Editing")

    def test_document_editing_invalid(self):
        """Invalid operations in document editing."""
        doc = DocumentEditingSystem()
        self.assertEqual(doc.edit_document(), "Invalid operation in current state")
        doc.save_document()
        self.assertEqual(doc.save_document(), "Invalid operation in current state")

    # 26 ElevatorSystem
    def test_elevator_movement_and_stop(self):
        """Elevator movement and stop transitions."""
        el = ElevatorSystem()
        self.assertEqual(el.state, "Idle")
        self.assertEqual(el.move_up(), "Elevator moving up")
        self.assertEqual(el.state, "Moving Up")
        self.assertEqual(el.stop(), "Elevator stopped")
        self.assertEqual(el.state, "Idle")
        self.assertEqual(el.move_down(), "Elevator moving down")
        self.assertEqual(el.state, "Moving Down")
        self.assertEqual(el.stop(), "Elevator stopped")
        self.assertEqual(el.state, "Idle")

    def test_elevator_invalid_operations(self):
        """Invalid elevator operations."""
        el = ElevatorSystem()
        self.assertEqual(el.stop(), "Invalid operation in current state")
        el.move_up()
        self.assertEqual(el.move_up(), "Invalid operation in current state")
        self.assertEqual(el.move_down(), "Invalid operation in current state")


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
