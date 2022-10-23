from utils import  equals


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

    
    def check_move(self,move :int) -> bool:
        if move > 0 and move < 4: return True if self.row_1[move] is None else False
        if move >3 and move < 7: return True if self.row_2[move%4] is None else False
        if move > 6 and move < 10: return True if self.row_2[move%7] is None else False
        return False

    def make_move(self,move:int,choise:bool) -> None:
        
        if move > 0 and move < 4: self.row_1[move] = choise
        if move >3 and move < 7: self.row_2[move%4] = choise
        if move > 6 and move < 10:self.row_1[move%7] = choise

    def game_ended(self) -> bool:
        return self.count_full() == 8 or self.winer_exist()


    def winer_exist(self) -> bool:
        return self.check_row() or self.check_colum() or self.check_corner()

    def check_row(self) -> bool:
        if equals(self.row_1[0],self.row_1[1],self.row_1[2]) :return True
        if equals(self.row_2[0],self.row_2[1],self.row_2[2]) :return True
        if equals(self.row_3[0],self.row_3[1],self.row_3[2]) :return True
        return False


    def check_colum(self) -> bool:
        
        if equals(self.row_1[0],self.row_2[0],self.row_3[0]) :return True
        if equals(self.row_1[1],self.row_2[1],self.row_3[1]) :return True
        if equals(self.row_1[2],self.row_2[2],self.row_3[2]) :return True
        return False

    def check_corner(self) -> bool:
        
        if equals(self.row_1[0],self.row_2[1],self.row_3[2]) :return True
        if equals(self.row_3[0],self.row_1[1],self.row_1[2]) :return True
        return False

    def count_full(self) -> int:
        count :int = 0
        for cas in self.row_1:
            if not (cas is None):
                count += 1

        for cas in self.row_2:
            if not (cas is None):
                count += 1

        for cas in self.row_3:
            if not (cas is None):
                count += 1
        return count
    
