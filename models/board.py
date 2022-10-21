

class Board:

    """the Board is the model responseble of saving 
    the information about the board of the X O game
    and every player move.
    Every board has three rows every row contain three
    case with True for X and False for O.
    """

    def __init__(self) -> None:
       
        """to create an object Board use this following code:
        ```python
        >>> xo_board = Board()
        >>> # to see the rows you need this code
        >>> xo_board.row_1 # or xo_board.row_2
        ```
        """

        self.row_1 :list[bool] = 3*[None]
        self.row_2 :list[bool] = 3*[None]
        self.row_3 :list[bool] = 3*[None]


    def reset(self) -> None:
        
        """After the end of the game of XO
        we need to reset the board to do that we use this
        folowing code :
        ```python
        >>> xo_board = Board()
        >>> xo_board.reset()
        ```
        """

        self.row_1 :list[bool] = 3*[None]
        self.row_1 :list[bool] = 3*[None]
        self.row_1 :list[bool] = 3*[None]
