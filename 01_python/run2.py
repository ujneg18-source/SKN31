from calc import plus

def plus(num1, num2):
    return("안녕하세요")

result = plus(1, 2) 
print(result)
# plus => 라는 동일 함수를 만들면, 기존 함수를 덮어씀

from my_package import greet

greet.hello_kor()

import sys
sys.path.append(r'c:\temp\lib')

from new_package import new_module
new_module.test_func()
