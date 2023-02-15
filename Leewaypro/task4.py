def try_catch():
    try:
        num=int(input("Enter a number :"))

        if not num:
            raise ZeroDivisionError("Sorry cannot Divide with 0")
        else:
            print(f"Answer is {100/num}")
    except  ValueError:
        print("Invalid input only number allowed")
    except ZeroDivisionError as e:
        print(e)
print("Some code before")
try_catch()
print("Some code After")













'''
class MyException(Exception):
    pass
def try_catch():
    try:
        num=int(input("Enter a number :"))
        if not num:
            raise MyException("Sorry cannot Divide with 0")
        else:
            print(f"Answer is {100/num}")
    except  ValueError:
        print("Invalid input only number allowed")
    except MyException as e:
        print(e)
print("Some code before")
try_catch()
print("Some code After")
'''