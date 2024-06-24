from order import Order
from orderbook import OrderBook
from storage import save_orderbook, load_orderbook
import time

def main():
    orderbook = load_orderbook('orderbook.pkl')
    
    while True:
        print("Enter an order (user_id, amount, price, side) or 'exit' to quit or 'clear' to clear order book:")
        user_input = input().strip()
        if user_input.lower() == 'exit':
            break
        if user_input.lower() == 'clear':
            orderbook.clear()
            continue
        try:
            user_id, amount, price, side = user_input.split()
            timestamp = time.time()  
            order = Order(int(user_id), int(amount), float(price), side.lower() == 'buy', timestamp)
            orderbook.add_order(order)
            orderbook.print_order_book()
        except ValueError:
            print("Invalid input. Please try again.")
    
    save_orderbook(orderbook, 'orderbook.pkl')

if __name__ == "__main__":
    main()
