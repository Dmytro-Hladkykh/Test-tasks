class Order:
    def __init__(self, user_id, amount, price, side, timestamp):
        self.user_id = user_id
        self.amount = amount
        self.price = price
        self.side = side  # True for buy, False for sell
        self.timestamp = timestamp  

    def __lt__(self, other):
        if self.price == other.price:
            return self.timestamp < other.timestamp
        return self.price < other.price

    def __repr__(self):
        return f'Order(user_id={self.user_id}, amount={self.amount}, price={self.price}, side={"buy" if self.side else "sell"})'
