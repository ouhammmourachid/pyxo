from abc import ABC,abstractmethod


class View(ABC):
    
    @abstractmethod
    def print(self) -> None:
        pass


from .start import *
from .addplayer import *
from .playing import *
from .showiner import *
from .playagain import *
