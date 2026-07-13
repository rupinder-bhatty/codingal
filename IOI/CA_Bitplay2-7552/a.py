"""
1) Add the project title and topics.
   a) Label the program as "Bit Play".
   b) Mention topics like set bits, zero bits, bit masks, and checking nth bit.

2) Create a number for bit practice.
   a) Store `52` in variable `n`.
   b) Note its binary form as `110100`.

3) Create the `bits()` helper function.
   a) Convert a number into binary.
   b) Remove the `0b` prefix using slicing.

4) Display set bits and zero bits.
   a) Print the number and its binary form.
   b) Count the number of `1`s using `.count('1')`.
   c) Count the number of `0`s using `.count('0')`.

5) Count set bits manually.
   a) Start `count` from 0.
   b) Store `n` in a temporary variable.
   c) Use a `while` loop to check each bit.
   d) Increase the count when the last bit is 1.
   e) Shift the number right by 1 each time.

6) Find the first set bit.
   a) Start the position from 1.
   b) Check each bit from right to left.
   c) Stop when the first `1` bit is found.
   d) Print the position of the first set bit.

7) Build bit masks.
   a) Use a loop from 0 to 5.
   b) Use `1 << i` to create each bit mask.
   c) Print each mask in decimal and binary form.

8) Check if each bit is set.
   a) Loop through bit positions 1 to 6.
   b) Use `n & (1 << (bit - 1))` to check each bit.
   c) Print whether each bit is SET or NOT SET.
"""