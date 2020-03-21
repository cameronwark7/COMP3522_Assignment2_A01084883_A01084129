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
        pass

    def create_candy(self) -> PCToffee:
        pass

    def create_toy(self) -> RCSpider:
        pass


class ChristmasFactory(InventoryFactory):
    def create_stuffed_animal(self) -> Reindeer:
        pass

    def create_candy(self) -> CandyCanes:
        pass

    def create_toy(self) -> SantaWorkshop:
        pass


class EasterFactory(InventoryFactory):
    def create_stuffed_animal(self) -> EasterBunny:
        pass

    def create_candy(self) -> CremeEggs:
        pass

    def create_toy(self) -> RobotBunny:
        pass
