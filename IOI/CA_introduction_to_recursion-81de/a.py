"""
1) Add the project title and topics.
   a) Label the program as "Dream Recursion Lab".
   b) Mention topics like recursion, base case, build and unwind, factorial, and stack overflow.

2) Introduce recursion.
   a) Explain that recursion means a function calls itself.
   b) Mention that each recursive call should use a smaller problem.
   c) Mention that every recursive function needs a base case.

3) Create the `count_up()` function.
   a) Use a base case to stop when `n` is greater than 10.
   b) Print the current number.
   c) Call the function again with `n + 1`.

4) Create the `countdown()` function.
   a) Use a base case to stop when `n` becomes 0.
   b) Print "Liftoff!" at the end.
   c) Call the function again with `n - 1`.

5) Create the `factorial()` function.
   a) Use the base case when `n` is 0 or 1.
   b) Return 1 for the base case.
   c) Multiply `n` by `factorial(n - 1)` for the recursive case.
   d) Print factorial examples.

6) Demonstrate recursion limit.
   a) Import the `sys` module.
   b) Print Python’s current recursion limit.
   c) Temporarily reduce the recursion limit for a safe demo.

7) Create a function without a base case.
   a) Define `no_base_case()`.
   b) Keep calling the function again without stopping.
   c) Show how missing a base case causes a `RecursionError`.

8) Handle the stack overflow safely.
   a) Use `try` to run the unsafe recursive function.
   b) Use `except RecursionError` to catch the error.
   c) Print a message explaining stack overflow.

9) Reset the recursion limit.
   a) Set the recursion limit back to 1000.
   b) End with the rule that every recursive function must have a base case.
"""