import heapq
from order import Order
from logger import log_transaction

class OrderBook:
    def __init__(self):
        self.buy_orders = []  # Max-heap for buy orders
        self.sell_orders = []  # Min-heap for sell orders
        self.balances = {}  # Dictionary to store user balances

    def add_order(self, order):
        if order.side:
            # Insert into buy_orders as a max-heap (negate price for max-heap behavior)
            heapq.heappush(self.buy_orders, (-order.price, order))
        else:
            # Insert into sell_orders as a min-heap
            heapq.heappush(self.sell_orders, (order.price, order))
        
        self.match_orders()
    
    def match_orders(self):
        while self.buy_orders and self.sell_orders and -self.buy_orders[0][0] >= self.sell_orders[0][0]:
            buy_order = heapq.heappop(self.buy_orders)[1]
            sell_order = heapq.heappop(self.sell_orders)[1]

            traded_amount = min(buy_order.amount, sell_order.amount)
            trade_price = sell_order.price  # Execute at sell price

            # Update balances
            self.update_balance(buy_order.user_id, -traded_amount * trade_price, 'USD')
            self.update_balance(buy_order.user_id, traded_amount, 'UAH')
            self.update_balance(sell_order.user_id, traded_amount * trade_price, 'USD')
            self.update_balance(sell_order.user_id, -traded_amount, 'UAH')

            # Log transaction
            log_transaction(buy_order.user_id, sell_order.user_id, traded_amount, trade_price)

            # Adjust or remove orders
            buy_order.amount -= traded_amount
            sell_order.amount -= traded_amount
            if buy_order.amount > 0:
                heapq.heappush(self.buy_orders, (-buy_order.price, buy_order))
            if sell_order.amount > 0:
                heapq.heappush(self.sell_orders, (sell_order.price, sell_order))
    
    def update_balance(self, user_id, value, currency):
        if user_id not in self.balances:
            self.balances[user_id] = {'USD': 0, 'UAH': 0}
        self.balances[user_id][currency] += value
        print(f'BalanceChange{{user_id: {user_id}, value: {value}, currency: {currency}}}')
    
    def print_order_book(self):
        print("Buy Orders:")
        for price, order in sorted(self.buy_orders, reverse=True):
            print(f'{order.user_id}: {order.amount} UAH @ {-price} USD')
        print("Sell Orders:")
        for price, order in sorted(self.sell_orders):
            print(f'{order.user_id}: {order.amount} UAH @ {price} USD')

    def save_to_file(self, filename):
        import pickle
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
    
    @staticmethod
    def load_from_file(filename):
        import pickle
        with open(filename, 'rb') as f:
            return pickle.load(f)

    def clear(self):
        self.buy_orders.clear()
        self.sell_orders.clear()
        self.balances.clear()
        print("Order book cleared.")
