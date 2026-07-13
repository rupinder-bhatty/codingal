"""
1) Create the `Cricket` class.
   a) Define the constructor with player and score.
   b) Store player and score as private attributes using double underscores.

2) Add methods inside the `Cricket` class.
   a) Create `info()` to display cricket player details.
   b) Create `play()` to show cricket-specific action.
   c) Create `get_score()` to read the private score.
   d) Create `set_score()` to update the score safely.

3) Create the `Football` class.
   a) Define the constructor with player and score.
   b) Store player and score as private attributes.

4) Add methods inside the `Football` class.
   a) Create `info()` to display football player details.
   b) Create `play()` to show football-specific action.
   c) Create `get_score()` to read the private score.
   d) Create `set_score()` to update the score safely.

5) Create sports objects.
   a) Create one Cricket object.
   b) Create one Football object.

6) Demonstrate polymorphism.
   a) Loop through both sports objects.
   b) Call the same `info()` method on each object.
   c) Call the same `play()` method on each object.
   d) Observe how the same method names give different outputs.

7) Demonstrate encapsulation.
   a) Try to directly change the private cricket score.
   b) Use `get_score()` to show that the private score is still protected.

8) Update scores safely.
   a) Use `set_score()` to update the cricket score.
   b) Use `set_score()` to update the football score.
   c) Prevent negative scores using a condition inside the setter.
"""