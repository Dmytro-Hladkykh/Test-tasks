# Website Analytics Project

This project analyzes user data from two separate days to identify specific user behavior patterns related to product visits.

## Installation and Running

1. Ensure you have Python (version 3.x) installed.
2. Clone the repository to your local machine.
3. Run the `main.py` script using the command `python main.py` in your terminal or command prompt.

## Project Structure

- `main.py` - Main script that identifies users meeting the specified criteria.
- `day1.csv` - Sample CSV file representing user visits on day 1.
- `day2.csv` - Sample CSV file representing user visits on day 2.
- `README.md` - This file.

## Usage

The `main.py` script identifies users who:

 - Visited some pages on both days.
 - On the second day, visited a page that hadn’t been visited by this user on the first day.

# Solution Efficiency and Complexity Analysis

## Algorithm Explanation

1. Data Representation:

 - Each CSV file (`day1.csv` and `day2.csv`) is read and parsed to populate a nested dictionary (`visited_products`) where keys are `user_id`, and values are dictionaries (`day1` and `day2`) containing sets of `product_id` visited by each user on that day.

2. Finding Common Users:

 - Iterate over `visited_products` to find users who visited pages on both `day1` and `day2`.
 - Compare the sets of `product_id` for each user to determine if they visited different products on `day2`.

## Efficiency

 - **Time Complexity**: Reading and parsing each CSV file is `O(n)` where `n` is the number of entries in the file. Finding common users and comparing product sets is efficient due to dictionary and set operations.
 - **Space Complexity**: Uses memory efficiently by storing data in a nested dictionary structure (`visited_products`).

## Why this Solution is Efficient

 - **Hash Table Usage**: Utilizes a nested `defaultdict` structure with lambda-function (`visited_products`) to efficiently store and retrieve data about user visits across multiple days.
 - **Optimized Operations**: By leveraging Python's dictionary and set operations, the solution minimizes unnecessary iterations and comparisons, ensuring efficient processing of user data.
