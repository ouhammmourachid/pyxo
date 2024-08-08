from typing import TYPE_CHECKING

from pyxo.utils import clear
from pyxo.views.view import View

if TYPE_CHECKING:
    from pyxo.controller import Engin


class AddPlayer(View):
    def __init__(self, controller: "Engin") -> None:
        self.controller: "Engin" = controller

    def print(self) -> None:
        clear()
        name_first_player: str = str(input("     the name of the player - 1 - :\t"))
        choice: str = input("      chose {X} or {O}  :\t ")
        self.controller.add_player(name_first_player, choice)
        name_second_player: str = str(input("     the name of the player - 2 - :\t"))
        self.controller.add_player(name_second_player)
