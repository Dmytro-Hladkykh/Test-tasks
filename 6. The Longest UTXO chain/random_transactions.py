import csv
import random
import string

# Genmerate random UTXO identifier
def generate_utxo():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))

# Generate random Bitcoin-like transactions, where 
# num_transactions is the number of transactions to generate
def generate_transactions(filename, num_transactions):
    utxos = [generate_utxo() for _ in range(num_transactions + 1)]
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['tx_id', 'input_utxo', 'output_utxo1', 'output_utxo2'])
        
        for i in range(num_transactions):
            tx_id = f'tx_{i+1}'
            input_utxo = random.choice(utxos)
            output_utxo1 = generate_utxo()
            output_utxo2 = generate_utxo()
            
            writer.writerow([tx_id, input_utxo, output_utxo1, output_utxo2])
            
            # Remove the spent UTXO and add the new ones
            utxos.remove(input_utxo)
            utxos.extend([output_utxo1, output_utxo2])

if __name__ == "__main__":
    generate_transactions('transactions.csv', 1000)
    print("Generated transactions.csv with 1000 transactions.")