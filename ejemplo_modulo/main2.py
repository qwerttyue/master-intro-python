# programa principal

import sys
from module2 import sumar

# if __name__ == "__main__":
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
print(f"{num1} + {num2} = {sumar(num1, num2)}")
