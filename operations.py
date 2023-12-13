def basic_operations(a, b):
    # Perform basic arithmetic operations
    result = {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b
    }
    return result


def power_operation(base,exponent,**kwargs):
    print(int(base)**int(exponent))



try:
        num=int(input("enter num "))
        num2=int(input("enter num2 "))
        result=num/num2
        print(result) 
except ZeroDivisionError:
        print("you can't divide by zero")
except ValueError:
        print("Enter only numbers")