"""
1) Add the project title and file name.
   a) Label the program as "Phone Keypad Combinations".
   b) Mention the file name as `phone-keypad.py`.

2) Create the keypad mapping.
   a) Use a dictionary to store digits as keys.
   b) Store the matching letters for each digit from 2 to 9.
   c) Use lists to hold multiple letters for each digit.

3) Create the recursive `combinations()` function.
   a) Take `digits` and `current` as parameters.
   b) Use `digits` to track the remaining numbers.
   c) Use `current` to build the current letter combination.

4) Add the base case.
   a) If no digits are left, print the current combination.
   b) Return to stop that recursive path.

5) Explore each possible letter.
   a) Take the first digit from the input.
   b) Store the remaining digits separately.
   c) Loop through each letter linked to the first digit.
   d) Call the function again with the remaining digits and updated combination.

6) Take user input.
   a) Ask the user to enter digits such as 23.
   b) Print a heading for all combinations.
   c) Call `combinations(number, "")` to start recursion.

7) Count the total combinations.
   a) Start count from 1.
   b) Loop through each digit in the input.
   c) Multiply count by the number of letters for that digit.
   d) Print the total number of combinations.
"""