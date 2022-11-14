# working of try()
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Answer is :", result)
    except ZeroDivisionError:
        print("Warning ! You are dividing by zero ")
 

divide(5, 2)