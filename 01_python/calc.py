__version__ = 0.1 #변수

def plus(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def multiplu(num1, num2):
    return num1 * num2

def divid(num1, num2):  
    return num1 / num2

#실행코드 -> main 모듈로 실행될때만 실행되도록 처리.
print(__name__)
if __name__ == "__main__":
    result = minus(10,5) #함수를 호출 -> 기본:같은 모듈에 정의된 함수를 호출
    print(result)

# python calc.py

result = minus(10, 5)
print(result)

# from 모듈명 import 함수1, 함수2
#현재 실행중인 모듈(메인)과 서브모듈을 구분하려면 if문을 사용해야한다.

