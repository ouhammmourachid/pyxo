class Player:
    """the player class is a model that hold :
    the name :str of the player.
    the points :int contain how many time you win.
    the choice :bool contain true if player X other wise it contain false.
    """

    def __init__(self, name: str) -> None:
        """to create an player you need just a name and the number of point
        hold by default 0 in the beginning of th game.
        ```python
        >>> player = Player('rachid')
        >>> # to change the name
        >>> player.name = 'new name'
        ```
        """

        self.name: str = name
        self.points: int = 0

    def set_choice(self, choice: bool) -> None:
        """this method allow you to set the choice of the player
        like this:
        ```python
        >>> player = Player('rachid')
        >>> player.set_choise('X')
        >>> player.choice
        True
        ```
        """

        self.choice: bool = choice

    def get_choice(self) -> bool:
        return self.choice
