import csv
import time
import sys
from collections import namedtuple

# Define a named tuple for transactions
Transaction = namedtuple('Transaction', ['id', 'size', 'fee'])

def read_transactions(filename='transactions.csv'):
    transactions = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                tx_id, tx_size, tx_fee = row
                transactions.append(Transaction(tx_id, int(tx_size), int(tx_fee)))
    except FileNotFoundError:
        print(f"Error: File {filename} was not found.")
        sys.exit(1)
    return transactions

def greedy_construct_block(transactions, max_block_size):
    remaining_size = max_block_size
    selected_transactions = []
    total_fee = 0

    for tx in transactions:
        if tx.size <= remaining_size:
            selected_transactions.append(tx)
            remaining_size -= tx.size
            total_fee += tx.fee

    return selected_transactions, total_fee

def main():
    max_block_size = 1_000_000  # 1MB в байтах

    start_time = time.time()
    transactions = read_transactions()
    
    # Sort transactions by fee/size ratio
    transactions.sort(key=lambda x: x.fee / x.size, reverse=True)
    
    selected_transactions, total_fee = greedy_construct_block(transactions, max_block_size)
    end_time = time.time()

    # Calculate results
    block_size = sum(tx.size for tx in selected_transactions)
    construction_time = end_time - start_time
    max_memory = sys.getsizeof(transactions) + sys.getsizeof(selected_transactions)

    # Displaying the results
    print(f"Constructed block:")
    for tx in selected_transactions[:10]:  
        print(f"  Transaction ID: {tx.id}, Size: {tx.size}, Fee: {tx.fee}")
    if len(selected_transactions) > 10:
        print("  ...")
    print(f"Amount of transactions in the block: {len(selected_transactions)}")
    print(f"Block size: {block_size} bytes")
    print(f"Total fee: {total_fee} satoshis")
    print(f"Construction time: {construction_time:.4f} seconds")
    print(f"Max memory used: {max_memory} bytes")

if __name__ == "__main__":
    main()