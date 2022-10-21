from views import *
from models import *

class Engin:
    
    def __init__(self) -> None:

        
        self.views : dict[str,__View] = {
                'start' : Start(),
                'add_player' : AddPlayer(self),
                'play_again' : PlayAgain(),
                'playing' : Playing(),
                'show_winer' :ShoWiner()
        }

        self.players : list[Player] = list()
        self.board : Board = Board()
        self.status :str = 'not_started'
        self.play_again ;bool = True
    
    def start_game(self) -> None:
        self.views['start'].print()
        self.status = 'started'

    def add_player(self,name:str,choise:str = None) -> None:
        
        player : Player = Player(name)

        if choise :
            player.set_choise(choise if choise in ['X','x','O','o'] else 'X')
        else :
            player.set_choise( not self.players[0].get_choise())

        self.player.append(player)

    def add_players(self) -> None:

        self.views['add_player'].print()
        self.status = 'not_palying'

    def play_again(self) -> None:
        
        self.play_again = True if ans in ['YES','YEs','Yes','yes','ye','y','Y'] else False

    def playing(self) -> None:
        
        # the code

        self.status = 'show_result'

    def show_winer(self) -> None:
        # the code 
        
        self.status = 'ended'


    def run(self) -> None:


        while self.play_again:
            match self.status:
                case 'not_started':
                    self.start_game()
                case 'started':
                    self.add_players()
                case 'not_playing':
                    self.playing()
                case 'show_result':
                    self.show_winer()
                case 'ended':
                    self.play_again()

        print("saving the result to the database ...")
        print("END")
