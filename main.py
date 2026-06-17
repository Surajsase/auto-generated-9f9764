import sys
import os
import subprocess

def generate_cpp_code():
    cpp_code = '''
    #include <iostream>
    
    int main() {
        int num;
        std::cout << "Enter a number: ";
        std::cin >> num;
        int cube = num * num * num;
        std::cout << "The cube of the number is: " << cube << std::endl;
        return 0;
    }
    '''
    with open('cube.cpp', 'w') as f:
        f.write(cpp_code)
    try:
        subprocess.check_output(['g++', 'cube.cpp', '-o', 'cube'])
        result = subprocess.check_output(['./cube'], input=b'5\n').decode('utf-8')
        return result
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    print(generate_cpp_code())