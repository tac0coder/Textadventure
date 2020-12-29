class item():
    def __init__(self,
                 quantity: int,
                 item: str,
                 description: str = None,
                 code: list = None, type=None):
        self.quantity = str(quantity)
        self.item = item
        self.description = description
        self.get = (self.quantity, self.item, self.description)
        self.code = code
        self.type = type
# F#IXME:TRY scrap it and change the trigger function to 'mine' and make a new function for miners?

    def mine(self):
        __import__('run').main(code)

    def add(self, dic):
        dic[self.type] = self

    def get_values(self):
        self.description = __import__('shop').items[item][0]
        self.type = __import__('shop').items[item][2]
        self.code = __import__('shop').code[item]


class ore():
    def __init__(self, name):
        self.name = name
        self.price = __import__('shopp').worth[self.name]

    def sell(self, dic):
        try:
            dic['coins'].quantity += self.price
        except Exception as e:
            print(e)
