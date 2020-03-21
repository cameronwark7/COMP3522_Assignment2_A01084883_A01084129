from Toy import Toy


class RobotBunny(Toy):
    def __init__(self, min_age, name, description, product_id, num_sound_effects, colour):
        super().__init__(True, min_age, name, description, product_id)
        num_sound_effects = num_sound_effects
        colour = colour  # orange, blue, or pink
