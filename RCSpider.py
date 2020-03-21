from Toy import Toy


class RCSpider(Toy):
    def __init__(self, min_age, name, description, product_id, speed, jump_height, glow_in_dark,
                 spider_type):
        super().__init__(True, min_age, name, description, product_id)
        speed = speed
        jump_height = jump_height
        glow_in_dark = glow_in_dark
        spider_type = spider_type  # tarantula or wolf spider
