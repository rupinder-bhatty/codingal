"""
1) Add the project title and topics.
   a) Label the program as "Kadane's Algorithm".
   b) Mention topics like subarrays, running sum, reset, and max-so-far tracker.

2) Show examples of subarrays.
   a) Create a list of positive and negative numbers.
   b) Print the full array.
   c) Use slicing to show different subarrays.
   d) Use `sum()` to print each subarray sum.

3) Trace the running sum.
   a) Start `running` from 0.
   b) Loop through each number in the array.
   c) Add each number to the running sum.
   d) Reset the running sum to 0 when it becomes negative.

4) Track the maximum subarray sum.
   a) Start `running` and `best` from 0.
   b) Add each number to the running sum.
   c) Reset running sum if it becomes negative.
   d) Update `best` when running sum becomes larger.

5) Apply Kadane's algorithm on a harder array.
   a) Create a second array with more positive and negative values.
   b) Repeat the running sum and reset logic.
   c) Keep updating the best maximum sum.
   d) Print the maximum subarray sum.
"""