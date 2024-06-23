# The Longest UTXO chain

This program finds the longest chain of Unspent Transaction Outputs (UTXOs) in a Bitcoin-like system, applying specific filtering rules.

## Features

- Filters transactions to include only those with one input and two outputs.
- Builds a graph representation of UTXO connections.
- Uses Depth-First Search (DFS) to find the longest UTXO chain.
- Includes a script to generate test data.
- Optimized to handle large datasets efficiently.

## How to Run

1. **Clone this repository**
2. **Generate test data (Optional): `python random_transactions.py`**
This will create a `transactions.csv` file with 1000 random transactions.
3. **Run the main script with `python main.py`**
4. **The program will automatically read from `transactions.csv` in the same directory and process it.**

## Input 

The input CSV file should have the following format:

```
tx_id,input_utxo,output_utxo1,output_utxo2
tx1,utxo1,utxo2,utxo3
tx2,utxo2,utxo4,utxo5
...
```
## Configuration

- To change the number of transactions in the generated test data, modify the argument in the `generate_transactions()` function call in `random_transactions.py`.
```
generate_transactions('transactions.csv', `argument to changge`)
```
- The main script `main.py` does not require additional configuration. It uses the filtering rules (one input, two outputs) by default.

## Algorithm Explanation

1. The program loads transactions from the CSV file.
2. It builds a graph where nodes are UTXOs and edges represent connections between input and output UTXOs.
3. The algorithm identifies potential starting points by finding UTXOs that are not outputs of any transaction.
4. It then performs a Depth-First Search (DFS) from each starting point to find the longest chain.
5. The longest chain found is returned as the result.

## Performance Considerations

- The program uses a dictionary-based graph representation for efficient lookup.
- DFS is only initiated from potential starting points, reducing unnecessary computations.
- The algorithm can handle large datasets by avoiding full graph traversal for each UTXO.

## Additional Information

- **The program assumes that the input CSV file is well-formed and contains valid data.**
- **Time complexity:** O(V + E), where V is the number of UTXOs and E is the number of connections between them.
- **Space complexity**: O(V), as we store the graph and visited sets.



