"""
1) Add the project title and topics.
   a) Label the program as an algorithm analysis activity.
   b) Mention the topics: algorithm, pseudocode, time complexity, space complexity, and efficiency comparison.

2) Define the problem.
   a) Set `n = 4` rounds.
   b) Explain that each round gives points equal to its round number.
   c) Print the activity heading.

3) Solve using the formula method.
   a) Use the formula `n * (n + 1) // 2`.
   b) Store the answer in `total`.
   c) Print the total and show that it takes only 1 step.

4) Solve using the loop method.
   a) Start `total` and `steps` from 0.
   b) Use a `for` loop from 1 to `n`.
   c) Add each round number to the total.
   d) Count one step for each loop run.
   e) Print the total and number of steps.

5) Solve using the nested loop method.
   a) Start `total` and `steps` from 0.
   b) Use one loop for rounds.
   c) Use another loop to add points one by one.
   d) Count each inner loop run as a step.
   e) Print the total and number of steps.

6) Test with a larger value.
   a) Change `n` to 10.
   b) Count the nested loop steps again.
   c) Print the steps for formula, loop, and nested loop methods.

7) Compare efficiency.
   a) Show that all methods give the same answer.
   b) Explain that their step counts are different.
   c) Connect this difference to time complexity.
"""