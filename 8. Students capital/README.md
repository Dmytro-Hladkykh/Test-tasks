# Student's Capital 

This CLI application calculates the maximum capital a student can achieve by buying, fixing, and selling laptops over the summer.

## Features

- Calculates the optimal selection of laptops to maximize profit
- Handles constraints on the number of laptops that can be bought
- Considers initial capital and ensures purchases are within budget

## How to Run

1. **Clone this repository.**
2. **Ensure you have Python installed on your system.**
3. **Run the script with the command: `python main.py`**
6. **Follow the prompts to enter the required information:**
- N: The maximum number of laptops you can buy
- C: Your initial capital
- Gains: The expected gain for each laptop (space-separated integers)
- Prices: The price of each laptop (space-separated integers)
7. **The application will output your capital at the end of the summer.**

## Input Format

- N: A single integer
- C: A single integer
- Gains: Space-separated integers (e.g., "100 200 300")
- Prices: Space-separated integers (e.g., "80 150 250")

## Example

**Input**:
```
Enter the number of laptops you can buy (N): 2
Enter your initial capital (C): 300
Enter the gains for each laptop (separated by spaces): 100 200 300
Enter the prices for each laptop (separated by spaces): 80 150 250
```

**Output**:
```
Your capital at the end of the summer: 370
```

This means that by strategically buying and selling laptops, you can increase your initial capital of 300 to 370 by the end of the summer.

## Algorithm Explanation

The algorithm works as follows:
1. Calculate the profit ratio (gain/price) for each laptop.
2. Sort the laptops by their profit ratio in descending order.
3. Iterate through the sorted list, buying laptops if:
   a) You haven't reached the maximum number of laptops (N)
   b) You have enough capital to buy the laptop
4. For each purchased laptop, update your capital by subtracting the price and adding the gain.

This greedy approach ensures maximum profit within the given constraints.

## Note

- Ensure that the number of gains and prices entered matches the number of available laptops.
- The application assumes all inputs are valid integers.
