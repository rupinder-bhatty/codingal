"""
1) Add the project title and topics.
   a) Label the program as "Array Problems 2".
   b) Mention topics like stock buy-sell, tallest bars, and rainwater trapped.

2) Calculate maximum stock profit.
   a) Create a list of stock prices.
   b) Start profit from 0.
   c) Loop through prices from the second day.
   d) Add profit whenever today’s price is higher than yesterday’s price.
   e) Print the maximum profit.

3) Find left tallest bars.
   a) Create a list of building heights.
   b) Create a `left_tallest` list filled with 0s.
   c) Store the first height as the first left tallest value.
   d) Loop from left to right.
   e) Store the maximum height seen so far.

4) Find right tallest bars.
   a) Create a `right_tallest` list filled with 0s.
   b) Store the last height as the first right-side value.
   c) Loop from right to left.
   d) Store the maximum height seen so far.

5) Calculate trapped rainwater.
   a) Start water from 0.
   b) Loop through each bar.
   c) Find the smaller value between left tallest and right tallest.
   d) Subtract the current height to find trapped water at that bar.
   e) Add it to the total water.

6) Print the final result.
   a) Show the original heights.
   b) Show left tallest and right tallest lists.
   c) Print the total water trapped.
"""