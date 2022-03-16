# Function to calculate order of the number
def order(x):
  
    # Variable to store of the number
    n = 0
    while (x != 0):
        n = n + 1
        x = x // 10
          
    return n	
y = order(153)
print("Order is " , y)
