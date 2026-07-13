"""
1) Add the project title and topics.
   a) Label the program as "Reverse Lab".
   b) Mention topics like digit extraction, reverse number, reverse string, and power of 4.

2) Scan the digits of a number.
   a) Ask the user to enter a number.
   b) Use `% 10` to get the last digit.
   c) Use `// 10` to remove the last digit.
   d) Repeat until no digits are left.

3) Create the `flipNumber()` function.
   a) Use recursion to reverse a number.
   b) Use the base case when only one digit is left.
   c) Extract the last digit using `% 10`.
   d) Recursively flip the remaining digits.
   e) Join the last digit and the flipped rest.

4) Test the number flipper.
   a) Ask the user to enter a number.
   b) Print the reversed number.

5) Create the `flipName()` function.
   a) Use recursion to reverse a string.
   b) Use the base case when only one character is left.
   c) Move the first character to the end after reversing the rest.

6) Test the name flipper.
   a) Ask the user to enter a name.
   b) Print the reversed name.

7) Create the `isPower4()` function.
   a) Return False for numbers less than or equal to 0.
   b) Return True if the number becomes 1.
   c) If the number is divisible by 4, call the function again with `n // 4`.
   d) Otherwise, return False.

8) Test the power of 4 checker.
   a) Test fixed values like 16 and 12.
   b) Ask the user to test their own number.
   c) Print whether it is a power of 4.
"""