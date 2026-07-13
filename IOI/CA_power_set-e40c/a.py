"""
1) Add the project title and topics.
   a) Label the program as "Power Map".
   b) Mention topics like power set, binary mask, bit probe, subset enumeration, and bit difference.

2) Create the item list.
   a) Store items like A, B, and C in a list.
   b) Find the number of items using `len()`.
   c) Calculate total subsets using `2 ** n`.

3) Display the binary mask table.
   a) Loop from 0 to total subsets minus 1.
   b) Treat each number as a binary mask.
   c) Extract each bit using right shift and `& 1`.
   d) Print which bits are on or off.

4) Build all subsets using bit probes.
   a) Loop through every mask.
   b) Start with an empty subset list.
   c) Use `1 << j` to create a probe for each item.
   d) Use `mask & probe` to check if the item should be included.
   e) Print each subset.

5) Create the `bit_diff()` function.
   a) Start the flip count from 0.
   b) Compare the last bit of both numbers using `& 1`.
   c) Increase the count when the bits are different.
   d) Right-shift both numbers to check the next bits.
   e) Return the total number of different bit positions.

6) Test bit difference.
   a) Compare sample number pairs.
   b) Print how many bit positions are different.
   c) Show that equal numbers have 0 bit differences.
"""