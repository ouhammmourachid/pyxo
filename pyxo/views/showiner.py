from pyxo.utils import clear
from pyxo.views.view import View


class ShoWiner(View):
    def __init__(self, controller: "Engin") -> None:
        self.controller: "Engin" = controller

    def print(self) -> None:
        clear()
        print(f"\n\n the winer is 🏆 {self.controller.winer} 🏆")

    def print_no_winer(self) -> None:
        print("\n\n   draw no winer 🫠")
