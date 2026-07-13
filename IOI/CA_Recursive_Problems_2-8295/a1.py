"""
1) Add the activity details.
   a) Mention the activity name as "ClimbStairs".
   b) Mention the lesson, grade range, and file name.
   c) Explain that the program counts ways to climb stairs using recursion.

2) Create the `ways()` function.
   a) Define the function with `stairs` as the parameter.
   b) Use recursion to count paths using 1-step and 2-step moves.

3) Add the first base case.
   a) If `stairs` is less than 0, return 0.
   b) This means the path has gone past the top and is invalid.

4) Add the second base case.
   a) If `stairs` is equal to 0, return 1.
   b) This means the top was reached exactly, so one valid path is found.

5) Count the 2-step paths.
   a) Start `twoSteps` from 0.
   b) If at least 2 stairs remain, call `ways(stairs - 2)`.

6) Count the 1-step paths.
   a) Call `ways(stairs - 1)`.
   b) Store the result in `oneStep`.

7) Return the total number of paths.
   a) Add `twoSteps` and `oneStep`.
   b) Return the final result.

8) Take user input.
   a) Ask the user to enter the number of steps.
   b) Convert the input into an integer.

9) Print the result.
   a) Call the `ways()` function with the entered number.
   b) Display the number of ways to climb the stairs.
"""