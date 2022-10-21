# libraries
from views.start import Start 
import time
import os

def main() -> None:
    
    start = Start()
    start.print()
    _ = input("to continue press enter :")
    start.print()


if __name__ == '__main__':
    main()


