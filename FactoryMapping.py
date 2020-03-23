# from PyQt5.QtCore.QTextCodec import kwargs

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

class FactoryMapping:
    def __init__(self):
        self.order_num = None
        self.product_id = None
        self.item_type = None
        self.item_name = None
        self.holiday = None

    def determine_factory(self, holiday, item_type, my_dict):
        if holiday == 'Halloween':
            if item_type == 'StuffedAnimal':
                return HalloweenFactory.StuffedAnimalFactory(my_dict.get('size', None), self.item_name, self.product_id)
            elif item_type == 'Toy':
                return HalloweenFactory.ToyFactory(my_dict.get('min_age', None), self.item_name, my_dict.get('description', None),
                                                   self.product_id, my_dict.get('speed', None),
                                                   my_dict.get('jump_height', None),
                                                   my_dict.get('has_glow', None), my_dict.get('spider_type', None))
            elif item_type == 'Candy':
                return HalloweenFactory.CandyFactory(self.item_name, my_dict.get('description', None),
                                                     self.product_id, my_dict.get('variety', None))
        elif holiday == 'Easter':
            if item_type == 'StuffedAnimal':
                return EasterFactory.StuffedAnimalFactory(my_dict.get('size', None), self.item_name,
                                                          self.product_id, my_dict.get('colour', None))
            elif item_type == 'Toy':
                return EasterFactory.ToyFactory(my_dict.get('min_age', None), self.item_name,
                                                my_dict.get('description', None), self.product_id,
                                                my_dict.get('num_sound', None), my_dict.get('colour', None))
            elif item_type == 'Candy':
                return EasterFactory.CandyFactory(self.item_name, my_dict.get('description', None),
                                                  self.product_id, my_dict.get('pack_size', None))
        elif holiday == 'Christmas':
            if item_type == 'StuffedAnimal':
                return ChristmasFactory.StuffedAnimalFactory(my_dict.get('size', None), self.item_name, self.product_id)
            elif item_type == 'Toy':
                return ChristmasFactory.ToyFactory(my_dict.get('min_age', None), self.item_name, my_dict.get('description', None),
                                                   self.product_id, my_dict.get('dimensions', None), my_dict.get('num_rooms', None))
            elif item_type == 'Candy':
                return ChristmasFactory.CandyFactory(self.item_name, my_dict.get('description', None),
                                                     self.product_id, my_dict.get('colour', None))

class HalloweenFactory(InventoryFactory):
    class StuffedAnimalFactory:
        def __init__(self, size, name, product_id):
            self.size = size
            self.name = name
            self.product_id = product_id

        def create_item(self) -> DancingSkeleton:
            return DancingSkeleton(self.size, self.name, self.product_id)

    class ToyFactory:
        def __init__(self, min_age, name, description, product_id, speed, jump_height, glow_in_dark,
                 spider_type):
            self.min_age = min_age
            self.name = name
            self.description = description
            self.product_id = product_id
            self.speed = speed
            self.jump_height = jump_height
            self.glow_in_dark = glow_in_dark
            self.spider_type = spider_type

        def create_item(self) -> RCSpider:
            return RCSpider(self.min_age, self.name, self.description, self.product_id, self.speed, self.jump_height, self.glow_in_dark, self.spider_type)

    class CandyFactory:
        def __init__(self, name, description, product_id, variant):
            self.name = name
            self.description = description
            self.product_id = product_id
            self.variant = variant

        def create_item(self) -> PCToffee:
            return PCToffee(self.name, self.description, self.product_id, self.variant)


class ChristmasFactory(InventoryFactory):
    class StuffedAnimalFactory:
        def __init__(self, size, name, product_id):
            self.size = size
            self.name = name
            self.product_id = product_id

        def create_item(self) -> Reindeer:
            return Reindeer(self.size, self.name, self.product_id)

    class ToyFactory:
        def __init__(self, min_age, name, description, product_id, dimensions, num_rooms):
            self.min_age = min_age
            self.name = name
            self.description = description
            self.product_id = product_id
            self.dimensions = dimensions
            self.num_rooms = num_rooms

        def create_item(self) -> SantaWorkshop:
            return SantaWorkshop(self.min_age, self.name, self.description, self.product_id, self.dimensions, self.num_rooms)

    class CandyFactory:
        def __init__(self, name, description, product_id, stripe_colour):
            self.name = name
            self.description = description
            self.product_id = product_id
            self.stripe_colour = stripe_colour

        def create_item(self) -> CandyCanes:
            return CandyCanes(self.name, self.description, self.product_id, self.stripe_colour)


class EasterFactory(InventoryFactory):
    class StuffedAnimalFactory:
        def __init__(self, size, name, product_id, colour):
            self.size = size
            self.name = name
            self.product_id = product_id
            self.colour = colour

        def create_item(self) -> EasterBunny:
            return EasterBunny(self.size, self.name, self.product_id, self.colour)

    class ToyFactory:
        def __init__(self, min_age, name, description, product_id, num_sound_effects, colour):
            self.min_age = min_age
            self.name = name
            self.description = description
            self.product_id = product_id
            self.num_sound_effects = num_sound_effects
            self.colour = colour

        def create_item(self) -> RobotBunny:
            return RobotBunny(self.min_age, self.name, self.description, self.product_id, self.num_sound_effects, self.colour)

    class CandyFactory:
        def __init__(self, name, description, product_id, pack_size):
            self.name = name
            self.description = description
            self.product_id = product_id
            self.pack_size = pack_size

        def create_item(self) -> CremeEggs:
            return CremeEggs(self.name, self.description, self.product_id, self.pack_size)