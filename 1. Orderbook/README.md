# Orderbook

This project implements a digital order book for trading UAH (base asset) and USD (quote asset).

## Installation and Running

1. Ensure you have Python (version 3.x) installed.
2. Clone the repository.
3. Run the `main.py` file using the command `python main.py` in the console.

## Project Structure

- `order.py` - `Order` class representing an order.
- `orderbook.py` - `OrderBook` class managing buy and sell orders.
- `main.py` - Main file for running the program.
- `storage.py` - Functions for saving and loading the order book.
- `logger.py` - Logging transactions.
- `README.md` - This file.

## Usage

When running the program, you can enter orders in the format `user_id amount price side`, where:
- `user_id` - the user ID
- `amount` - the amount of UAH
- `price` - the price per 1 UAH in USD
- `side` - `buy` to buy or `sell` to sell

You can also type `clear` to clear the order book or `exit` to quit the program.

### Example 

````
1 1000 0.024 buy
2 50 0.023 sell
exit
````

The order book is automatically saved upon exiting the program and loaded upon the next start.

## Transaction Logging

Transactions are logged to a file named `transactions.log` with details about the buyer, seller, amount, and price.

## Algorithm and Data Structure Complexity

### Data Structures

1. **Buy Orders**: Max-heap for buy orders (using negative prices for max-heap behavior).
2. **Sell Orders**: Min-heap for sell orders.
3. **Balances**: Dictionary where keys are user IDs and values are dictionaries representing balances in USD and UAH.

### Operations

1. **Adding an Order**:
    - **Buy Order**: Insert into the `buy_orders` max-heap.
    - **Sell Order**: Insert into the `sell_orders` min-heap.

2. **Matching Orders**:
    - Continuously check the top of the `buy_orders` and `sell_orders` heaps to find matching orders.
    - Update the balances accordingly.

### Complexity Analysis

1. **Adding an Order**:
    - Inserting an order into a heap using `heapq.heappush()` takes `O(log n)` time complexity, where `n` is the number of orders in the heap.
    - Thus, the complexity of adding an order is `O(log n)`.

2. **Matching Orders**:
    - Matching orders involves checking the top elements of both heaps, which is an `O(1)` operation.
    - If a match is found, removing an order from the heap using `heapq.heappop()` takes `O(log n)` time.
    - The complexity for updating balances is `O(1)`.
    - Thus, the complexity of matching orders is `O(log n)` per match.

### Summary of Complexities

- **Adding an Order**: `O(log n)`
- **Matching Orders**: `O(log n)` per match.

## How Complexity Was Calculated

1. **Adding Orders**:
    - The `heapq.heappush()` function is used to insert elements into a heap. The binary heap structure ensures that the insertion point is found and adjusted in `O(log n)` time.

2. **Matching Orders**:
    - Checking the top elements of the buy and sell heaps is a direct index access operation, which takes `O(1)` time.
    - Removing the top elements when a match is found is `O(log n)` because it involves re-heapifying the heap.
    - The balance update operations involve dictionary lookups and updates, both of which are `O(1)` operations.
    - Thus, in each step, the matching process takes `O(log n)` time per match.

By maintaining these efficient data structures and operations, the order book ensures quick and reliable processing of buy and sell orders.

