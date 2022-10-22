from views import *
from models import *

class Engin:
    
    def __init__(self) -> None:

        
        self.views : dict[str,View] = {
                'start' : Start(),
                'add_player' : AddPlayer(self),
                'play_again' : PlayAgain(),
                'playing' : Playing(self),
                'show_winer' :ShoWiner(self)
        }

        self.players : list[Player] = list()
        self.board : Board = Board()
        self.status :str = 'not_started'
        self.winer :str = None
    
    def start_game(self) -> None:
        self.views['start'].print()
        self.status = 'started'

    def add_player(self,name:str,choise:str = None) -> None:
        
        player : Player = Player(name)

        if choise :
            player.set_choise(choise if choise in ['X','x','O','o'] else 'X')
        else :
            player.set_choise( not self.players[0].get_choise())

        self.players.append(player)

    def add_players(self) -> None:
        
        self.views['add_player'].print()
        self.status = 'not_playing'

    def play_again(self) -> None:
        
        want_play_again = True if self.views['play_again'].print() in ['YES','YEs','Yes','yes','ye','y','Y'] else False
        if want_play_again:
            self.status = 'not_playing'
        else :
            self.status = 'exit'


    def play_a_round(self,number:int) -> None:
        move :int = self.views['playing'].print(self.players[number])
        
        while not self.board.check_move(move):
            move = self.views['playing'].print_error()
        return move

    def playing(self) -> None:
       
        winer = " "
        #while winer is None:

         #   self.play_a_round()

        self.status = 'show_result'

    def show_winer(self) -> None:

        if self.winer is None:
            self.views['show_winer'].print_no_winer()
        else :
            self.views['show_winer'].print()
            self.winer = None

        self.status = 'ended'


    def run(self) -> None:


        while True:
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
                case 'exit':
                    break

        print("saving the result to the database ...")
        print("END")
