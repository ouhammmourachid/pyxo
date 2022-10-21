import os


def clear() -> None:

    """this function is respenseble of clearing 
    the terminal on linux or the console on 
    windows .
    """

    try:
        os.system("clear")
    except Exception as ex:
        os.system("cls")



