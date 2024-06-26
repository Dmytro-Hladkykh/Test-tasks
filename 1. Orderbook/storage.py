import pickle
from orderbook import OrderBook

def save_orderbook(orderbook, filename='orderbook.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(orderbook, f)

def load_orderbook(filename='orderbook.pkl'):
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return OrderBook()
