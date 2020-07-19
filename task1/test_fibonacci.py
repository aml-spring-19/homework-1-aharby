import fib
import unittest

class TestFibonadfacci (unittest.TestCase):
    
    def test_fib(self):
        self.assertEqual(fib.fib(2), 1)
        self.assertEqual(fib.fib(5), 5)
        self.assertEqual(fib.fib(12), 144)
        
