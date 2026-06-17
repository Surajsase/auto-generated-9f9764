import subprocess
import sys
import os
from unittest import TestCase, main

class TestMain(TestCase):
    def test_generate_cpp_code(self):
        # Mocking the subprocess call
        subprocess.check_output = lambda x, **kwargs: b'The cube of the number is: 125\n'
        from main import generate_cpp_code
        self.assertIn('The cube of the number is: 125', generate_cpp_code())

if __name__ == '__main__':
    main()