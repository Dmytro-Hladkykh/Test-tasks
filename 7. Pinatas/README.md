# Pinatas

This CLI application calculates the maximum number of candies you can get from smashing a pinata in a specific position within an array of pinatas.

## Features

- Processes an array of pinatas, each containing a specific number of candies.
- Calculates the maximum number of candies obtainable by smashing a single pinata.
- Handles edge cases where the pinata is at the start or end of the array.

## How to Run

1. **Clone this repository.**
2. **Ensure you have Python installed on your system.**
3. **Run the script with the command: `python main.py`**
4. **When prompted, enter the numbers representing the candies in each pinata, separated by spaces.**

## Input

The input should be a series of integers separated by spaces, representing the number of candies in each pinata.

Example:
```
Enter numbers divided by spaces: 3 1 5 8
```

## Output

The program will output the maximum number of candies obtainable by smashing a single pinata.

Example:
```
Max number of candies: 40
```

## Algorithm Explanation

1. The program creates a list of pinatas from the user input.
2. For each pinata, it calculates the number of candies that would drop if that pinata were smashed.
3. The calculation for each pinata is: `previous_pinata * current_pinata * next_pinata`
   - If there's no previous or next pinata (i.e., at the edges of the array), the value 1 is used instead.
4. The program then finds and returns the maximum value from these calculations.

## Performance Considerations

- Time complexity: O(n), where n is the number of pinatas.
- Space complexity: O(n) to store the input and calculated values.

## Additional Information

- The program assumes that the input consists of valid integers.
- There is no limit to the number of pinatas that can be processed, but very large inputs may be limited by system memory.

## Error Handling

If invalid input is provided (e.g., non-integer values), the program will raise a `ValueError`. Ensure all inputs are valid integers.