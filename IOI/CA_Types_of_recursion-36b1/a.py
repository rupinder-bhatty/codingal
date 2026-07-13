"""
1) Add the project title and topics.
   a) Label the program as "Recursion Patterns".
   b) Mention patterns like linear, tail, head, increasing-decreasing, and tree recursion.

2) Create the `linear()` function.
   a) Use a base case to stop when `n` becomes 0.
   b) Print the current number.
   c) Make exactly one recursive call with `n - 1`.

3) Create the `tail()` function.
   a) Use a base case to stop at 0.
   b) Do the work first by printing `n`.
   c) Make the recursive call at the end.

4) Create the `head()` function.
   a) Use a base case to stop at 0.
   b) Make the recursive call first.
   c) Print `n` while the calls are returning.

5) Create the `inc_dec()` function.
   a) Print `n` before the recursive call.
   b) Call the function again with `n - 1`.
   c) Print `n` again while coming back up.

6) Create the `tree()` function.
   a) Use a base case to stop at 0.
   b) Print the current number.
   c) Make two recursive calls with `n - 1`.

7) Run each recursion pattern.
   a) Call each function with a sample number.
   b) Print headings to show what each pattern does.
   c) Show that tree recursion branches double at each level.
"""