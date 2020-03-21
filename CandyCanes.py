from Candy import Candy


class CandyCanes(Candy):
    def __init__(self, name, description, product_id, stripe_colour):
        super().__init__(name, description, product_id, True, True, "Christmas")
        stripe_colour = stripe_colour  # red or green
