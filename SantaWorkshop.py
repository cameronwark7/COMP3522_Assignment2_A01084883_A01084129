from Toy import Toy


class SantaWorkshop(Toy):
    def __init__(self, min_age, name, description, product_id, dimensions, num_rooms):
        super().__init__(False, min_age, name, description, product_id)
        dimensions = dimensions
        num_rooms = num_rooms