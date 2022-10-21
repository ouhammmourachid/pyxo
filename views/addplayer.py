from . import __View

class AddPlayer(__View):
    
    count :int = 1

    def print(self) -> None:
        name :str = str(input(f'  what is your name of the player {AddPlayer.count} :\t'))
        
