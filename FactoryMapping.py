from PyQt5.QtCore.QTextCodec import kwargs

from CandyCanes import CandyCanes
from CremeEggs import CremeEggs
from DancingSkeleton import DancingSkeleton
from EasterBunny import EasterBunny
from PCToffee import PCToffee
from RCSpider import RCSpider
from Reindeer import Reindeer
from RobotBunny import RobotBunny
from SantaWorkshop import SantaWorkshop
from StuffedAnimals import StuffedAnimals
from Toy import Toy
from Candy import Candy
import abc


class InventoryFactory(abc.ABC):
    @abc.abstractmethod
    def create_toy(self) -> Toy:
        pass

    @abc.abstractmethod
    def create_stuffed_animal(self) -> StuffedAnimals:
        pass

    @abc.abstractmethod
    def create_candy(self) -> Candy:
        pass


class HalloweenFactory(InventoryFactory):

    def create_stuffed_animal(self) -> DancingSkeleton:
        return DancingSkeleton(self, **kwargs)

    def create_candy(self) -> PCToffee:
        return PCToffee(self, **kwargs)

    def create_toy(self) -> RCSpider:
        return RCSpider(self, **kwargs)


class ChristmasFactory(InventoryFactory):
    def create_stuffed_animal(self) -> Reindeer:
        return Reindeer(self, **kwargs)

    def create_candy(self) -> CandyCanes:
        return CandyCanes(self, **kwargs)

    def create_toy(self) -> SantaWorkshop:
        return SantaWorkshop(self, **kwargs)


class EasterFactory(InventoryFactory):
    def create_stuffed_animal(self) -> EasterBunny:
        return EasterBunny(self, **kwargs)

    def create_candy(self) -> CremeEggs:
        return CremeEggs(self, **kwargs)

    def create_toy(self) -> RobotBunny:
        return RobotBunny(self, **kwargs)
