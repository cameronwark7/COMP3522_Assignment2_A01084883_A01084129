from Candy import Candy


class PCToffee(Candy):
    def __init__(self, name, description, product_id, variant):
        super().__init__(name, description, product_id, False, False, "Halloween")
        variant = variant  # sea salt or regular
