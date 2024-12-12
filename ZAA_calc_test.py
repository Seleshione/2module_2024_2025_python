import unittest
from ZAA_calc import process_key, trig_test, evaluate_expression_test, factorial_test, convert_test

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        result, _ = process_key("=", "2+2")
        self.assertEqual(result, "4")

    def test_subtraction(self):
        result, _ = process_key("=", "5-3")
        self.assertEqual(result, "2")

    def test_multiplication(self):
        result, _ = process_key("=", "3*4")
        self.assertEqual(result, "12")

    def test_division(self):
        result, _ = process_key("=", "10/2")
        self.assertEqual(result, "5.0")

    def test_trigonometry_sin(self):
        result, _ = process_key("sin", "30")
        self.assertEqual(result, str(trig_test(30, "sin")))

    def test_trigonometry_tg(self):
        result, _ = process_key("tg", "45")
        self.assertEqual(result, str(trig_test(45, "tg")))

    def test_factorial(self):
        result, _ = process_key("x!", "5")
        self.assertEqual(result, "120")

    def test_base_conversion(self):
        result, _ = process_key("2-ная", "10")
        self.assertEqual(result, "1010")

    def test_negative_sign(self):
        result, _ = process_key("±", "5")
        self.assertEqual(result, "-5")
        result, _ = process_key("±", "-5")
        self.assertEqual(result, "5")

    def test_clear_entry(self):
        result, _ = process_key("Del", "123")
        self.assertEqual(result, "")

    def test_abs(self):
        result, abs_value = process_key("=", "5")
        result, _ = process_key("Abs", "", abs_value)
        self.assertEqual(result, "5")

    def test_invalid_expression(self):
        result, _ = process_key("=", "5/0")
        self.assertEqual(result, "Данное выражение не определено")
        
    def test_addition_1(self):
        self.assertEqual(evaluate_expression_test("2 + 3"), 5)

    def test_subtraction_1(self):
        self.assertEqual(evaluate_expression_test("10 - 4"), 6)

    def test_multiplication_1(self):
        self.assertEqual(evaluate_expression_test("3 * 7"), 21)

    def test_division_1(self):
        self.assertEqual(evaluate_expression_test("8 / 2"), 4.0)

    def test_division_by_zero(self):
        self.assertEqual(evaluate_expression_test("5 / 0"), "Данное выражение не определено")

    def test_negative_result(self):
        self.assertEqual(evaluate_expression_test("2 - 5"), -3)

    def test_float_result(self):
        self.assertEqual(evaluate_expression_test("5 / 2"), 2.5)

    def test_combined_operations(self):
        self.assertEqual(evaluate_expression_test("2 + 3 * 4 - 5"), 9)

    def test_invalid_expression(self):
        with self.assertRaises(SyntaxError):
            evaluate_expression_test("2 +")
            
    def test_factorial_of_zero(self):
        self.assertEqual(factorial_test(0), 1)  

    def test_factorial_of_positive_integer(self):
        self.assertEqual(factorial_test(5), 120)  
        self.assertEqual(factorial_test(3), 6)    
        self.assertEqual(factorial_test(1), 1)    

    def test_factorial_of_large_integer(self):
        self.assertEqual(factorial_test(10), 3628800)  

    def test_factorial_of_negative_integer(self):
        with self.assertRaises(ValueError):
            factorial_test(-1)  

    def test_factorial_of_non_integer(self):
        with self.assertRaises(ValueError):
            factorial_test(4.5)  
        with self.assertRaises(ValueError):
            factorial_test("string")  
        with self.assertRaises(ValueError):
            factorial_test([])  
            
    def test_convert_positive_integer_to_binary(self):
        self.assertEqual(convert_test(10, 2), '1010')

    def test_convert_positive_integer_to_octal(self):
        self.assertEqual(convert_test(10, 8), '12')

    def test_convert_positive_integer_to_decimal(self):
        self.assertEqual(convert_test(10, 10), '10')

    def test_convert_positive_integer_to_hexadecimal(self):
        self.assertEqual(convert_test(255, 16), 'FF')

    def test_convert_zero(self):
        self.assertEqual(convert_test(0, 2), '0')

    def test_convert_negative_integer(self):
        self.assertEqual(convert_test(-10, 2), '-1010')

    def test_invalid_base_too_low(self):
        with self.assertRaises(ValueError):
            convert_test(10, 1)
            
    def test_sin_positive(self):
        self.assertEqual(trig_test(30, "sin"), 0.5)

    def test_sin_negative(self):
        self.assertEqual(trig_test(-30, "sin"), -0.5)

    def test_cos_positive(self):
        self.assertEqual(trig_test(60, "cos"), 0.5)

    def test_cos_negative(self):
        self.assertEqual(trig_test(-60, "cos"), 0.5)

    def test_tg_positive(self):
        self.assertEqual(trig_test(45, "tg"), 1.0)

    def test_tg_negative(self):
        self.assertEqual(trig_test(-45, "tg"), -1.0)

    def test_ctg_positive(self):
        self.assertEqual(trig_test(45, "ctg"), 1.0)

    def test_ctg_negative(self):
        self.assertEqual(trig_test(-45, "ctg"), -1.0)

    def test_tg_zero_division(self):
        self.assertEqual(trig_test(90, "tg"), "Тангенс не определён для данного угла.")

    def test_ctg_zero_division(self):
        self.assertEqual(trig_test(0, "ctg"), "Котангенс не определён для данного угла.")

    def test_invalid_function_type(self):
        self.assertEqual(trig_test(30, "invalid"), "Неизвестный тип тригонометрической функции.")

if __name__ == "__main__":
    unittest.main()