from StuffedAnimals import StuffedAnimals


class Reindeer(StuffedAnimals):
    def __init__(self, size, name, product_id):
        super().__init__("Wool", size, "Cotton", name, "Has glow in the dark nose", product_id)