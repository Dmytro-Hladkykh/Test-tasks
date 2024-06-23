import csv
from collections import defaultdict

# Class representing a Bitcoin transaction with one input and two outputs
class Transaction:
    def __init__(self, tx_id, input_utxo, output_utxo1, output_utxo2):
        self.tx_id = tx_id
        self.input_utxo = input_utxo
        self.output_utxo1 = output_utxo1
        self.output_utxo2 = output_utxo2

# Load transactions from a CSV file
def load_transactions(filename='transactions.csv'):
    transactions = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            tx_id, input_utxo, output_utxo1, output_utxo2 = row
            transactions.append(Transaction(tx_id, input_utxo, output_utxo1, output_utxo2))
    return transactions

# Build a graph representation of UTXO connections
# Graph is a defaultdict where keys are input UTXOs 
# and values are lists of output UTXOs
def build_graph(transactions):
    graph = defaultdict(list)
    for tx in transactions:
        graph[tx.input_utxo].extend([tx.output_utxo1, tx.output_utxo2])
    return graph

# Perform DFS to find the longest path in the graph
def dfs(graph, start_node, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    
    visited.add(start_node)
    path.append(start_node)
    
    longest_path = path.copy()
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, visited.copy(), path.copy())
            if len(new_path) > len(longest_path):
                longest_path = new_path
    
    return longest_path

# Find the longest UTXO chain in the transaction set
def find_longest_chain(transactions):
    graph = build_graph(transactions)
    longest_chain = []
    
    # Create a set of all UTXOs
    all_utxos = set(graph.keys())
    for tx in transactions:
        all_utxos.add(tx.output_utxo1)
        all_utxos.add(tx.output_utxo2)
    
    # Find UTXOs that are not outputs of any transaction (potential starting points)
    start_utxos = all_utxos - set(utxo for tx in transactions for utxo in [tx.output_utxo1, tx.output_utxo2])
    
    for start_node in start_utxos:
        path = dfs(graph, start_node)
        if len(path) > len(longest_chain):
            longest_chain = path
    
    return longest_chain

def main():
    transactions = load_transactions()
    longest_chain = find_longest_chain(transactions)
    
    print(f"Longest UTXO chain length: {len(longest_chain)}")
    print("Chain:")
    for utxo in longest_chain:
        print(utxo)

if __name__ == "__main__":
    main()