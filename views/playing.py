from . import View
from utils import show_board
from models import Player


class Playing(View):

    def __init__(self,controler:"Engin") -> None:
        self.controler :"Engin" = controler

    def print(self,player:Player) -> int:
        show_board(self.controler.board,self.controler.players)
        move :int = int(input(f"  what is your next move  {player.name}  :(1...9)"))
        return move

    def print_error(self) -> int:

        return int(input(" tnis nomber is not vailable chose an ather one:(1...9) \t"))

        

