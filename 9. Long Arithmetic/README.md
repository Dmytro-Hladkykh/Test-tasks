# Long Arithmetic

The `BigInt` class provides a way to handle arbitrarily large integers, exceeding the typical capabilities of standard integer types. This README provides an overview of its implementation, approach to solving large integer operations, and the functionality of its methods compared to standard integer operations.

## Implementation Overview

The `BigInt` class uses a vector of `uint32_t` to store digits of the integer and includes a boolean flag `negative` to handle negative numbers. Key operations like addition, subtraction, multiplication, division, modulus, exponentiation, and comparison are implemented to work seamlessly with large numbers.

## How to Compile and Run

To compile and run the unit tests for the BigInt class implementation, follow these steps:

**Prerequisites**

Ensure you have the following installed on your system:

 - C++ compiler that supports C++11 or later (e.g., GCC, Clang)

**Steps**

1. **Clone the Repository**

2. **Compile the Unit Test Program**
    Compile `unit_test.cpp` using your C++ compiler:
    ```
    g++ -std=c++11 -o unit_test unit_test.cpp bigint.h
    ```
    This command compiles `unit_test.cpp` with the `bigint.h` header file.

    Or you can use any C++ framework to deal with project.

3. **Run the Unit Tests**
    Execute the compiled unit test program:
    ```
    ./unit_test
    ```
    This command runs the executable `unit_test`, which contains various tests to validate the functionality of the `BigInt` class.

4. **Verify Test Results**
    After running the tests, you should see output indicating whether each test passed successfully. For example:
    ```
    Running unit tests for BigInt class...
    Naive multiplication time: 1.1e-06 seconds
    Karatsuba multiplication time: 7e-07 seconds
    Caught expected overflow error
    All tests passed successfully!
    ```

## Key Features

**Construction and Initialization:**

- Constructors allow initialization from int64_t, std::string, and default constructor initializes to 0.
- Handles both positive and negative numbers with automatic handling of sign.

## Approach and Implementation Principle 

**Comparison Operations**

1. **Operations: <, <=, >, >=, ==**

    **Approach:**

     - Comparison operations for `BigInt` need to account for their arbitrary length and sign.
     - Each digit of `BigInt` needs to be compared starting from the most significant to determine the relationship between numbers.
     - Sign of numbers must be considered for correct comparisons.

    **Implementation Principle:**

     - **Operator `<`**: First check the sign. If `this` and `rhs` have different signs, the result is determined by the sign of `this`. If signs are the same, compare digits starting from the most significant.
     - **Operator `<=`**: Implemented as `!(rhs < *this)`.
     - **Operator `>`**: Implemented as `rhs < *this`.
     - **Operator `>=`**: Implemented as `!(rhs < *this)`.
     - **Operator `==`**: Compare signs and the `digits` vector for equality.
     - **Where `rhs` - is a `right-hand side`, like a second `BigInt`.**

**Arithmetic Operations**

2. **Operations: +, binary -, *, /, %, ****

    **Approach:**

    - Each operation must handle the sign and arbitrary length of numbers.
    - Efficient algorithms are necessary for performing operations on large numbers.

    **Implementation Principle:**

    - **Operator `+`**: Addition considering the sign. Handle carries between digits.
    - **Operator `-`**: Subtraction considering the sign. Handle borrows between digits.
    - **Operator `*`**: Multiplication using the Karatsuba algorithm for optimization.
    - **Operator `/` and `%`**: Division with sign consideration using long division to find quotient and remainder.
    - **Operator `**`**: Exponentiation using iterative multiplication for efficiency.

**Conversions**

3. **Conversions: `int -> BigInt`, `BigInt -> int`, `BigInt -> string`, `string -> BigInt`**

    **Approach:**

    - Implement functions for converting between `int`, `string`, and `BigInt`.
    - Handle potential errors such as overflow during conversions to `int`.

    **Implementation Principle:**

    - **`int -> BigInt`**: Convert integer to `BigInt` considering sign and digit grouping.
    - **`BigInt -> int`**: Convert `BigInt` to int, checking for overflow.
    - **`BigInt -> string`**: Convert `BigInt` to string considering sign and formatting.
    - **`string -> BigInt`**: Convert string to `BigInt`, considering sign and digit grouping.

**Karatsuba Multiplication Algorithm**

4. **Karatsuba Multiplication Algorithm:**

    **Approach:**

    - The Karatsuba algorithm efficiently multiplies large numbers using improved divide-and-conquer techniques.
    - It is particularly useful for large numbers where naive multiplication becomes too slow.

    **Implementation Principle:**

    - Divide each number into two roughly equal parts.
    - Recursively apply multiplication and addition for these parts.
    - Combine the results to obtain the final product.

# Conclusion

This `BigInt` class provides comprehensive functionality for working with large integers, including all fundamental operations, algorithms, and conversions. Each operation and algorithm is implemented with efficiency and edge case handling in mind, such as sign handling and digit management. 