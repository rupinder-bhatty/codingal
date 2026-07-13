"""
1) Add the project title and topics.
   a) Label the program as "Array Problems 3".
   b) Mention topics like binary arrays, streak counter, two pointers, and write-pointer pattern.

2) Count the current streak of 1s.
   a) Create a binary array with 0s and 1s.
   b) Start the streak from 0.
   c) Loop through each number.
   d) Reset the streak when the number is 0.
   e) Increase the streak when the number is 1.

3) Find the maximum consecutive 1s.
   a) Start both `streak` and `best` from 0.
   b) Loop through the binary array again.
   c) Reset streak on 0.
   d) Increase streak on 1.
   e) Update `best` whenever the current streak is higher.

4) Move all zeros to the end.
   a) Create a list with zeros and non-zero numbers.
   b) Use `zero` as the write pointer.
   c) Loop through the list using `nonzero`.
   d) Swap non-zero values to the front.
   e) Move the write pointer forward after each swap.

5) Print the write-pointer result.
   a) Show where the write pointer stopped.
   b) Print how many non-zero values are at the front.
   c) Print how many zeros are at the end.
"""