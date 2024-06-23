import csv
import random

def generate_transactions(filename, num_transactions):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(num_transactions):
            tx_id = f"tx_{i+1:06d}"  # Creates IDs like tx_000001, tx_000002, etc.
            tx_size = random.randint(100, 1000)  # Random size between 100 and 1000 bytes
            tx_fee = random.randint(100, 5000)   # Random fee between 100 and 5000 satoshis
            writer.writerow([tx_id, tx_size, tx_fee])

generate_transactions('transactions.csv', 100000)