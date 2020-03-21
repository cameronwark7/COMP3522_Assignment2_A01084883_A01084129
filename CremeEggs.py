from Candy import Candy


class CremeEggs(Candy):
    def __init__(self, name, description, product_id, pack_size):
        super().__init__(name, description, product_id, False, False, "Easter")
        pack_size = pack_size
