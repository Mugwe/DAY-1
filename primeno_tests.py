import unittest

Import day1.prime_no_solution from primenumbers

class testprimenumbers(unittest.Testcase):
    
    def test_if_number_is_integer(self):
        answer = primenumbers("tracy")
        self.assertEqual(answer, "Enter an integer")

    def test_if_number_is_divisible_by_2(self)
		self.assertTrue(4%2 == 0,0)

    def test_if_number_is_equal_to_2(self)
        self.assertNotEqual(7,2)


    def test_if_number_is_zero(self)
		result = primenumbers(0)
		self.assertTrue(result, "invalid number"



if __name__ == '__main__':
    unittest()