from StuffedAnimals import StuffedAnimals


class EasterBunny(StuffedAnimals):
    def __init__(self, size, name, product_id, colour):
        super().__init__("Polyester", size, "Linen", name, "Comes in different colours", product_id)
        colour = colour  # white, grey, pink or blue
