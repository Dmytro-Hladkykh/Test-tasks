import pickle
from orderbook import OrderBook

def save_orderbook(orderbook, filename='orderbook.pkl'):
    """Saves the order book to a file."""
    with open(filename, 'wb') as f:
        pickle.dump(orderbook, f)

def load_orderbook(filename='orderbook.pkl'):
    """Loads the order book from a file. If the file does not exist, returns a new OrderBook."""
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return OrderBook()
