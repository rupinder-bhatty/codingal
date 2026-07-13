"""
1) Add the project title and topics.
   a) Label the program as "Power Surge".
   b) Mention topics like `n & (n-1)`, powers of 2, powers of 4, powers of 8, and binary exponentiation.

2) Demonstrate the `n & (n-1)` trick.
   a) Store a number in `n`.
   b) Print `n`, `n - 1`, and `n & (n - 1)`.
   c) Show how this removes the rightmost set bit.

3) Check powers of 2.
   a) Loop through sample numbers.
   b) Check if the number is positive.
   c) Use `(x & (x - 1)) == 0` to check if only one bit is set.
   d) Print whether each number is a power of 2.

4) Create the `pow4()` function.
   a) First check if the number is a valid power of 2.
   b) Count how many right shifts are needed to reach 1.
   c) Return True if the bit position is even.
   d) Test the function with sample numbers.

5) Create the `pow8()` function.
   a) First check if the number is a valid power of 2.
   b) Count how many right shifts are needed to reach 1.
   c) Return True if the bit position is divisible by 3.
   d) Test the function with sample numbers.

6) Create the `fast_power()` function.
   a) Start the result from 1.
   b) Use a loop while the exponent is greater than 0.
   c) If the exponent is odd, multiply the result by the base.
   d) Square the base each time.
   e) Right-shift the exponent to halve it.
   f) Return the final result.

7) Test binary exponentiation.
   a) Calculate powers like 6^5, 2^10, and 3^8.
   b) Print the results.
"""