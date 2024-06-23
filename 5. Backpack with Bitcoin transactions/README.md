# Backpack with Bitcoin transactions

This program constructs a Bitcoin block by selecting transactions to maximize the total fee while respecting the block size limit. It uses a greedy algorithm approach for efficient transaction selection.

## How to Run

1. **Clone the repository.** 
2. **Place the `transactions.csv` file in the same directory or generate the test one running `random_transactions.py`**
3. **Run the main script with `python main.py`**
4. **The program will automatically process the transactions and output the results.**

## Input 

The program expects a `transactions.csv` file in the following format:
```
tx_id,tx_size,tx_fee
tx_001,250,1000
tx_002,100,300
```
You can use `random_transactions.py` to generate a test csv-file to check how the script works.

## Output

The program will output:
- A sample of transactions included in the block
- The total number of transactions in the block
- The total size of the block
- The total fee collected
- The time taken to construct the block
- The maximum memory used during execution

## Efficiency

### Time Complexity

- **Sorting:** O(n log n), where n is the number of transactions.
- **Greedy Selection:** O(n), as it iterates through the sorted list once.
- **Overall:** O(n log n) due to the sorting step.

### Space Complexity

- O(n) to store the list of transactions and selected transactions.

## Algorithm

The program uses a greedy approach:
1. Sort transactions by fee-to-size ratio (descending).
2. Iterate through sorted transactions, adding them to the block if they fit.
3. Continue until the block is full or all transactions are processed.

This approach provides a good approximation of the optimal solution in linear time after sorting.