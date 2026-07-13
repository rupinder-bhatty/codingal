"""
1) Add the lesson and activity details.
   a) Mention the lesson as "Introduction to Turtle".
   b) Mention the activity name as "Neon Mandala".
   c) Mention the file name as `neon-mandala.py`.

2) Import Turtle and create the screen.
   a) Import the `turtle` module.
   b) Create the drawing screen using `turtle.Screen()`.
   c) Set the background colour to black.
   d) Set the window title as "Neon Mandala".

3) Create the turtle drawing pen.
   a) Create a turtle object named `board`.
   b) Set its speed to fastest.
   c) Hide the turtle arrow using `hideturtle()`.

4) Draw the outer colour spiral.
   a) Create a list of neon colours.
   b) Use a loop to repeat the drawing 80 times.
   c) Cycle through colours using the remainder operator `%`.
   d) Move forward by an increasing distance.
   e) Turn right by 91 degrees to create a spiral effect.

5) Move to the centre and draw a filled star.
   a) Lift the pen using `penup()`.
   b) Move to the starting position using `goto()`.
   c) Set the turtle direction using `setheading()`.
   d) Put the pen down using `pendown()`.
   e) Use `begin_fill()` and `end_fill()` to colour the star.
   f) Use a loop to draw a 5-point star.

6) Draw the inner petal ring.
   a) Move the turtle back to the centre.
   b) Create a list of petal colours.
   c) Use an outer loop to draw 36 petals.
   d) Use an inner loop to draw one square petal.
   e) Fill each petal with colour.
   f) Turn slightly after each petal to create a circular pattern.

7) Keep the drawing window open.
   a) Use `turtle.done()` to display the completed mandala.
"""