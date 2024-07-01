#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
#from src.question_d.question_d import get_sum_of_evens
from src.question_d.question_d import get_sum_of_evens
class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, Test_Config(get_sum_of_evens))

original_string = "Hello, World"
reversed_string = ''
index = len(original_string) - 1

while index >= 0:
  reversed_string += original_string(index)
  index -= 1

  print("Original String:", original_string)
  print("Reversed String", reversed_string)

def test_get_sum_of_evens(self):
   self.assertEqual(11, (get_sum_of_evens, 30))
   self.assertEqual(10, (get_sum_of_evens, 30))
   self.assertEqual(8, (get_sum_of_evens, 30))
   