from . import __View

class PlayAgain(__View):

    def print(self) -> str:
        return input("do you want to play again (yes,no)")

