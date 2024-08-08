from pyxo.utils import clear, show_board
from pyxo.views.view import View


class Playing(View):
    def __init__(self, controller: "Engin") -> None:
        self.controller: "Engin" = controller

    def print(self, number: int) -> int:
        clear()
        show_board(self.controller.board, self.controller.players)

        try:
            return int(
                input(
                    f"  what is your next move  {self.controller.players[number].name}  :(1...9) \t"
                )
            )
        except Exception:
            return 100

    def print_error(self) -> int:
        try:
            return int(
                input(" this number is not available chose an other one:(1...9) \t")
            )
        except Exception:
            return 100
